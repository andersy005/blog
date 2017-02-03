---
layout:     post
title:      Quantum Mechanics - The Wave Function
date:       2017-02-02 20:00:00
author:     "Anderson Banihirwe"
header-img: "img/post-02.png"

---

<div id="test">
<p>Imagine a particle of mass m, constrained to move along the x-axis, subject to some specified force $F(x,t)$.<br>
 <img src="{{ site.baseurl }}/img/particle.PNG"  alt="Particle Image"></p>
<p><strong>Classical Mechanics</strong> approaches this problem with the objective of determining the position of the particle at any given time $x(t)$. Once we know that, we can figure out:</p>
<ul>
<li id="test">The velocity ($v=\frac{dx}{dt}$)</li>
<li >The momentum ($p=mv$)</li>
<li>The kinetic Energy($T=\frac{mv^2}{2}$)</li>
<li>Any other dynamical variable of interest</li>
</ul>
<p>We get $x(t)$ by applying Newton’s second law: $F=ma$</p>
<p><strong>Quantum Mechanics</strong> approaches the same problem quite differently. In this case we look for the particle’s <em>wave function</em>, $\Psi (x,t)$ and we get it by solving one of the famous equation, the <strong>Schrödinger equation</strong>:<br><br><br>
<span class="math inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mi mathvariant="normal">ℏ</mi><mfrac><mrow><mi mathvariant="normal">∂</mi><mi mathvariant="normal">Ψ</mi></mrow><mrow><mi mathvariant="normal">∂</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>−</mo><mfrac><mrow><msup><mi mathvariant="normal">ℏ</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mfrac><mrow><msup><mi mathvariant="normal">∂</mi><mn>2</mn></msup><mi mathvariant="normal">Ψ</mi></mrow><mrow><mi mathvariant="normal">∂</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>V</mi><mi mathvariant="normal">Ψ</mi></mrow><annotation encoding="application/x-tex">i\hbar\frac{\partial \Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial ^2 \Psi}{\partial x^2}+V\Psi</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height:0.97032em;"></span><span class="strut bottom" style="height:1.3153199999999998em;vertical-align:-0.345em;"></span><span class="base textstyle uncramped"><span class="mord mathit">i</span><span class="mord">ℏ</span><span class="minner reset-textstyle textstyle uncramped"><span class="mfrac"><span class="vlist"><span style="top:0.345em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle cramped"><span class="mord scriptstyle cramped"><span class="mord" style="margin-right:0.05556em;">∂</span><span class="mord mathit">t</span></span></span></span><span style="top:-0.22999999999999998em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle textstyle uncramped frac-line"></span></span><span style="top:-0.394em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord scriptstyle uncramped"><span class="mord" style="margin-right:0.05556em;">∂</span><span class="mord">Ψ</span></span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span></span><span class="mrel">=</span><span class="mord">−</span><span class="minner reset-textstyle textstyle uncramped"><span class="mfrac"><span class="vlist"><span style="top:0.345em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle cramped"><span class="mord scriptstyle cramped"><span class="mord">2</span><span class="mord mathit">m</span></span></span></span><span style="top:-0.22999999999999998em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle textstyle uncramped frac-line"></span></span><span style="top:-0.394em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord scriptstyle uncramped"><span class="mord"><span class="mord">ℏ</span><span class="vlist"><span style="top:-0.363em;margin-right:0.07142857142857144em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-scriptstyle scriptscriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span></span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span></span><span class="minner reset-textstyle textstyle uncramped"><span class="mfrac"><span class="vlist"><span style="top:0.345em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle cramped"><span class="mord scriptstyle cramped"><span class="mord" style="margin-right:0.05556em;">∂</span><span class="mord"><span class="mord mathit">x</span><span class="vlist"><span style="top:-0.289em;margin-right:0.07142857142857144em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-scriptstyle scriptscriptstyle cramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span></span></span></span><span style="top:-0.22999999999999998em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle textstyle uncramped frac-line"></span></span><span style="top:-0.394em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord scriptstyle uncramped"><span class="mord"><span class="mord" style="margin-right:0.05556em;">∂</span><span class="vlist"><span style="top:-0.363em;margin-right:0.07142857142857144em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-scriptstyle scriptscriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span><span class="mord">Ψ</span></span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span></span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mord">Ψ</span></span></span></span></span></p>
<ul>
<li>$i$ is the square root of $-1$</li>
<li>$\hbar$ is Planck’s constant divide by $2\pi$</li>
</ul>
<p>The Schrödinger equation plays a role analogous to Newton’s second law:</p>
<blockquote>
<p>Given suitable initial conditions (typically, $\Psi(x,0)$), the Schrödinger equation determines $\Psi(x,t)$ for all future time.</p>
</blockquote>
<p><strong>Borns’s statistical interpretation</strong> provides an answer to the question, &quot; what exactly is the wave function and what does it do for you once you’ve got it?&quot;.</p>
<p>Born’s statistical interpretation of the wave function says that $
\left |\Psi(x,t)  \right |^2$ gives the <strong>probability</strong> of finding the particle at point $x$, at time $t$ or more precisely</p>
<p>$$
\left |\Psi(x,t)  \right |^2 = \begin{Bmatrix}
\text{probability of finding the particle
between x and (x+dx) at time t}
\end{Bmatrix}$$</p>
<p>The statistical interpretation introduces a kind of <strong>indeterminacy</strong> into quantum mechanics, for even if you know everything the theory has to tell you about the particle, you cannot predict with certainty the outcome of a simple experiment to measure its position.</p>
<blockquote>
<p>All quantum mechanics has to offer is <strong>statistical information</strong> about the <strong>possible results</strong>.</p>
</blockquote>

</div>
Resources: [Introduction To Quantum Mechanics by Griffts](https://www.amazon.com/Introduction-Quantum-Mechanics-David-Griffiths/dp/1107179866/ref=sr_1_1?ie=UTF8&qid=1486084860&sr=8-1&keywords=introduction+to+quantum)
<script>
      renderMathInElement(
          document.getElementById("test"),
          {
              delimiters: [
                  {left: "$$", right: "$$", display: true},
                  {left: "\\[", right: "\\]", display: true},
                  {left: "$", right: "$", display: false},
                  {left: "\\(", right: "\\)", display: false}
              ]
          }
      );
    </script>