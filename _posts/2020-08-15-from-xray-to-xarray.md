---
keywords: xarray
description: ""
title: From xray to xarray
badges: false
comments: true
author: Anderson
layout: post
toc: false
categories: ["2020", "xarray", "todayilearned"]
---

I started using [xarray](https://github.com/pydata/xarray) in the summer of 2017. At the time, the latest version was `v0.9.5`. Today I learned that in its early stages, xarray was called **xray** (no ties to [x-ray machines](https://en.wikipedia.org/wiki/X-ray_machine) :)). Once it gained popularity, the core developers decided it was a good idea to rename the package to a more descriptive/neutral name. The following names were considered:

- **pandasnd**: pandasnd was abandoned because it promised too much, and the core devs didn't want to tie xarray to the pandas approach. I wonder if today we would have imported it as:

  ```python
  import pandasnd as pdnd # 🤔

  # or

  import pandasnd as pdd # 🤔

  ```
- **scikit-xray**: this one was abandoned because **xarray** was a better alternative to **xray**.
Here's a screenshot of some of the discussions about the name change:
![](/images/xray-to-xarray.png "https://gitter.im/pydata/xarray")
