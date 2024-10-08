# Configuration file for the Sphinx documentation builder.
import datetime
import pathlib
from textwrap import dedent
from urllib.parse import urlparse

import yaml
from sphinx.application import Sphinx
from sphinx.util import logging

LOGGER = logging.getLogger('conf')

# -- Project information -----------------------------------------------------

project = 'Paysage Pythonique'
license_message = (
    'Except where otherwise noted, this work is licensed under '
    'a Creative Commons Attribution-ShareAlike 4.0 International License'
)
copyright = f'2018-{datetime.datetime.now().year}. {license_message}'
author = 'Anderson Banihirwe'
html_last_updated_fmt = '%b %d, %Y'

extensions = [
    'myst_nb',
    'ablog',
    'sphinx_panels',
    'sphinx_design',
    'sphinxcontrib.bibtex',
    'sphinxext.opengraph',
    'sphinx_comments',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '*import_posts*',
    '**/pandoc_ipynb/inputs/*',
]

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'github_url': 'https://github.com/andersy005/',
    'twitter_url': 'https://twitter.com/andersy005',
    'search_bar_text': 'Search this site...',
    'google_analytics_id': 'UA-91185106-1',
    'search_bar_position': 'navbar',
}
html_theme_options['analytics'] = {
    # The domain you'd like to use for this analytics instance
    'plausible_analytics_domain': 'blog.andersonbanihirwe.dev',
    # The analytics script that is served by Plausible
    'plausible_analytics_url': 'https://plausible.andersonb.xyz/js/script.js',
}

html_favicon = '_static/share.png'
html_title = ''

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ['feed.xml']
html_sidebars = {
    'index': ['hello.html'],
    'about': ['hello.html'],
    'publications': ['hello.html'],
    'projects': ['hello.html'],
    'talks': ['hello.html'],
    'posts': ['tagcloud.html', 'archives.html'],
    'posts/**': ['postcard.html', 'recentposts.html', 'archives.html'],
}
blog_baseurl = 'https://blog.andersonbanihirwe.dev'
blog_title = 'Paysage Pythonique'
blog_path = 'posts'
fontawesome_included = True
blog_post_pattern = 'posts/*/*'
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 1


# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ['http', 'https', 'mailto']

# OpenGraph config
ogp_site_url = 'https://blog.andersonbanihirwe.dev'
ogp_image = 'https://blog.andersonbanihirwe.dev/_static/share.png'
ogp_site_name = f' {blog_title} | Anderson Banihirwe'
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta name="twitter:site" content="@andersy005" />',
    '<meta name="twitter:creator" content="@andersy005" />',
]

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = 'off'

comments_config = {
    'utterances': {'repo': 'andersy005/blog', 'optional': 'config', 'label': '💬 comment'},
    'hypothesis': False,
}


def build_teaching_gallery(app: Sphinx):
    LOGGER.info('Building teaching gallery')
    path = pathlib.Path(app.srcdir) / 'config_data/teaching.yaml'
    teaching = yaml.safe_load(path.read_text())
    teaching = sorted(teaching, key=lambda item: item['date'])
    grid_items = []
    for item in teaching:
        if not item.get('video'):
            item['video'] = '...'

        repo_text = ''
        star_text = ''

        if item['repository']:
            repo_text = f'{{bdg-link-secondary}}`repo <{item["repository"]}>`'

            try:
                url = urlparse(item['repository'])
                if url.netloc == 'github.com':
                    _, org, repo = url.path.rstrip('/').split('/')
                    link = f'https://img.shields.io/github/stars/{org}/{repo}?style=social'
                    star_text = f"[![GitHub Repo stars]({link})]({item['repository']})"
            except Exception:
                pass

        grid_items.append(
            f"""\
        `````{{grid-item-card}} {" ".join(item["name"].split())}
        :text-align: center
        {item["video"]}
        +++

        ````{{grid}} 2 2 2 2
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :gutter: 1

        ```{{grid-item}}
        :child-direction: row
        :child-align: start
        :class: sd-fs-5
        {repo_text}
        ```

        ```{{grid-item}}
        :child-direction: row
        :child-align: end
        {star_text}
        ```

        ````

        `````
        """
        )
    grid_items = '\n'.join(grid_items)

    panels = f"""``````{{grid}} 2
:class-container: full-width

{dedent(grid_items)}
``````
    """
    (pathlib.Path(app.srcdir) / 'teaching_gallery.md').write_text(panels)


def build_talks_gallery(app: Sphinx):
    LOGGER.info('Building talks gallery')
    path = pathlib.Path(app.srcdir) / 'config_data/talks.yaml'
    talks = yaml.safe_load(path.read_text())
    talks = sorted(talks, key=lambda item: item['conference']['date'], reverse=True)
    LOGGER.info(f'Found {len(talks)} talks')
    content = [
        """\
```{panels}
:card: text-center
"""
    ]
    for index, item in enumerate(talks):
        content.append(
            f"""\
[{item['title']}]({item['slides']})
^^^
{item['video']}
+++
{item['conference']['name']} | {item['conference']['location']} | {item['conference']['date']}
"""
        )

        if index < len(talks) - 1:
            content.append(
                """\
---
"""
            )

    content.append(
        """\
```"""
    )

    content = dedent('\n'.join(content))
    out_path = pathlib.Path(app.srcdir) / 'talks_gallery.md'
    out_path.write_text(content)


def setup(app: Sphinx):
    app.add_css_file('custom.css')
    app.connect('builder-inited', build_talks_gallery)
    app.connect('builder-inited', build_teaching_gallery)
