PRINICPLES OF
MATHEMATICAL
ANALYSIS

# INTERNATIONAL SERIES IN PURE AND APPLIED MATHEMATICS 

William Ted Martin, E.H. Spainer, G. Springer and P.J. Davis. Consulting Editors

AHLFORS: Complex Analysis
BuCK: Advanced Calculus
BuSACKER AND SAATY: Finite Graphs and Networks
CHENEY: Introduction to Approximation Theory
CHESTER: Techniques in Partial Differential Equations
Coddington and Levinson: Theory of Ordinary Differential Equations
CONTE AND DE BOOR: Elementary Numerical Analysis: An Algorithmic Approach
DENNEMEYER: Introduction to Partial Differential Equations and Boundary Value Problems
Dettman: Mathematical Methods in Physics and Engineering
Golomb and Shanks: Elements of Ordinary Differential Equations
Greenspan: Introduction to Partial Differential Equations
Hamming: Numerical Methods for Scientists and Engineers
Hildebrand: Introduction to Numerical Analysis
Householder: The Numerical Treatment of a Single Nonlinear Equation
Kalman, Falb, and Arbib: Topics in Mathematical Systems Theory
LASS: Vector and Tensor Analysis
McCARTY: Topology: An Introduction with Applications to Topological Groups
MONK: Introduction to Set Theory
MOore: Elements of Linear Algebra and Matrix Theory
MOSTOW AND SAMPSON: Linear Algebra
MourSund and Duris: Elementary Theory and Application of Numerical Analysis
Pearl: Matrix Theory and Finite Mathematics
Pipes and Harvill: Applied Mathematics for Engineers and Physicists
Ralston: A First Course in Numerical Analysis
Ritger and Rose: Differential Equations with Applications
RITT: Fourier Series
Rudin: Principles of Mathematical Analysis
ShAPIRO: Introduction to Abstract Algebra
Simmons: Differential Equations with Applications and Historical Notes
Simmons: Introduction to Topology and Modern Analysis
Sneddon: Elements of Partial Differential Equations
Struble: Nonlinear Differential Equations

McGraw-Hill, Inc.
New York St. Louis San Francisco Auckland Bogotá
Caracas Lisbon London Madrid Mexico City Milan
Montreal New Delhi San Juan Singapore
Sydney Tokyo Toronto

WALTER RUDIN
Professor of Mathematics
University of Wisconsin-Madison

# Principles of Mathematical Analysis <br> THIRD EDITION

This book was set in Euler.
The editors were A. Anthony Arthur and Shelly Levine Langman; the production supervisor was Leroy A. Young.
R.R. Donnelley \& Sons Company was printer and binder.

This book is printed on acid-free paper.

# Library of Congress Cataloging in Publication Data 

Rudin, Walter, date
Principles of mathematical analysis.
(International series in pure and applied mathematics)
Bibliography: p .
Includes index.

1. Mathematical Analysis. I. Title

QA300.R8 1976 515 75-17903
ISBN-13: 978-0-07-054235-8
ISBN-10: 0-07-054235-X

## PRINCIPLES OF MATHEMATICAL ANALYSIS

Copyright © 1964, 1976 by McGraw-Hill, Inc. All rights reserved.
Copyright 1953 by McGraw-Hill, Inc. All rights reserved.
Printed in the United States of America. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of the publisher.
42434445 DOC 154321

# FOREWORD 

Well, I have decided to completely retype Rudin's Principles of Mathematical Analysis from scratch. There really are not many compelling reasons to do this-I decided to begin the project just because I was tired of the fact that any time I wanted to consult Rudin, I had to pull up a scanned copy of a book from the 1970s. Is this a good reason? Probably not, as who will find value in this document? The main group of people that need to consult Rudin are undergraduates in analysis courses that use Rudin. But somebody has to do the work that nobody else will.

My original plan was to type 2 pages per day and be done in six months. However, to my surprise, five other people were willing to help me by typesetting some of the chapters. This made the work go much faster than it otherwise would have, and probably prevented me from only typing the first seven chapters before calling it quits. Thank you. Of course, all of us will remain anonymous due to the fact that this is a blatant violation of copyright law.

I have made modifications in several places, including global changes to Rudin's outdated (or simply bad) notation. These changes are:

- Rather than denoting the field of real numbers by R and the field of rational numbers by Q , I have denoted them by $\mathbb{R}$ and $\mathbb{Q}$, respectively. The same is true for $\mathrm{R}^{\mathrm{k}}$.
- Rather than denoting the set of positive integers by J, I denote it by $\mathbb{N}$.
- Rather than denoting sequences by $\left\{s_{k}\right\}$, they are denoted by $\left\{s_{k}\right\}$ or $\left\{s_{k}\right\}_{k=1}^{\infty}$. A real valued sequence is an element of the product $\mathbb{R}^{\mathbb{N}}$, and so modern notation has one write them as ordered tuples. The notation $\left\{s_{k}\right\}$ appears to define the range of a sequence, not the sequence itself.
- Rather than denoting an ordered k-tuple by $\left\{i_{1}, \ldots, i_{k}\right\}$ as Rudin does in Theorem 10.14, I have used the notation $\left(i_{1}, \ldots, i_{k}\right)$. That Rudin does not do this is especially strange, given the fact that he does use this notation in Definition 9.33.
- Some sections, such as Definition 10.18, have been converted into a definition environment, as that is what their essential purpose is. I have put the title of the section as Rudin has written it in parenthesis. This shouldn't cause any major confusion, as the section number is unchanged (and uniquely identifies each section of the book).
- Proofs are non-indented and written in proof environments; as a result, they now end with a $\square$ symbol.
- Rather than using the term "nonabsolutely" as Rudin does in Remark 3.46, I have used the word "conditionally," as it is much more standard. I have inserted "[[nonabsolutely]]" after the first instance in which I do this.
- Rather than denoting a continuously differentiable function by $\mathscr{C}^{\prime}$, I have denoted it by $\mathscr{C}^{1}$. Similarly, a function that is twice continuously differentiable is denoted by $\mathscr{C}^{2}$, etc.
- At my discretion, I have converted inline math fractions such as $\frac{1}{2}, \frac{x}{|x|}$ to be in the form $1 / 2, x /|x|$. Rudin uses both styles and is not consistent. I have tried to be more consistent than he was.

- The remark above goes for summation symbols too. I have mostly followed the notation $\Sigma a_{n}$, but in some instances (when the series is sufficiently complex), I have used $\sum$ when Rudin uses $\Sigma$.
- Rather than referencing exercises as "Exercise 5, Chapter 3," they are referenced as "Exercise 3.5." As a result, the exercises are numbered as C.E, where $C$ is the chapter and $E$ is the exercise number as it appears in Rudin.
- Instead of writing $\bigcap_{1}^{n} E_{j}$, I have written it in full as $\bigcap_{j=1}^{n} E_{j}$.
- Some multi-line equations in Rudin are labeled via a single number that appears only on the first line, yet the number is supposed to label the entire multi-line series of equations. I have fixed this.
- In the proof of Theorem 3.54, I have shrunk the text size of one of the equations in order to make it fit on the page. Rudin opts for an uglier solution of adding an extra line that only contains $-\cdots-Q_{k_{2}}<\alpha_{2}$ at the very end.
- In Definition 5.1, Rudin says "If $f^{\prime}$ is defined at every point of a set $E \subset[a, b]$, $f$ is said to be differentiable on $E$." However, in Theorems (or proofs of) 5.9, 5.10 and 5.11 , he says " f is differentiable in $(a, b)$ " to mean $f^{\prime}$ is defined at every point of $(a, b) \subset[a, b]$. In the Corollary to Theorem 5.12, he uses "on" when $f$ is defined on $[a, b]$ and $f^{\prime}$ is differentiable at every point of $[a, b]$. In Theorem 5.13, he again uses "in" for the situation where f is defined on [a, b] and differentiable at every point of $(a, b)$.

This situation continues on. It seems as if Rudin wants to say "differentiable on $E$ " for the situation where $f$ is defined on $E$ and differentiable at every point of $E$. However, that is not how he defined it. As a result, I have changed all instances of "differentiable in E" to "differentiable on E," to agree with his definition.

- Many typos have been fixed; however, I can't help but feel it is likely that even more have been introduced.
- Instead of placing a footnote to credit V.P. Havin for the proof of Theorem 5.19, I have written Proof (V.P. Havin). I did this primarily because of whitespace issues. Let it be noted here that he also translated the second edition of this book into Russian.

Throughout the entire book, I have altered the way that Rudin uses commas and creates paragraphs. Rudin is inconsistent with his comma usage and often grammatically incorrect. He also seems to make new paragraphs whenever he feels that he is saying something slightly different than the previous sentencethere are many points throughout the book where he chains three one-sentence paragraphs together, which I believe is simply bad style.

Page numbering is not identical: this document is slightly shorter than Rudin's book. All equation/exercise/theorem/corollary/definition/section/etc. numbering is consistent with Rudin's original copy, however.

The page immediately before this foreword is copied exactly how it appears in my "International Series in Pure and Applied Mathematics" copy, and so all relevant data refers to that edition.

Should you wish, you could conceivably print this book out and bind it in some way. The PDF has dimensions that are exactly the same as Rudin's book (each page

is $\forall$ in by $\omega$ in), and the font size is 9 pt , as $\mathrm{LA}_{\mathrm{E}} \mathrm{X}$ defines it, if you're curious.

# Contents 

Foreword ..... i
Preface ..... viii
1 The Real and Complex Number Systems ..... 1
Introduction ..... 1
Ordered Sets ..... 3
Fields ..... 5
The Real Field ..... 8
The Extended Real Number System ..... 10
The Complex Field ..... 11
Euclidean Spaces ..... 14
Appendix ..... 16
Exercises ..... 20
2 Basic Topology ..... 22
Finite, Countable, and Uncountable Sets ..... 22
Metric Spaces ..... 28
Compact Sets ..... 33
Perfect Sets ..... 37
Connected Sets ..... 38
Exercises ..... 39
3 Numerical Sequences and Series ..... 43
Convergent Sequences ..... 43
Subsequences ..... 47
Cauchy Sequences ..... 48
Upper and Lower Limits ..... 51
Some Special Sequences ..... 52
Series ..... 54
Series of Nonnegative terms ..... 56
The Number e ..... 58
The Root and Ratio Tests ..... 60
Power Series ..... 63

Summation by Parts ..... 64
Absolute Convergence ..... 66
Addition and Multiplication of Series ..... 66
Rearrangements ..... 69
Exercises ..... 72
4 Continuity ..... 76
Limits of Functions ..... 76
Continuous Functions ..... 78
Continuity and Compactness ..... 81
Continuity and Connectedness ..... 85
Discontinuities ..... 86
Monotonic Functions ..... 87
Infinite Limits and Limits at Infinity ..... 89
Exercises ..... 90
5 Differentiation ..... 94
The Derivative of a Real Function ..... 94
Mean Value Theorems ..... 97
The Continuity of Derivatives ..... 99
L'Hôpital's Rule ..... 99
Derivatives of Higher Order ..... 100
Taylor's Theorem ..... 101
Differentiation of Vector-valued Functions ..... 102
Exercises ..... 104
6 The Riemann-Stieltjes Integral ..... 110
Definition and Existence of the Integral ..... 110
Properties of the Integral ..... 118
Integration and Differentiation ..... 123
Rectifiable Curves ..... 126
Exercises ..... 128
7 Sequences and Series of Functions ..... 132
Discussion of the Main Problem ..... 132
Uniform Convergence ..... 135
Uniform Convergence and Continuity ..... 137
Uniform Convergence and Integration ..... 140
Uniform Convergence and Differentiation ..... 141
Equicontinuous Families of Functions ..... 143
The Stone-Weierstrass Theorem ..... 147
Exercises ..... 153

8 Some Special Functions ..... 159
Power Series ..... 159
The Exponential and Logarithmic Functions ..... 165
The Trigonometric Functions ..... 169
The Algebraic Completeness of the Complex Field ..... 171
Fourier Series ..... 172
The Gamma Function ..... 179
Exercises ..... 183
9 Functions of Several Variables ..... 190
Linear Transformations ..... 190
Differentiation ..... 197
The Contraction Principle ..... 206
The Inverse Function Theorem ..... 207
The Implicit Function Theorem ..... 210
The Rank Theorem ..... 214
Determinants ..... 218
Derivatives of Higher Order ..... 221
Differentiation of Integrals ..... 222
Exercises ..... 225
10 Integration of Differential Forms ..... 230
Integration ..... 230
Primitive Mappings ..... 233
Partitions of Unity ..... 235
Change of Variables ..... 236
Differential Forms ..... 238
Simplexes and Chains ..... 251
Stokes' Theorem ..... 257
Closed Forms and Exact Forms ..... 260
Vector Analysis ..... 265
Exercises ..... 273
11 The Lebesgue Theory ..... 282
Set Functions ..... 282
Construction of the Lebesgue Measure ..... 284
Measure Spaces ..... 291
Measurable Functions ..... 292
Simple Functions ..... 294
Integration ..... 295
Comparison with the Riemann Integral ..... 303
Integration of Complex Functions ..... 306
Functions of Class $\mathscr{L}^{2}$ ..... 307
Exercises ..... 313

Bibliography ..... 316

# PREFACE 

This book is intended to serve as a text for the course in analysis that is usually taken by advanced undergraduates or by first-year students who study mathematics.

The present edition covers essentially the same topics as the second one, with some additions, a few minor omissions, and considerable rearrangement. I hope that these changes will make the material more accessible and more attractive to the students who take such a course.

Experience has convinced me that it is pedagogically unsound (though logically correct) to start off with the construction of the real numbers from the rational ones. At the beginning, most students simply fail to appreciate the need for doing this. Accordingly, the real number system is introduced as an ordered field with the least-upper-bound property, and a few interesting applications of this property are made. However, Dedekind's construction is not omitted. It is now in an Appendix to Chapter 1, were it may be studied and enjoyed whenever the time seems ripe.

The material on functions of several variables is almost completely rewritten, with many details filled in, and with more examples and more motivation. The proof of the inverse function theorem-the key item in Chapter 9-is simplified by means of the fixed point theorem about contraction mappings. Differential forms are discussed in much greater detail. Several applications of Stokes' theorem are included.

As regards other changes, the chapter on the Riemann-Stieltjes integral has been trimmed a bit, a short do-it-yourself section on the gamma function has been added to Chapter 8, and there is a large number of new exercises, most of them with fairly detailed hints.

I have also included several references to articles appearing in the American Mathematical Monthly and in Mathematics Magazine, in the hope that students will develop the habit of looking into the journal literature. Most of these references were kindly supplied by R. B. Burckel.

Over the years, many people students as well as teachers, have sent me corrections, criticisms, and other comments concerning the previous edition of this book. I have appreciated these, and I take this opportunity to express my sincere thanks to all who have written me.

# Chapter 1 

## THE REAL AND COMPLEX NUMBER SYSTEMS

## INTRODUCTION

A satisfactory discussion of the main concepts of analysis (such as convergence, continuity, differentiation, and integration) must be based on an accurately defined number concept. We shall not, however, enter into any discussion of the axioms that govern the arithmetic of the integers, but assume familiarity with the rational numbers (i.e., the numbers of the form $\mathrm{m} / \mathrm{n}$ where m and n are integers and $\mathrm{n} \neq 0$ ).

The rational number system is inadequate for many purposes, both as a field and as an ordered set. (These terms will be defined in Definitions 1.6 and 1.12.) For instance, there is no rational p such that $\mathrm{p}^{2}=2$. (We shall prove this presently.) This leads to the introduction of so-called "irrational numbers" which are often written as infinite decimal expansions and are considered to be "approximated" by the corresponding finite decimals. Thus the sequence

$$
1,1.4,1.41,1.414,1.4142, \ldots
$$

"tends to $\sqrt{2}$." But unless the irrational number $\sqrt{2}$ has been clearly defined, the question must arise: Just what is it that this sequence "tends to"?

This sort of question can be answered as soon as the so-called "real number system" is constructed.
1.1 Example. We now show that the equation

$$
\mathrm{p}^{2}=2
$$

is not satisfied by any rational $p$. If there were such a $p$, we could write $p=m / n$ where $m$ and $n$ are integers that are not both even. Let us assume this is done.

Then (1.1) implies

$$
m^{2}=2 n^{2}
$$

This shows that $m^{2}$ is even. Hence $m$ is even (if $m$ were odd, $m^{2}$ would be odd), and so $m^{2}$ is divisible by 4 . It follows that the right side of (1.2) is divisible by 4 , so that $n^{2}$ is even, which implies that $n$ is even.

The assumption that (1.1) holds thus leads to the conclusion that both $m$ and $n$ are even, contrary to our choice of $m$ and $n$. Hence (1.1) is impossible for rational p.

We now examine this situation a little more closely. Let $A$ be the set of all positive rationals $p$ such that $p^{2}<2$ and let $B$ consist of all positive rationals $p$ such that $p^{2}>2$. We shall show that $A$ contains no largest number and $B$ contains no smallest.

More explicitly, for every $p$ in $A$ we can find a rational $q$ in $A$ such that $p<q$, and for every $p$ in $B$ we can find a rational $q$ in $B$ such that $q<p$.

To do this, we associate with each rational $p>0$ the number

$$
q=p-\frac{p^{2}-2}{p+2}=\frac{2 p+2}{p+2}
$$

Then

$$
q^{2}-2=\frac{2\left(p^{2}-2\right)}{(p+2)^{2}}
$$

If $p$ is in $A$, then $p^{2}-2<0,(1.3)$ shows that $q>p$ and (1.4) shows that $q^{2}<2$. Thus $q$ is in $A$.

If $p$ is in $B$, then $p^{2}-2>0,(1.3)$ shows that $0<q<p$, and (1.4) shows that $q^{2}>2$. Thus $q$ is in $B$.
1.2 Remark. The purpose of the above discussion has been to show that the rational number system has certain gaps, in spite of the fact that between any two rationals there is another: if $r<s$, then $r<(r+s) / 2<s$. The real number system fills these gaps. This is the principal reason for the fundamental role for which it plays in analysis.

In order to elucidate its structure, as well as that of the complex numbers, we start with a brief discussion of the general concepts of ordered set and field.

Here is some of the standard set-theoretic terminology that will be used throughout this book.
1.3 Definitions. If $A$ is any set (whose elements may be numbers or any other objects), we write $x \in A$ to indicate that $x$ is a member (or an element) of $A$. If $x$ is not a member of $A$, we write $x \notin A$.

The set which contains no element will be called the empty set. If a set has at least one element, it is called nonempty.

If $A$ and $B$ are sets, and if every element of $A$ is an element of $B$, we say that $A$ is a subset of $B$, and we write $A \subset B$, or $B \supset A$. If, in addition, there is an element of $B$ which is not in $A$, then $A$ is said to be a proper subset of $B$. Note that $A \subset A$ for every set $A$.

If $A \subset B$ and $B \subset A$, we write $A=B$. Otherwise, $A \neq B$.
1.4 Definition. Throughout Chap. 1, the set of all rational numbers will be denoted by $\mathbb{Q}$.

# ORDERED SETS 

1.5 Definition. Let $S$ be a set. An order on $S$ is a relation, denoted by $<$, with the following two properties
(i) If $x \in S$ and $y \in S$, then one and only one of the statements

$$
x<y, \quad x=y, \quad y<x
$$

is true.
(ii) If $x, y, z \in S$, if $x<y$ and $y<z$, then $x<z$.

The statement " $x<y$ " may be read as " $x$ is less than $y$ " or " $x$ is smaller than $y$ " or " $x$ precedes $y$ ".

It is often convenient to write $y>x$ in place of $x<y$.
The notation $x \leq y$ indicates that $x<y$ or $x=y$, without specifying which of these two is to hold. In other words, $x \leq y$ is the negation of $x>y$.
1.6 Definition. An ordered set is a set $S$ in which an order is defined.

For example, $\mathbb{Q}$ is an ordered set if $r<s$ is defined to mean that $s-r$ is a positive rational number.
1.7 Definition. Suppose $S$ is an ordered set, and $E \subset S$. If there exists a $\beta \in S$ such that $x \leq \beta$ for every $x \in E$, we say that $E$ is bounded above, and call $\beta$ an upper bound of E.

Lower bounds are defined the same way (with $\geq$ in place of $\leq$ ).
1.8 Definition. Suppose $S$ is an ordered set, $E \subset S$, and $E$ is bounded above. Suppose there exists an $\alpha \in S$ with the following properties:
(i) $\alpha$ is an upper bound of $E$.
(ii) If $\gamma<\alpha$ then $\gamma$ is not an upper bound of $E$.

Then $\alpha$ is called the least upper bound of $E$ [that there is at most one such $\alpha$ is clear from (ii)] or the supremum of E, and we write

$$
\alpha=\sup E
$$

The greatest lower bound, or infimum, of a set E which is bounded below is defined in the same manner: The statement

$$
\alpha=\inf \mathrm{E}
$$

means that $\alpha$ is a lower bound of $E$ and that no $\beta$ with $\beta>\alpha$ is a lower bound of E.

# 1.9 Examples. 

(a) Consider the sets A and B of Example 1.1 as subsets of the ordered set $\mathbb{Q}$. The set $A$ is bounded above. In fact, the upper bounds of $A$ are exactly the members of B. Since B contains no smallest member, A has no least upper bound in $\mathbb{Q}$.

Similarly, B is bounded below: the set of all lower bounds of B consists of $A$ and of all $r \in \mathbb{Q}$ with $r \leq 0$. Since $A$ has no largest member, $B$ has no greatest lower bound in $\mathbb{Q}$.
(b) If $\alpha=\sup E$ exists, then $\alpha$ may or may not be a member of $E$. For instance, let $E_{1}$ be the set of all $r \in \mathbb{Q}$ with $r<0$. Let $E_{2}$ be the set of all $r \in \mathbb{Q}$ with $r \leq 0$. Then

$$
\sup E_{1}=\sup E_{2}=0
$$

and $0 \notin E_{1}, 0 \in E_{2}$.
(c) Let E consist of all numbers $1 / n$, where $n=1,2,3, \ldots$ Then $\sup E=1$, which is in $E$, and $\inf E=0$, which is not in $E$.
1.10 Definition. An ordered set $S$ is said to have the least-upper-bound property if the following is true:

If $E \subset S, E$ is not empty, and $E$ is bounded above, then sup $E$ exists in $S$.
Example 1.9(a) shows that $\mathbb{Q}$ does not have the least-upper-bound property. We shall now show that there is a close relation between greatest lower bounds and least upper bounds, and that every ordered set with the least-upper-bound property also has the greatest-lower-bound property.
1.11 Theorem. Suppose $S$ is an ordered set with the least-upper-bound property, $B \subset S$, $B$ is not empty, and $B$ is bounded below. Let $L$ be the set of all lower bounds of $B$. Then

$$
\alpha=\sup \mathrm{L}
$$

exists in $S$ and $\alpha=\inf B$.
In particular, inf B exists in $S$.
Proof. Since B is bounded below, L is not empty. Since L consists of exactly those $y \in S$ which satisfy the inequality $y \leq x$ for every $x \in B$, we see that every $x \in B$ is an upper bound of L . Thus L is bounded above. Our hypothesis about S implies therefore that L has a supremum in S ; call it $\alpha$.

If $\gamma<\alpha$ then (see Definition 1.8) $\gamma$ is not an upper bound of $L$, hence $\gamma \notin B$. It follows that $\alpha \leq x$ for every $x \in B$. Thus $\alpha \in L$.

If $\alpha<\beta$ then $\beta \notin L$, since $\alpha$ is an upper bound of $L$.
We have shown that $\alpha \in L$ but $\beta \notin L$ if $\beta>\alpha$. In other words, $\alpha$ is a lower bound of $B$, but $\beta$ is not if $\beta>\alpha$. This means that $\alpha=\inf B$.

# FIELDS 

1.12 Definition. A field is a set $\mathbb{F}$ with two operations, called addition and multiplication, which satisfy the following so-called "field axioms" (A), (M), and (D):
(A) Axioms for addition
(A1) $x \in \mathbb{F}$ and $y \in \mathbb{F}$, then their sum $x+y$ is in $\mathbb{F}$.
(A2) Addition is commutative: $x+y=y+x$ for all $x, y \in \mathbb{F}$.
(A3) Addition is associative: $(x+y)+z=x+(y+z)$ for all $x, y, z \in \mathbb{F}$.
(A4) F contains an element 0 such that $0+x=x$ for every $x \in \mathbb{F}$.
(A5) To every $x \in \mathbb{F}$ corresponds an element $-x \in \mathbb{F}$ such that

$$
x+(-x)=0
$$

## (M) Axioms for multiplication

(M1) If $x \in \mathbb{F}$, then their product $x y$ is in $\mathbb{F}$.
(M2) Multiplication is commutative: $x y=y x$ for all $x, y \in \mathbb{F}$.
(M3) Multiplication is associative: $(x y) z=x(y z)$ for all $x, y, z \in \mathbb{F}$.
(M4) F contains an element $1 \neq 0$ such that $1 x=x$ for every $x \in \mathbb{F}$.
(M5) If $x \in \mathbb{F}$ and $x \neq 0$ then there exists an element $1 / x \in \mathbb{F}$ such that

$$
x \cdot(1 / x)=1
$$

## (D) The distributive law

$$
x(y+z)=x y+x z
$$

holds for all $x, y, z \in \mathbb{F}$.

### 1.13 Remarks.

(a) One usually writes (in any field)

$$
x-y, \frac{x}{y}, x+y+z, x y z, x^{2}, x^{3}, 2 x, 3 x, \ldots
$$

in place of

$$
x+(-y), x \cdot\left(\frac{1}{y}\right),(x+y)+z,(x y) z, x x, x x x, x+x, x+x+x, \ldots
$$

(b) The field axioms clearly hold in $\mathbb{Q}$, the set of all rational numbers, if addition and multiplication have their customary meaning. Thus $\mathbb{Q}$ is a field.
(c) Although it is not our purpose to study fields (or any other algebraic structures) in detail, it is worthwhile to prove that some of the familiar properties of $\mathbb{Q}$ are consequences of the field axioms; once we do this, we will not need to do it again for the real numbers and for the complex numbers.
1.14 Proposition. The axioms for addition imply the following statements.
(a) If $x+y=x+z$ then $y=z$.
(b) If $x+y=x$ then $y=0$.
(c) If $x+y=0$ then $y=-x$.
(d) $-(-x)=x$.

Statement (a) is a cancellation law. Note that (b) asserts the uniqueness of the element whose existence is assumed in (A4), and that (c) does the same for (A5).

Proof. If $x+y=x+z$, the axioms (A) give

$$
\begin{aligned}
y=0+y & =(-x+x)+y=-x+(x+y) \\
& =-x+(x+z)=(-x+x)+z=0+z=z
\end{aligned}
$$

This proves (a). Take $z=0$ in (a) to obtain (b). Take $z=-x$ in (a) to obtain (c). Since $-x+x=0$, (c) (with $-x$ in place of $x$ ) gives (d).
1.15 Proposition. The axioms for multiplication imply the following statements
(a) If $x \neq 0$ and $x y=x z$ then $y=z$.
(b) If $x \neq 0$ and $x y=x$ then $y=1$.
(c) If $x \neq 0$ and $x y=1$ then $y=1 / x$.
(d) If $x \neq 0$ then $1 /(1 / x)=x$.

The proof is so similar to that of Proposition 1.14 that we omit it.
1.16 Proposition. The field axioms imply the following statements, for any $x, y, z \in \mathbb{F}$.
(a) $0 x=0$.
(b) If $x \neq 0$ and $y \neq 0$ then $x y \neq 0$.
(c) $(-x) y=-(x y)=x(-y)$.
(d) $(-x)(-y)=x y$.

Proof. $0 x+0 x=(0+0) x=0 x$. Hence Proposition 1.14(b) implies that $0 x=0$, and (a) holds. Next, assume $x \neq 0, y \neq 0$, but $x y=0$. Then (a) gives

$$
1=\left(\frac{1}{y}\right)\left(\frac{1}{x}\right) x y=\left(\frac{1}{y}\right)\left(\frac{1}{x}\right) 0=0
$$

a contradiction. Thus (b) holds.

The first equality in (c) comes from

$$
(-x) y+x y=(-x+x) y=0 y=0
$$

combined with Proposition 1.14(c); the other half of (c) is proved in the same way.
Finally,

$$
(-x)(-y)=-[x(-y)]=-[-(x y)]=x y
$$

by (c) and Proposition 1.14(d).
1.17 Definition. An ordered field is a field $\mathbb{F}$ which is also an ordered set, such that
(i) $x+y<x+z$ if $x, y, z \in \mathbb{F}$ and $y<z$,
(ii) $x y>0$ if $x \in \mathbb{F}, y \in \mathbb{F}, x>0$, and $y>0$.

If $x>0$, we call $x$ positive; if $x<0, x$ is negative.
For example, $\mathbb{Q}$ is an ordered field.
All the familiar rules for working with inequalities apply in every ordered field: Multiplication by positive [negative] quantities preserves [reverses] inequalities, no square is negative, etc. The following proposition lists some of these.
1.18 Proposition. The following statements are true in every ordered field.
(a) If $x>0$ then $-x<0$, and vice versa.
(b) If $x>0$ and $y<z$ then $x y<x z$.
(c) If $x<0$ and $y<z$ then $x y>x z$.
(d) If $x \neq 0$ then $x^{2}>0$. In particular, $1>0$.
(e) If $0<x<y$ then $0<1 / y<1 / x$.

Proof.
(a) If $x>0$ then $0=-x+x>-x+0$, so that $-x<0$. If $x<0$ then $0=-x+x<$ $-x+0$, so that $-x>0$. This proves (a).
(b) Since $z>y$, we have $z-y>y-y=0$, hence $x(z-y)>0$, and therefore

$$
x z=x(z-y)+x y>0+x y=x y
$$

(c) By (a), (b), and Proposition 1.16(c),

$$
-[x(z-y)]=(-x)(z-y)>0
$$

so that $x(z-y)<0$, hence $x z<x y$.
(d) If $x>0$, part (ii) of Definition 1.17 gives $x^{2}>0$. If $x<0$, then $-x>0$, hence $(-x)^{2}>0$. But $x^{2}=(-x)^{2}$ by Proposition 1.16(d). Since $1=1^{2}, 1>0$.
(e) If $y>0$ and $v \leq 0$, then $y v \leq 0$. But $y \cdot(1 / y)=1>0$. Hence $1 / y>0$. Likewise, $1 / x>0$. If we multiply both sides of the inequality $x<y$ by the positive quantity $(1 / x)(1 / y)$, we obtain $1 / y<1 / x$.

# THE REAL FIELD 

We now state the existence theorem which is the core of this chapter.
1.19 Theorem. There exists an ordered field $\mathbb{R}$ which has the least-upper-bound property. Moreover, $\mathbb{R}$ contains $\mathbb{Q}$ as a subfield.

The second statement means that $\mathbb{Q} \subset \mathbb{R}$ and that the operations of addition and multiplication in $\mathbb{R}$, when applied to members of $\mathbb{Q}$, coincide with the usual operations on rational numbers; also, the positive rational numbers are positive elements of $\mathbb{R}$. The members of $\mathbb{R}$ are called real numbers.

The proof of Theorem 1.19 is rather long and a bit tedious and is therefore presented in an Appendix to Chap. 1. The proof actually constructs $\mathbb{R}$ from $\mathbb{Q}$.

The next theorem could be extracted from this construction with very little extra effort. However, we prefer to derive it from Theorem 1.19 since this provided a good illustration of what one can do with the least-upper-bound property.

### 1.20 Theorem.

(a) If $x \in \mathbb{R}, y \in \mathbb{R}$, and $x>0$, then there is a positive integer $n$ such that

$$
n x>y
$$

(b) If $x \in \mathbb{R}, y \in \mathbb{R}$, and $x<y$, then there exists a $p \in \mathbb{Q}$ such that $x<p<y$.

Part (a) is usually referred to as the archimedean property of $\mathbb{R}$. Part (b) may be stated by saying that $\mathbb{Q}$ is dense in $\mathbb{R}$ : Between any two real numbers, there is a rational one.

Proof.
(a) Let $A$ be the set of all $n x$, where $n$ runs through the positive integers. If (a) were false, then $y$ would be an upper bound of $A$. But then $A$ has a least upper bound in $\mathbb{R}$. Put $\alpha=\sup A$. Since $x>0, \alpha-x<\alpha$, and $\alpha-x$ is not an upper bound of $A$. Hence $\alpha-x<m x$ for some positive integer $m$. But then $\alpha<(m+1) x \in A$, which is impossible, since $\alpha$ is an upper bound of $A$.
(b) Since $x<y$, we have $y-x>0$, and (a) furnishes a positive integer $n$ such that

$$
n(y-x)>1
$$

Apply (a) again, to obtain positive integers $m_{1}$ and $m_{2}$ such that $m_{1}>n x$, $m_{2}>-n x$. Then

$$
-m_{2}<n x<m_{1}
$$

Hence there is an integer $m$ (with $-m_{2} \leq m \leq m_{1}$ ) such that

$$
m-1 \leq n x<m
$$

If we combine these inequalities, we obtain

$$
n x<m \leq 1+n x<n y
$$

Since $n>0$, it follows that

$$
x<\frac{m}{n}<y
$$

This proves (b), with $\mathrm{p}=\mathrm{m} / \mathrm{n}$.
We shall now prove the existence of nth roots of positive reals. This proof will show how the difficulty pointed out in the Introduction (irrationality of $\sqrt{2}$ ) can be handled in $\mathbb{R}$.
1.21 Theorem. For every real $x>0$ and every integer $n>0$, there is one and only one positive real $y$ such that $y^{n}=x$.

This number $y$ is written $\sqrt[n]{x}$ or $x^{1 / n}$.
Proof. That there is at most one such $y$ is clear, since $0<y_{1}<y_{2}$ implies $y_{1}^{n}<y_{2}^{n}$.
Let $E$ be the set consisting of all positive real numbers $t$ such that $t^{n}<x$. If $t=x /(1+x)$ then $0 \leq t<1$. Hence $t^{n} \leq t<x$. Thus $t \in E$, and $E$ is not empty.

If $t>1+x$ then $t^{n} \geq t>x$ so that $t \notin E$. Thus $1+x$ is an upper bound of $E$. Hence Theorem 1.19 implies the existence of

$$
y=\sup E
$$

To prove that $y^{n}=x$ we will show that each of the inequalities $y^{n}<x$ and $y^{n}>x$ leads to a contradiction.

The identity $b^{n}-a^{n}=(b-a)\left(b^{n-1}+b^{n-2} a+\cdots+a^{n-1}\right)$ yields the inequality

$$
b^{n}-a^{n}<(b-a) n b^{n-1}
$$

when $0<a<b$.
Assume $y^{n}<x$. Choose $h$ so that $0<h<1$ and

$$
h<\frac{x-y^{n}}{n(y+1)^{n-1}}
$$

Put $a=y, b=y+h$. Then

$$
(y+h)^{n}-y^{n}<h n(y+h)^{n-1}<h n(y+1)^{n-1}<x-y^{n}
$$

Thus $(y+h)^{n}<x$ and $y+h \in E$. Since $y+h>y$, this contradicts the fact that $y$ is an upper bound of $E$.

Assume $y^{n}>x$. Put

$$
k=\frac{y^{n}-x}{n y^{n-1}}
$$

Then $0<k<y$. If $t \geq y-k$, we conclude that

$$
y^{n}-t^{n} \leq y^{n}-(y-k)^{n}<k n y^{n-1}=y^{n}-x
$$

Thus $t^{n}>x$ and $t \notin E$. It follows that $y-k$ is an upper bound of $E$. But $y-k<y$, which contradicts the fact that $y$ is the least upper bound of $E$.

Hence $y^{n}=x$, and the proof is complete.
Corollary. If $a$ and $b$ are positive real numbers and $n$ is a positive integer, then

$$
(a b)^{1 / n}=a^{1 / n} b^{1 / n}
$$

Proof. Put $\alpha=a^{1 / n}, \beta=b^{1 / n}$. Then

$$
a b=\alpha^{n} \beta^{n}=(\alpha \beta)^{n}
$$

since multiplication is commutative. [Axiom (M2) in Definition 1.12.] The uniqueness assertion of Theorem 1.21 shows therefore that

$$
(a b)^{1 / n}=\alpha \beta=a^{1 / n} b^{1 / n}
$$

1.22 Decimals. We conclude this section by pointing out the relation between real numbers and decimals.

Let $x>0$ be real. Let $n_{0}$ be the largest integer such that $n_{0} \leq x$. (Note that the existence of $n_{0}$ depends on the archimedean property of $\mathbb{R}$.) Having chosen $n_{0}, n_{1}, \ldots, n_{k-1}$, let $n_{k}$ denote the largest integer such that

$$
n_{0}+\frac{n_{1}}{10}+\cdots+\frac{n_{k}}{10^{k}} \leq x
$$

Let $E$ be the set of these numbers

$$
n_{0}+\frac{n_{1}}{10}+\cdots+\frac{n_{k}}{10^{k}} \quad(k=0,1,2, \ldots)
$$

Then $x=\sup E$. The decimal expansion of $x$ is

$$
n_{0} \cdot n_{1} n_{2} n_{3} \cdots
$$

Conversely, for any infinite decimal expansion (1.6) the set E of numbers (1.5) is bounded above and (1.6) is the decimal expansion of sup E.

Since we shall never use decimals, we do not enter into a detailed discussion.

# THE EXTENDED REAL NUMBER SYSTEM 

1.23 Definition. The extended real number system consists of the real field $\mathbb{R}$ and two symbols, $+\infty$ and $-\infty$. We preserve the original order in $\mathbb{R}$ and define

$$
-\infty<x<+\infty
$$

for every $x \in \mathbb{R}$.
It is then clear that $+\infty$ is an upper bound of every subset of the extended real number system, and that every nonempty subset has a least upper bound. If, for example, E is a nonempty subset of real numbers which is not bounded above in $\mathbb{R}$, then $\sup \mathrm{E}=+\infty$ in the extended real number system.

Exactly the same remarks apply to lower bounds.
The extended real number system does not form a field, but it is customary to make the following conventions:
(a) If $x$ is real then

$$
x+\infty=+\infty, \quad x-\infty=-\infty, \quad \frac{x}{+\infty}=\frac{x}{-\infty}=0
$$

(b) If $x>0$ then $x \cdot(+\infty)=+\infty, x \cdot(-\infty)=-\infty$.
(c) If $x<0$ then $x \cdot(+\infty)=-\infty, x \cdot(-\infty)=+\infty$.

When it is desired to make the distinction between real numbers on the one hand and the symbols $+\infty$ and $-\infty$ on the other quite explicit, the former are called finite.

# THE COMPLEX FIELD 

1.24 Definition. A complex number is an ordered pair ( $a, b$ ) of real numbers. "Ordered" means that $(a, b)$ and $(b, a)$ are regarded as distinct if $a \neq b$.

Let $x=(a, b), y=(c, d)$ be two complex numbers. We write $x=y$ if and only if $a=c$ and $b=d$. (Note that this definition is not entirely superfluous; think of equality of rational numbers, represented as quotients of integers.) We define

$$
\begin{aligned}
x+y & =(a+c, b+d) \\
x y & =(a c-b d, a d+b c)
\end{aligned}
$$

1.25 Theorem. These definitions of addition and multiplication turn the set of all complex numbers into a field, which $(0,0)$ and $(1,0)$ in the role of 0 and 1.

Proof. We simply verify the field axioms, as listed in Definition 1.12. (Of course, we use the field structure of $\mathbb{R}$.) Let $x=(a, b), y=(c, d), z=(e, f)$.
(A1) is clear.
(A2) $x+y=(a+c, b+d)=(c+a, d+b)=y+x$.
(A3) $(x+y)+z=(a+c, b+d)+(e, f)$

$$
\begin{aligned}
& =(a+c+e, b+d+f) \\
& =(a, b)+(c+e, d+f)=x+(y+z)
\end{aligned}
$$

(A4) $x+0=(a, b)+(0,0)=(a, b)=x$.
(A5) Put $-x=(-a,-b)$. Then $x+(-x)=(0,0)=0$.

(M1) is clear.
(M2) $x y=(a c-b d, a d+b c)=(c a-d b, d a+c b)=y x$.
(M3) $(x y) z=(a c-b d, a d+b c)(e, f)$

$$
\begin{aligned}
& =(a c e-b d e-a d f-b c f, a c f-b d f+a d e+b c e) \\
& =(a, b)(c e-d f, c f+d e)=x(y z)
\end{aligned}
$$

(M4) $1 x=(1,0)(a, b)=(a, b)=x$.
(M5) If $x \neq 0$ then $(a, b) \neq(0,0)$, which means that at least one of the real numbers $a, b$ is different from 0 . Hence $a^{2}+b^{2}>0$, by Proposition 1.18(d), and we can define

$$
\frac{1}{x}=\left(\frac{a}{a^{2}+b^{2}}, \frac{-b}{a^{2}+b^{2}}\right)
$$

Then

$$
x \cdot \frac{1}{x}=(a, b)\left(\frac{a}{a^{2}+b^{2}}, \frac{-b}{a^{2}+b^{2}}\right)=(1,0)=1
$$

(D) $x(y+z)=(a, b)(c+e, d+f)$

$$
\begin{aligned}
& =(a c+a e-b d-b f, a d+a f+b c+b e) \\
& =(a c-b d, a d+b c)+(a e-b f, a f+b e) \\
& =x y+x z
\end{aligned}
$$

1.26 Theorem. For any real numbers $a$ and $b$ we have

$$
(a, 0)+(b, 0)=(a+b, 0), \quad(a, 0)(b, 0)=(a b, 0)
$$

The proof is trivial.
Theorem 1.26 shows that the complex numbers of the form $(a, 0)$ have the same arithmetic properties as the corresponding real numbers $a$. We can therefore identify $(a, 0)$ with $a$. This identification gives us the real field as a subfield of the complex field.

The reader may have noticed that we defined the complex numbers without any reference to the mysterious square root of -1 . We now show that the notation $(a, b)$ is equivalent to the more customary $a+b i$.
1.27 Definition. $i=(0,1)$.
1.28 Theorem. $i^{2}=-1$.

Proof. $i^{2}=(0,1)(0,1)=(-1,0)=-1$.
1.29 Theorem. If $a$ and $b$ are real, then $(a, b)=a+b i$.

Proof.

$$
\begin{aligned}
a+b i & =(a, 0)+(b, 0)(0,1) \\
& =(a, 0)+(0, b)=(a, b)
\end{aligned}
$$

1.30 Definition. If $a, b$ are real and $z=a+b i$, then the complex number $\bar{z}=a-b i$ is called the conjugate of $z$. The numbers $a$ and $b$ are the real part and the imaginary part of $z$, respectively.

We shall occasionally write

$$
a=\operatorname{Re}(z), \quad b=\operatorname{Im}(z)
$$

1.31 Theorem. If $z$ and $w$ are complex, then
(a) $\overline{z+w}=\bar{z}+\bar{w}$,
(b) $\overline{z w}=\bar{z} \cdot \bar{w}$,
(c) $z+\bar{z}=2 \operatorname{Re}(z), z-\bar{z}=2 i \operatorname{Im}(z)$,
(d) $z \bar{z}$ is real and positive (except when $z=0$ ).

Proof. (a), (b), and (c) are quite trivial. To prove (d), write $z=a+b i$, and note that $z \bar{z}=a^{2}+b^{2}$
1.32 Definition. If $z$ is a complex number, its absolute value $|z|$ is the non-negative square root of $z \bar{z}$; that is $|z|=(z \bar{z})^{1 / 2}$.

The existence (and uniqueness) of $|z|$ follows from Theorem 1.21 and part (d) of Theorem 1.31.

Note that when $x$ is real, then $\bar{x}=x$, hence $|x|=\sqrt{x^{2}}$. Thus $|x|=x$ if $x \geq 0$, $|x|=-x$ if $x<0$.
1.33 Theorem. Let $z$ and $w$ be complex numbers. Then
(a) $|z|>0$ unless $z=0,|0|=0$,
(b) $|\bar{z}|=|z|$,
(c) $|z w|=|z||w|$,
(d) $|\operatorname{Re}(z)| \leq|z|$,
(e) $|z+w| \leq|z|+|w|$.

Proof. (a) and (b) are trivial. Put $z=a+b i, w=c+d i$, with $a, b, c, d$ real. Then

$$
|z w|^{2}=(a c-b d)^{2}+(a d+b c)^{2}=\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right)=|z|^{2}|w|^{2}
$$

or $|z w|^{2}=(|z||w|)^{2}$. Now (c) follows from the uniqueness assertion of Theorem 1.21 .

To prove (d), note that $a^{2} \leq a^{2}+b^{2}$, hence

$$
|a|=\sqrt{a^{2}} \leq \sqrt{a^{2}+b^{2}}
$$

To prove (e), note that $\bar{z} w$ is the conjugate of $z \bar{w}$, so that $z \bar{w}+\bar{z} w=2 \operatorname{Re}(z \bar{w})$. Hence

$$
\begin{aligned}
|z+w|^{2} & =(z+w)(\bar{z}+\bar{w})=z \bar{z}+z \bar{w}+\bar{z} w+w \bar{w} \\
& =|z|^{2}+2 \operatorname{Re}(z \bar{w})+|w|^{2} \\
& \leq|z|^{2}+2|z \bar{w}|+|w|^{2} \\
& =|z|^{2}+2|z||w|+|w|^{2}=(|z|+|w|)^{2}
\end{aligned}
$$

Now (e) follows by taking square roots.
1.34 Notation. If $x_{1}, \ldots, x_{n}$ are complex numbers, we write

$$
x_{1}+x_{2}+\cdots+x_{n}=\sum_{j=1}^{n} x_{j}
$$

We conclude this section with an important inequality, usually known as the Schwarz inequality.
1.35 Theorem. If $a_{1}, \ldots, a_{n}$ and $b_{1}, \ldots, b_{n}$ are complex numbers, then

$$
\left|\sum_{j=1}^{n} a_{j} \bar{b}_{j}\right|^{2} \leq \sum_{j=1}^{n}\left|a_{j}\right|^{2} \sum_{j=1}^{n}\left|b_{j}\right|^{2}
$$

Proof. Put $A=\Sigma\left|a_{j}\right|^{2}, B=\Sigma\left|b_{j}\right|^{2}, C=\Sigma a_{j} \bar{b}_{j}$ (in all sums in this proof, $j$ runs over the values $1, \ldots, n$ ). If $B=0$, then $b_{1}=\cdots=b_{n}=0$, and the conclusion is trivial. Assume therefore that $\mathrm{B}>0$. By Theorem 1.31 we have

$$
\begin{aligned}
\sum\left|B a_{j}-C b_{j}\right|^{2} & =\sum\left(B a_{j}-C b_{j}\right)\left(B \bar{a}_{j}-\overline{C b_{j}}\right) \\
& =B^{2} \sum\left|a_{j}\right|^{2}-B \bar{C} \sum a_{j} \bar{b}_{j}-B C \sum \bar{a}_{j} b_{j}+|C|^{2} \sum\left|b_{j}\right|^{2} \\
& =B^{2} A-B|C|^{2} \\
& =B\left(A B-|C|^{2}\right)
\end{aligned}
$$

Since each term in the first sum is nonnegative, we see that

$$
B(A B-|C|)^{2} \geq 0
$$

Since $B>0$, it follows that $A B-|C|^{2} \geq 0$. This is the desired inequality.

# EUCLIDEAN SPACES 

1.36 Definitions. For each positive integer k , let $\mathbb{R}^{\mathrm{k}}$ be the set of all ordered ktuples

$$
\mathbf{x}=\left(x_{1}, x_{2}, \ldots, x_{k}\right)
$$

where $x_{1}, \ldots, x_{k}$ are real numbers, called the coordinates of $\mathbf{x}$. The elements of $\mathbb{R}^{k}$ are called points, or vectors, especially when $\mathrm{k}>1$. We shall denote vectors by boldfaced letters. If $\mathbf{y}=\left(y_{1}, \ldots, y_{k}\right)$ and if $\alpha$ is a real number, put

$$
\begin{aligned}
\mathbf{x}+\mathbf{y} & =\left(\mathrm{x}_{1}+\mathrm{y}_{1}, \ldots, \mathrm{x}_{\mathrm{k}}+\mathrm{y}_{\mathrm{k}}\right) \\
\alpha \mathbf{x} & =\left(\alpha \mathrm{x}_{1}, \ldots, \alpha \mathrm{x}_{\mathrm{n}}\right)
\end{aligned}
$$

so that $\mathbf{x}+\mathbf{y} \in \mathbb{R}^{\mathrm{k}}$ and $\alpha \mathbf{x} \in \mathbb{R}^{\mathrm{k}}$. This defines addition of vectors, as well as multiplication of a vector by a real number (a scalar). These two operations satisfy the commutative, associative, and distributive laws (the proof is trivial, in view of the analogous laws for the real numbers) and make $\mathbb{R}^{\mathrm{k}}$ into a vector space over the real field. The zero element of $\mathbb{R}^{\mathrm{k}}$ (sometimes called the origin or the null vector) is the point 0 , all of whose coordinates are 0 .

We also define the so-called "inner product" (or scalar product) of $\mathbf{x}$ and $\mathbf{y}$ by

$$
\mathbf{x} \cdot \mathbf{y}=\sum_{i=1}^{k} x_{i} y_{i}
$$

and the norm of $\mathbf{x}$ by

$$
|\mathbf{x}|=(\mathbf{x} \cdot \mathbf{x})^{1 / 2}=\left(\sum_{i=1}^{k} x_{i}^{2}\right)^{1 / 2}
$$

The structure now defined (the vector space $\mathbb{R}^{\mathrm{k}}$ with the above inner product and norm is called euclidean k-space.
1.37 Theorem. Suppose $\mathbf{x}, \mathbf{y}, \mathbf{z} \in \mathbb{R}^{\mathrm{k}}$, and $\alpha$ is real. Then
(a) $|\mathbf{x}| \geq 0$;
(b) $|\mathbf{x}|=0$ if and only if $\mathbf{x}=\mathbf{0}$;
(c) $|\alpha \mathbf{x}|=|\alpha||\mathbf{x}| ;$
(d) $|\mathbf{x} \cdot \mathbf{y}| \leq|\mathbf{x}||\mathbf{y}| ;$
(e) $|\mathbf{x}+\mathbf{y}| \leq|\mathbf{x}|+|\mathbf{y}|$
(f) $|\mathbf{x}-\mathbf{z}| \leq|\mathbf{x}-\mathbf{y}|+|\mathbf{y}-\mathbf{z}|$.

Proof. (a), (b), and (c) are obvious, and (d) is an immediate consequence of the Schwarz inequality. By (d) we have

$$
\begin{aligned}
|\mathbf{x}+\mathbf{y}|^{2} & =(\mathbf{x}+\mathbf{y}) \cdot(\mathbf{x}+\mathbf{y}) \\
& =\mathbf{x} \cdot \mathbf{x}+2 \mathbf{x} \cdot \mathbf{y}+\mathbf{y} \cdot \mathbf{y} \\
& \leq|\mathbf{x}|^{2}+2|\mathbf{x}||\mathbf{y}|+|\mathbf{y}|^{2} \\
& =(|\mathbf{x}|+|\mathbf{y}|)^{2}
\end{aligned}
$$

so that (e) is proved. Finally (f) follows from (e) if we replace $\mathbf{x}$ by $\mathbf{x}-\mathbf{y}$ and $\mathbf{y}$ by $\mathbf{y}-\mathbf{z}$.

1.38 Remarks. Theorem 1.37(a), (b), and (f) will allow us (see Chap. 2) to regard $\mathbb{R}^{\mathrm{k}}$ as a metric space.
$\mathbb{R}^{1}$ (the set of all real numbers) is usually called the line, or the real line. Likewise, $\mathbb{R}^{2}$ is called the plane, or the complex plane (compare Definitions 1.24 and 1.36). In these two cases, the norm is just the absolute value of the corresponding real or complex number.

# APPENDIX 

Theorem 1.19 will be proved in this appendix by constructing $\mathbb{R}$ from $\mathbb{Q}$. We shall divide the construction into several steps.
Step 1 The members of $\mathbb{R}$ will be certain subsets of $\mathbb{Q}$, called cuts. A cut is, by definition, any set $\alpha \subseteq \mathbb{Q}$ with the following three properties.
(I) $\alpha$ is not empty, and $\alpha \neq \mathbb{Q}$.
(II) If $p \in \alpha, q \in \mathbb{Q}$, and $q<p$, then $q \in \alpha$.
(III) If $p \in \alpha$, then $p<r$ for some $r \in \alpha$.

The letters $\mathrm{p}, \mathrm{q}, \mathrm{r}, \ldots$ will always denote rational numbers, and $\alpha, \beta, \gamma, \ldots$ will denote cuts.

Note that (III) simply says that $\alpha$ has no largest member; (II) implies two facts which will be used freely:

If $p \in \alpha$ and $q \notin \alpha$, then $p<q$.
If $r \notin \alpha$ and $r<s$, then $s \notin \alpha$.
Step 2 Define " $\alpha<\beta$ " to mean: $\alpha$ is a proper subset of $\beta$.
Let us check that this meets the requirements of Definition 1.5.
If $\alpha<\beta$ and $\beta<\gamma$ it is clear that $\alpha<\gamma$. (A proper subset of a proper subset is a proper subset.) It is also clear that at most one of the three relations

$$
\alpha<\beta, \quad \alpha=\beta, \quad \beta<\alpha
$$

can hold for any pair $\alpha, \beta$. To show that at least one holds, assume that the first two fail. Then $\alpha$ is not a subset of $\beta$. Hence there is a $p \in \alpha$ with $p \notin \beta$. If $q \in \beta$, it follows that $q<p$ (since $p \notin \beta$ ), hence $q \in \alpha$, by (II). Thus $\beta \subset \alpha$. Since $\beta \neq \alpha$, we conclude $\beta<\alpha$.

Thus $\mathbb{R}$ is now an ordered set.
Step 3 The ordered set $\mathbb{R}$ has the least upper bound property.
To prove this, let $A$ be a nonempty subset of $\mathbb{R}$, and assume that $\beta \in \mathbb{R}$ is an upper bound of $A$. Define $\gamma$ to be the union of all $\alpha \in A$. In other words, $\mathrm{p} \in \gamma$ if and only if $\mathrm{p} \in \alpha$ for some $\alpha \in \mathrm{A}$. We shall prove that $\gamma \in \mathbb{R}$ and that $\gamma=\sup A$.

Since $A$ is not empty, there exists an $\alpha_{0} \in A$. This $\alpha_{0}$ is not empty. Since $\alpha_{0} \subset \gamma, \gamma$ is not empty. Next, $\gamma \subset \beta$ (since $\alpha \subset \beta$ for every $\alpha \in A$ ), and therefore $\gamma \neq \mathbb{Q}$. Thus $\gamma$ satisfies property (I). To prove (II) and (III), pick $p \in \gamma$. Then $p \in \alpha_{1}$

for some $\alpha_{1} \in \mathrm{~A}$. If $\mathrm{q}<\mathrm{p}$, then $\mathrm{q} \in \alpha_{1}$, hence $\mathrm{q} \in \gamma$; this proves (II). If $\mathrm{r} \in \alpha_{1}$ is so chosen that $r>p$, we see that $r \in \gamma$ (since $\alpha_{1} \subset \gamma$ ), and therefore $\gamma$ satisfies (III).

Thus $\gamma \in \mathbb{R}$.
It is clear that $\alpha \leq \gamma$ for every $\alpha \in \mathrm{A}$.
Suppose $\delta<\gamma$. Then there is an $s \in \gamma$ such that $s \notin \delta$. Since $s \in \gamma, s \in \alpha$ for some $\alpha \in \mathrm{A}$. Hence $\delta<\alpha$ and $\delta$ is not an upper bound of A .

This gives the desired result: $\gamma=\sup \mathrm{A}$.
Step 4 If $\alpha \in \mathbb{R}$ and $\beta \in \mathbb{R}$, we define $\alpha+\beta$ to be the set of all sums $r+s$, where $r \in \alpha$ and $s \in \beta$.

We define $0^{*}$ to be the set of all negative rational numbers. It is clear that $0^{*}$ is a cut. We verify that the axioms for addition (see Definition 1.12) hold in $\mathbb{R}$, with $0^{*}$ playing the role of 0 .
(A1) We have to show that $\alpha+\beta$ is a cut. It is clear that $\alpha+\beta$ is a nonempty subset of $\mathbb{Q}$. Take $r^{\prime} \notin \alpha, s^{\prime} \notin \beta$. Then $r^{\prime}+s^{\prime}>r+s$ for all choices of $r \in \alpha, s \in \beta$. Thus $r^{\prime}+s^{\prime} \notin \alpha+\beta$. It follows that $\alpha+\beta$ has property (I).

Pick $p \in \alpha+\beta$. Then $p=r+s$, with $r \in \alpha, s \in \beta$. If $q<p$, then $q-s<r$, so $\mathrm{q}-\mathrm{s} \in \alpha$, and $\mathrm{q}=(\mathrm{q}-\mathrm{s})+\mathrm{s} \in \alpha+\beta$. Thus (II) holds. Choose $\mathrm{t} \in \alpha$ so that $\mathrm{t}>\mathrm{r}$. Then $\mathrm{p}<\mathrm{t}+\mathrm{s}$ and $\mathrm{t}+\mathrm{s} \in \alpha+\beta$. Thus (III) holds.
(A2) $\alpha+\beta$ is the set of all $r+s$, with $r \in \alpha, s \in \beta$. By the same definition, $\beta+\alpha$ is the set of all $s+r$. Since $r+s=s+r$ for all $r \in \mathbb{Q}, s \in \mathbb{Q}$, we have $\alpha+\beta=\beta+\alpha$.
(A3) As above, this follows from the associative law in $\mathbb{Q}$.
(A4) If $r \in \alpha$ and $s \in 0^{*}$, then $r+s<r$, hence $r+s \in \alpha$. Thus $\alpha+0^{*} \subset \alpha$. To obtain the opposite inclusion, pick $p \in \alpha$, and pick $r \in \alpha, r>p$. Then $\mathrm{p}-\mathrm{r} \in 0^{*}$, and $\mathrm{p}=\mathrm{r}+(\mathrm{p}-\mathrm{r}) \in \alpha+0^{*}$. This $\alpha \subset \alpha+0^{*}$. We conclude that $\alpha+0^{*}=\alpha$.
(A5) Fix $\alpha \in \mathbb{R}$. Let $\beta$ be the set of all $p$ with the following property:

There exists $r>0$ such that $-p-r \notin \alpha$
In other words, some rational number smaller than $-p$ fails to be in $\alpha$. We show that $\beta \in \mathbb{R}$ and that $\alpha+\beta=0^{*}$.

If $s \notin \alpha$ and $p=-s-1$, then $-p-1 \notin \alpha$, hence $p \in \beta$. So $\beta$ is not empty. If $q \in \alpha$, then $-q \notin \beta$. So $\beta \neq Q$. Hence $\beta$ satisfies (I).

Pick $p \in \beta$ and $r>0$ so that $-p-r \notin \alpha$. If $q<p$, then $-q-r>-p-r$, hence $-q-r \notin \alpha$. Thus $q \in \beta$ and (II) holds. Put $t=p+(r / 2)$. Then $t>p$ and $-\mathrm{t}-(\mathrm{r} / 2)=-\mathrm{p}-\mathrm{r} \notin \alpha$, so that $\mathrm{t} \in \beta$. Hence $\beta$ satisfies (III).

We have proved that $\beta \in \mathbb{R}$.
If $r \in \alpha$ and $s \in \beta$, then $-s \notin \alpha$, hence $r<-s, r+s<0$. Thus $\alpha+\beta \subset 0^{*}$.
To prove the opposite inclusion, pick $v \in 0^{*}$, put $w=-v / 2$. Then $w>0$ and there is an integer $n$ such that $n w \in \alpha$ but $(n+1) w \notin \alpha$. (Note that this depends on the fact that $\mathbb{Q}$ has the archimedean property!) Put $\mathrm{p}=$ $-(n+2) w$. Then $p \in \beta$, since $-p-w \notin \alpha$ and

$$
v=n w+p \in \alpha+\beta
$$

Thus $0^{*} \subset \alpha+\beta$.
We conclude that $\alpha+\beta=0^{*}$. This $\beta$ will of course be denoted by $-\alpha$.
Step 5 Having proved that the addition defined in Step 4 satisfies axioms (A) of Definition 1.12, it follows that Proposition 1.14 is valid in $\mathbb{R}$, and we can prove one of the requirements in Definition 1.17:

If $\alpha, \beta, \gamma \in \mathbb{R}$ and $\beta<\gamma$, then $\alpha+\beta<\alpha+\gamma$.
Indeed, it is obvious from the definition of + in $\mathbb{R}$ that $\alpha+\beta \subset \alpha+\gamma$; if we had $\alpha+\beta=\alpha+\gamma$, the cancellation law (Proposition 1.14) would imply $\beta=\gamma$.

It also follows that $\alpha>0^{*}$ if and only if $-\alpha<0^{*}$.
Step 6 Multiplication is a little more bothersome than addition in the present context, since products of negative rationals are positive. For this reason we confine ourselves first to $\mathbb{R}^{+}$the set of all $\alpha \in \mathbb{R}$ with $\alpha>0^{*}$.

If $\alpha \in \mathbb{R}^{+}$and $\beta \in \mathbb{R}^{+}$, we define $\alpha \beta$ to be the set of all $\mathrm{p} \leq \mathrm{rs}$ for some choice of $r \in \alpha, s \in \beta, r>0, s>0$.

We define $1^{*}$ to be the set of all $\mathrm{q}<1$.
Then the axioms (M) and (D) of Definition 1.12 hold, with $\mathbb{R}^{+}$in place of $\mathbb{E}$, and with $1^{*}$ in the role of 1 .

The proofs are so similar to the ones given in detail in Step 4 that we omit them.

Note, in particular, that the second requirement of Definition 1.17 holds: If $\alpha>0^{*}$ and $\beta>0^{*}$, then $\alpha \beta>0^{*}$.
Step 7 We complete the definition of multiplication by setting $\alpha 0^{*}=0^{*} \alpha=0^{*}$, and by setting

$$
\alpha \beta= \begin{cases}(-\alpha)(-\beta) & \text { if } \alpha<0^{*}, \beta<0^{*}, \\ -[(-\alpha) \beta] & \text { if } \alpha<0^{*}, \beta>0^{*}, \\ -[\alpha(-\beta)] & \text { if } \alpha>0^{*}, \beta<0^{*}\end{cases}
$$

The products on the right were defined in Step 6.
Having proved (in Step 6) that the axioms (M) hold in $\mathbb{R}^{+}$, it is now perfectly simple to prove them in $\mathbb{R}$, by repeated application of the identity $\gamma=-(-\gamma)$ which is part of Proposition 1.14. (See Step 5.)

The proof of the distributive law

$$
\alpha(\beta+\gamma)=\alpha \beta+\alpha \gamma
$$

breaks into cases. For instance, suppose $\alpha>0^{*}, \beta<0^{*}, \beta+\gamma>0^{*}$. Then $\gamma=$ $(\beta+\gamma)+(-\beta)$, and (since we already know that the distributive law holds in $\mathbb{R}^{+}$)

$$
\alpha \gamma=\alpha(\beta+\gamma)+\alpha \cdot(-\beta)
$$

but $\alpha \cdot(-\beta)=-(\alpha \beta)$. Thus

$$
\alpha \beta+\alpha \gamma=\alpha(\beta+\gamma)
$$

The other cases are handled in the same way.
We have now completed the proof that $\mathbb{R}$ is an ordered field with the least upper bound property.
Step 8 We associate with each $r \in \mathbb{Q}$ the set $r^{*}$ which consists of all $p \in \mathbb{Q}$ such that $\mathrm{p}<\mathrm{r}$. It is clear that each $\mathrm{r}^{*}$ is a cut; that is, $\mathrm{r}^{*} \in \mathbb{R}$. These cuts satisfy the following relations:
(a) $r^{*}+s^{*}=(r+s)^{*}$
(b) $r^{*} s^{*}=(r s)^{*}$,
(c) $r^{*}<\mathrm{s}^{*}$ if and only if $\mathrm{r}<\mathrm{s}$.

To prove (a), choose $p \in r^{*}+s^{*}$. Then $p=u+v$, where $u<r, v<s$. Hence $\mathrm{p}<\mathrm{r}+\mathrm{s}$, which says that $\mathrm{p} \in(\mathrm{r}+\mathrm{s})^{*}$.

Conversely, suppose $\mathrm{p} \in(\mathrm{r}+\mathrm{s})^{*}$. Then $\mathrm{p}<\mathrm{r}+\mathrm{s}$. Choose t so that $2 \mathrm{t}=$ $r+s-p$, put

$$
r^{\prime}=r-t, \quad s^{\prime}=s-t
$$

Then $r^{\prime} \in r^{*}, s^{\prime} \in s^{*}$, and $p=r^{\prime}+s^{\prime}$, so that $p \in r^{*}+s^{*}$. This proves (a). The proof of (b) is similar.

If $r<s$ then $r \in s^{*}$, but $r \notin r^{*}$; hence $r^{*}<\mathrm{s}^{*}$.
If $r^{*}<\mathrm{s}^{*}$, then there is a $\mathrm{p} \in \mathrm{s}^{*}$ such that $\mathrm{p} \notin \mathrm{r}^{*}$. Hence $\mathrm{r} \leq \mathrm{p}<\mathrm{s}$, so that $r<s$. This proves (c).
Step 9 We saw in Step 8 that the replacement of the rational numbers $r$ by the corresponding "rational cuts" $r^{*} \in \mathbb{R}$ preserves sums, products, and order. This fact may be expressed by saying that the ordered field $\mathbb{Q}$ is isomorphic to the ordered field $\mathbb{Q}^{*}$ whose elements are the rational cuts. Of course, $r^{*}$ is by no means the same as $r$, but the properties we are concerned with (arithmetic and order) are the same in the two fields.

It is this identification of $\mathbb{Q}$ with $\mathbb{Q}^{*}$ which allows us to regard $\mathbb{Q}$ as a subfield of $\mathbb{R}$.
The second part of Theorem 1.19 is to be understood in terms of this identification. Note that the same phenomenon occurs when the real numbers are regarded as a subfield of the complex field, and it also occurs at a much more elementary level, when the integers are identified with a certain subset of $\mathbb{Q}$.

It is a fact, which we will not prove here, that any two ordered fields with the least-upper-bound property are isomorphic. The first part of Theorem 1.19 therefore characterizes the real field $\mathbb{R}$ completely.

The books by Landau [Lan51] and Thurston [Thu56] cited in the Bibliography are entirely devoted to number systems. Chapter 1 of Knopp's book [Kno28] contains a more leisurely description of how $\mathbb{R}$ can be obtained from $\mathbb{Q}$. Another construction, in which each real number is defined to be an equivalence class of

Cauchy sequences of rational numbers (see Chap. 3), is carried out in Sec. 5 of the book by Hewitt and Stromberg [HS65].

The cuts in $\mathbb{Q}$ which we used here were invented by Dedekind. The construction of $\mathbb{R}$ from $\mathbb{Q}$ by means of Cauchy sequences is due to Cantor. Both Cantor and Dedekind published their constructions in 1872.

# EXERCISES 

Unless the contrary is explicitly stated, all numbers that are mentioned in these exercises are understood to be real.
1.1. If $r$ is rational $(r \neq 0)$ and $x$ is irrational, prove that $r+x$ and $r x$ are irrational.
1.2. Prove that there is no rational number whose square is 12 .
1.3. Prove Proposition 1.15 .
1.4. Let $E$ be a nonempty subset of an ordered set; suppose $\alpha$ is a lower bound of $E$ and $\beta$ is an upper bound of $E$. Prove that $\alpha \leq \beta$.
1.5. Let $A$ be a nonempty set of real numbers which is bounded below. Let $-A$ be the set of all numbers $-x$, where $x \in A$. Prove that

$$
\inf A=-\sup (-A)
$$

1.6. Fix $b>1$.
(a) If $m, n, p, q$ are integers, $n>0, q>0$, and $r=m / n=p / q$, prove that

$$
\left(b^{m}\right)^{1 / n}=\left(b^{p}\right)^{1 / q}
$$

Hence it makes sense to define $b^{r}=\left(b^{m}\right)^{1 / n}$.
(b) Prove that $b^{r+s}=b^{r} b^{s}$ if $r$ and $s$ are rational.
(c) If $x$ is real, define $B(x)$ to be the set of all numbers $b^{t}$, where $t$ is rational and $t \leq x$. Prove that

$$
b^{r}=\sup B(r)
$$

when $r$ is rational. Hence it makes sense to define

$$
b^{x}=\sup B(x)
$$

for every real $x$.
(d) Prove that $b^{x+y}=b^{x} b^{y}$ for all real $x$ and $y$.
1.7. Fix $b>1, y>0$, and prove that there is a unique real $x$ such that $b^{x}=y$, by completing the following outline. (This $x$ is called the logarithm of $y$ to the base b.)
(a) For any positive integer $n, b^{n}-1 \geq n(b-1)$.
(b) Hence $b-1 \geq n\left(b^{1 / n}-1\right)$.
(c) If $t>1$ and $n>(b-1) /(t-1)$, then $b^{1 / n}<t$.
(d) If $w$ is such that $b^{w}<y$, then $b^{w+(1 / n)}<y$ for sufficiently large $n$; to see this, apply part (c) with $t=y \cdot b^{-w}$.
(e) If $b^{w}>y$, then $b^{w-(1 / n)}>y$ for sufficiently large $n$.
(f) Let $A$ be the set of all $w$ such that $b^{w}<y$, and show that $x=\sup A$ satisfies $b^{x}=y$.

(g) Prove that this $x$ is unique.
1.8. Prove that no order can be defined in the complex field that turns it into an ordered field. Hint: -1 is a square.
1.9. Suppose $z=a+b i, w+c+d i$. Define $z<w$ if $a<c$, and also if $a=c$ but $b<d$. Prove that this turns the set of complex numbers into an ordered set. (This type of order relation is called a dictionary order, or lexicographic order, for obvious reasons.) Does this ordered set have the least-upper-bound property?
1.10. Suppose $z=a+b i, w=u+i v$, and

$$
a=\left(\frac{|w|+u}{2}\right)^{1 / 2}, \quad b=\left(\frac{|w|-u}{2}\right)^{1 / 2}
$$

Prove that $z^{2}=w$ if $v \geq 0$ and that $|\bar{z}|^{2}=w$ if $v \leq 0$. Conclude that every complex number (with one exception!) has two complex square roots.
1.11. If $z$ is a complex number, prove that there exists an $r \geq 0$ and a complex number $w$ with $|w|=1$ such that $z=r w$. Are $w$ and $r$ always uniquely determined by $z$ ?
1.12. If $z_{1}, \ldots, z_{n}$ are complex, prove that

$$
\left|z_{1}+z_{2}+\cdots+z_{n}\right| \leq\left|z_{1}\right|+\left|z_{2}\right|+\cdots+\left|z_{n}\right|
$$

1.13. If $x, y$ are complex, prove that

$$
||x|-|y|| \leq|x-y|
$$

1.14. If $z$ is a complex number such that $|z|=1$, that is, such that $z \bar{z}=1$, compute

$$
|1+z|^{2}+|1-z|^{2}
$$

1.15. Under what conditions does equality hold in the Schwarz inequality?
1.16. Suppose $k \geq 3, \mathbf{x}, \mathbf{y} \in \mathbb{R}^{\mathrm{k}},|\mathbf{x}-\mathbf{y}|=\mathrm{d}>0$, and $\mathrm{r}>0$. Prove:
(a) If $2 r>d$, there are infinitely many $\mathbf{z} \in \mathbb{R}^{\mathrm{k}}$ such that

$$
|\mathbf{z}-\mathbf{x}|=|\mathbf{z}-\mathbf{y}|=\mathrm{r}
$$

(b) If $2 r=d$, there is exactly one such $\mathbf{z}$.
(c) If $2 r<d$, there is no such $\mathbf{z}$.

How must these statements be modified if k is 2 or 1 ?
1.17. Prove that

$$
|\mathbf{x}+\mathbf{y}|^{2}+|\mathbf{x}-\mathbf{y}|^{2}=2|\mathbf{x}|^{2}+2|\mathbf{y}|^{2}
$$

if $\mathbf{x} \in \mathbb{R}^{\mathrm{k}}$ and $\mathbf{y} \in \mathbb{R}^{\mathrm{k}}$. Interpret this geometrically, as a statement about parallelograms.
1.18. If $k \geq 2$ and $x \in \mathbb{R}^{k}$, prove that there exists $y \in \mathbb{R}^{k}$ such that $y \neq 0$ but $x \cdot y=0$. Is this also true if $k=1$ ?
1.19. Suppose $\mathbf{a} \in \mathbb{R}^{\mathrm{k}}, \mathbf{b} \in \mathbb{R}^{\mathrm{k}}$. Find $\mathbf{c} \in \mathbb{R}^{\mathrm{k}}$ and $\mathrm{r}>0$ such that

$$
|\mathbf{x}-\mathbf{a}|=2|\mathbf{x}-\mathbf{b}|
$$

if and only if $|\mathbf{x}-\mathbf{c}|=\mathrm{r}$.
(Solution: $\left.\left.3 \mathbf{c}=4 \mathbf{b}-\mathbf{a}, 3 \mathrm{r}=2|\mathbf{b}-\mathbf{a}|\right)\right)$
1.20. With reference to the Appendix, suppose that property (III) were omitted from the definition of a cut. Keep the same definitions of order and addition. Show that the resulting ordered set has the least-upper-bound property, that addition satisfies axioms (A1) to (A4) (with a slightly different zero-element!) but that (A5) fails.

# Chapter 2 

## BASIC TOPOLOGY

## FINITE, COUNTABLE, AND UNCOUNTABLE SETS

We begin this section with a definition of the function concept.
2.1 Definition. Consider two sets $A$ and $B$, whose elements may be any objects whatsoever, and suppose that with each element $x$ of $A$ there is associated, in some manner, an element of $B$, which we denote by $f(x)$. Then $f$ is said to be a function from A to B (or a mapping of A into B ). The set A is called the domain of f (we also say $f$ is defined on $A$ ) and the elements $f(x)$ are called the values of $f$. The set of all values of $f$ is called the range of $f$.
2.2 Definition. Let $A$ and $B$ be two sets and let $f$ be a mapping of $A$ into $B$. If $E \subset A, f(E)$ is defined to be the set of all elements $f(x)$, for $x \in E$. We call $f(E)$ the image of $E$ under $f$. In this notation, $f(A)$ is the range of $f$. It is clear that $f(A) \subset B$. If $f(A)=B$, we say that $f$ maps $A$ onto $B$. (Note that, according to this usage, onto is more specific than into).

If $E \subset B, f^{-1}(E)$ denotes the set of all $x \in A$ such that $f(x) \in E$. We call $f^{-1}(E)$ the inverse image of $E$ under $f$. If $y \in B, f^{-1}(y)$ is the set of all $x \in A$ such that $f(x)=y$. If, for each $y \in B, f^{-1}(y)$ consists of at most one element of $A$, then $f$ is said to be a 1-1 (one-to-one) mapping of $A$ into $B$. This may also be expressed as follows: $f$ is a 1-1 mapping of $A$ into $B$ provided that $f\left(x_{1}\right) \neq f\left(x_{2}\right)$ whenever $x_{1} \neq x_{2}, x_{1} \in A, x_{2} \in A$.
(The notation $x_{1} \neq x_{2}$ means that $x_{1}$ and $x_{2}$ are distinct elements; otherwise we write $x_{1}=x_{2}$.)
2.3 Definition. If there exists a 1-1 mapping of $A$ onto $B$, we say that $A$ and $B$ can be put in 1-1 correspondence, or that $A$ and $B$ have the same cardinal number, or, briefly, that $A$ and $B$ are equivalent, and we write $A \sim B$. This relation clearly has the following properties:

It is reflexive: $A \sim A$.

It is symmetric: If $A \sim B$, then $B \sim A$.
It is transitive: If $A \sim B$ and $B \sim C$, then $A \sim C$.
Any relation with these three properties is called an equivalence relation.
2.4 Definition. For any positive integer $n$, let $\mathbb{N}_{n}$ be the set whose elements are the integers $1,2, \ldots, n$; let $\mathbb{N}$ be the set consisting of all positive integers. For any set $A$, we say:
(a) $A$ is finite if $A \sim \mathbb{N}_{n}$ for some $n$ (the empty set is also considered to be finite).
(b) $A$ is infinite if $A$ is not finite.
(c) $A$ is countable if $A \sim \mathbb{N}$.
(d) $A$ is uncountable if $A$ is neither finite nor countable.
(e) $A$ is at most countable if $A$ is finite or countable.

Countable sets are sometimes called enumerable, or denumerable.
For two finite sets $A$ and $B$, we evidently have $A \sim B$ if and only if $A$ and $B$ contain the same number of elements. For infinite sets, however, the idea of "having the same number of elements" becomes quite vague, whereas the notion of 1-1 correspondence retains its clarity.
2.5 Example. Let $\mathbb{Z}$ be the set of all integers. Then $\mathbb{Z}$ is countable. For, consider the following arrangement of the sets $\mathbb{Z}$ and $\mathbb{N}$ :

$$
\begin{array}{ll}
\mathbb{Z}: & 0,1,-1,2,-2,3,-3, \ldots \\
\mathbb{N}: & 1,2,3,4,5,6,7, \ldots
\end{array}
$$

We can, in this example, even give an explicit formula for a function $f$ from $\mathbb{N}$ to $\mathbb{Z}$ which sets up a 1-1 correspondence:

$$
f(n)= \begin{cases}\frac{n}{2} & (n \text { even }) \\ -\frac{n-1}{2} & (n \text { odd })\end{cases}
$$

2.6 Remark. A finite set cannot be equivalent to one of its proper subsets. That this is, however, possible for infinite sets, is shown by Example 2.5, in which $\mathbb{N}$ is a proper subset of $\mathbb{Z}$.

In fact, we could replace def:2.4(b) by the statement: $A$ is infinite if $A$ is equivalent to one of its proper subsets.
2.7 Definition. By a sequence, we mean a function $f$ defined on the set $\mathbb{N}$ of all positive integers. If $f(n)=x_{n}$, for $n \in \mathbb{N}$, it is customary to denote the sequence $f$ by the symbol $\left(x_{n}\right)_{n=1}^{\infty}$, or more briefly by $\left(x_{n}\right)$, or sometimes by $x_{1}, x_{2}, x_{3}, \ldots$. The values of $f$, that is, the elements $x_{n}$, are called the terms of the sequence. If $A$ is a set and if $x_{n} \in A$ for all $n \in \mathbb{N}$, then $\left(x_{n}\right)$ is said to be a sequence in $A$, or a sequence of elements of $A$.

Note that the terms $x_{1}, x_{2}, x_{3}, \ldots$ of a sequence need not be distinct.
Since every countable set is the range of a 1-1 function defined on $\mathbb{N}$, we may regard every countable set as the range of a sequence of distinct terms. Speaking more loosely, we may say that the elements of any countable set can be "arranged in a sequence."

Sometimes it is convenient to replace $\mathbb{N}$ in this definition by the set of all nonnegative integers, i.e., to start with 0 rather than 1.
2.8 Theorem. Every infinite subset of a countable set A is countable.

Proof. Suppose $E \subset A$, and $E$ is infinite. Arrange the elements $x$ of $A$ in a sequence $\left(x_{n}\right)$ of distinct elements. Construct a sequence $\left(n_{k}\right)$ as follows:

Let $n_{1}$ be the smallest positive integer such that $x_{n_{1}} \in E$. Having chosen $n_{1}, \ldots, n_{k-1}(k=2,3,4, \ldots)$, let $n_{k}$ be the smallest integer greater than $n_{k-1}$ such that $x_{n_{k}} \in E$.

Putting $f(k)=x_{n_{k}}(k=1,2,3, \ldots)$, we obtain a 1-1 correspondence between $E$ and $\mathbb{N}$.

The theorem shows that, roughly speaking, countable sets represent the "smallest" infinite: No uncountable set can be a subset of a countable set.
2.9 Definition. Let $A$ and $\Omega$ be sets, and suppose that with each element $\alpha$ of $A$ there is associated a subset of $\Omega$ which we denote by $E_{\alpha}$.

The set whose elements are the sets $E_{\alpha}$ will be denoted by $\left\{E_{\alpha}\right\}$. Instead of speaking of sets of sets, we shall sometimes speak of a collection of sets, or a family of sets.

The union of the sets $E_{\alpha}$ is defined to be the set $S$ such that $x \in S$ if and only if $x \in E_{\alpha}$ for at least one $\alpha \in A$. We use the notation

$$
S=\bigcup_{\alpha \in A} E_{\alpha}
$$

If $A$ consists of the integers $1,2, \ldots, n$, one usually writes

$$
S=\bigcup_{m=1}^{n} E_{m}
$$

or

$$
S=E_{1} \cup E_{2} \cup \cdots \cup E_{n}
$$

If $A$ is the set of all positive integers, the usual notation is

$$
S=\bigcup_{m=1}^{\infty} E_{m}
$$

The symbol $\infty$ in (2.4) merely indicates that the union of a countable collection of sets is taken, and should not be confused with the symbols $+\infty,-\infty$, introduced

in Definition 1.23.
The intersection of the sets $\mathrm{E}_{\alpha}$ is defined to be the set P such that $\mathrm{x} \in \mathrm{P}$ if and only if $x \in E_{\alpha}$ for every $\alpha \in A$. We use the notation

$$
P=\bigcap_{\alpha \in A} E_{\alpha}
$$

or

$$
P=\bigcap_{m=1}^{n} E_{m}=E_{1} \cap E_{2} \cap \cdots \cap E_{n}
$$

or

$$
P=\bigcap_{m=1}^{\infty} E_{m}
$$

as for unions. If $A \cap B$ is not empty, we say that $A$ and $B$ intersect; otherwise they are disjoint.

# 2.10 Examples. 

(a) Suppose $E_{1}$ consists of $1,2,3$ and $E_{2}$ consists of $2,3,4$. Then $E_{1} \cup E_{2}$ consists of $1,2,3,4$, whereas $E_{1} \cap E_{2}$ consists of 2,3 .
(b) Let $A$ be the set of real numbers $x$ such that $0<x \leq 1$. For every $x \in A$, let $E_{x}$ be the set of real numbers $y$ such that $0<y<x$. Then
(i)

$$
E_{x} \subset E_{z} \text { if and only if } 0<x \leq z \leq 1
$$

(ii)

$$
\bigcup_{x \in A} E_{x}=E_{1}
$$

(iii)

$$
\bigcap_{x \in A} E_{x} \text { is empty. }
$$

(i) and (ii) are clear. To prove (iii), we note that for every $y>0, y \notin E_{x}$ if $x<y$. Hence $y \notin \bigcap_{x \in A} E_{x}$.
2.11 Remarks. Many properties of unions and intersections are quite similar to those of sums and products; in fact, the words sum and product were sometimes used in this connection, and the symbols $\Sigma$ and $\Pi$ were written in place of $\bigcup$ and $\cap$.

The commutative and associative laws are trivial:

$$
A \cup B=B \cup A ; \quad A \cap B=B \cap A
$$

$$
(A \cup B) \cup C=A \cup(B \cup C) ; \quad(A \cap B) \cap C=A \cap(B \cap C)
$$

Thus the omission of parenthesis in (2.3) and (2.6) is justified.
The distributive law also holds:

$$
A \cap(B \cup C)=(A \cap B) \cup(A \cap C)
$$

To prove this, let the left and right members of (2.10) be denoted by E and F , respectively.

Suppose $x \in E$. Then $x \in A$ and $x \in B \cup C$, that is, $x \in B$ or $x \in C$ (possibly both). Hence $x \in A \cap B$ or $x \in A \cap C$, so that $x \in F$. Thus $E \subset F$.

Next, suppose $x \in F$. Then $x \in A \cap B$ or $x \in A \cap C$. That is, $x \in A$, and $x \in B \cup C$. Hence $x \in A \cap(B \cup C)$, so that $F \subset E$.

It follows that $E=F$.
We list a few more relations which are easily verified:

$$
\begin{aligned}
& A \subset A \cup B \\
& A \cap B \subset A
\end{aligned}
$$

If $\varnothing$ denotes the empty set, then

$$
A \cup \varnothing=A, \quad A \cap \varnothing=\varnothing
$$

If $A \subset B$, then

$$
A \cup B=B, \quad A \cap B=A
$$

2.12 Theorem. Let $\left\{E_{n}\right\}, n=1,2,3, \ldots$, be a countable collection of countable sets, and put

$$
S=\bigcup_{n=1}^{\infty} E_{n}
$$

Then $S$ is countable.
Proof. Let every set $E_{n}$ be arranged in a sequence $\left(x_{n k}\right), k=1,2,3, \ldots$, and consider the infinite array
![img-0.jpeg](img-0.jpeg)
in which the elements of $E_{n}$ form the nth row. The array contains all elements of $S$. As indicated by the arrows, these elements can be arranged in a sequence

$$
x_{11} ; x_{21}, x_{12} ; x_{31}, x_{22} \cdot x_{13} ; x_{41}, x_{32}, x_{23}, x_{14} ; \ldots
$$

If any two of the sets $E_{n}$ have elements in common, these will appear more than once in (2.17). Hence there is a subset $T$ of the set of all positive integers such that $S \sim T$, which shows that $S$ is at most countable (Theorem 2.8). Since $E_{1} \subset S$, and $E_{1}$ is infinite, $S$ is infinite, and thus countable.

Corollary. Suppose A is at most countable, and, for every $\alpha \in \mathrm{A}, \mathrm{B}_{\alpha}$ is at most countable. Put

$$
\mathrm{T}=\bigcup_{\alpha \in \mathrm{A}} \mathrm{~B}_{\alpha}
$$

Then T is at most countable, for T is equivalent to a subset of (2.15).
2.13 Theorem. Let A be a countable set, and let $\mathrm{B}_{n}$ be the set of all n-tuples $\left(a_{1}, \ldots, a_{n}\right)$, where $a_{k} \in A(k=1, \ldots, n)$, and the elements $a_{1}, \ldots, a_{n}$ need not be distinct. Then $\mathrm{B}_{n}$ is countable.

Proof. That $B_{1}$ is countable is evident, since $B_{1}=A$. Suppose $B_{n-1}$ is countable $(n=2,3,4, \ldots)$. The elements of $B_{n}$ are of the form

$$
(b, a) \quad\left(b \in B_{n-1}, a \in A\right)
$$

For every fixed $b$, the set of pairs $(b, a)$ is equivalent to $A$, and hence countable. Thus $B_{n}$ is the union of a countable set of countable sets. By Theorem $2.12, B_{n}$ is countable.

The theorem follows by induction.
Corollary. The set of all rational numbers is countable.
Proof. We apply Theorem 2.13, with $n=2$, noting that every rational $r$ is of the form $b / a$, where $a$ and $b$ are integers. The set of pairs $(a, b)$, and therefore the set of fractions $b / a$, is countable.

In fact, even the set of all algebraic numbers is countable (see Exercise 2.2). That not all infinite sets are, however, countable, is shown by the next theorem.
2.14 Theorem. Let A be the set of all sequences whose elements are the digits 0 and 1 . This set A is uncountable.

The elements of $A$ are sequences like $1,0,0,1,0,1,1,1, \ldots$
Proof. Let E be a countable subset of A , and let E consist of the sequences $s_{1}, s_{2}, s_{3}, \ldots$ We construct a sequence $s$ as follows. If the nth digit in $s_{n}$ is 1 , we let the nth digit of $s$ be 0 , and vice versa. Then the sequence $s$ differs from every member of $E$ in at least one place; hence $s \notin E$. But clearly $s \in A$, so that $E$ is a proper subset of $A$.

We have shown that every countable subset of $A$ is a proper subset of $A$. It follows that $A$ is uncountable (for otherwise $A$ would be a proper subset of $A$, which is absurd).

The idea of the above proof was first used by Cantor, and is called Cantor's diagonal process; for, if the sequences $s_{1}, s_{2}, s_{3}, \ldots$ are placed in an array like (2.16), it is the elements on the diagonal which are involved in the construction of the new sequence.

Readers who are familiar with the binary representation of the real numbers (base 2 instead of 10) will notice that Theorem 2.14 implies that the set of all real numbers is uncountable. We shall give a second proof of this fact in Theorem 2.43.

# METRIC SPACES 

2.15 Definition. A set $X$, whose elements we shall call points, is said to be a metric space if with any two points $p$ and $q$ of $X$ there is associated a real number $d(p, q)$, called the distance from $p$ to $q$, such that
(a) $d(p, q)>0$ if $p \neq q ; d(p, p)=0$;
(b) $d(p, q)=d(q, p)$;
(c) $d(p, q) \leq d(p, r)+d(r, q)$ for any $r \in X$.

Any function with these three properties is called a distance function, or a metric.
2.16 Examples. The most important examples of metric spaces, from our standpoint, are the euclidean spaces $\mathbb{R}^{\mathrm{k}}$, especially $\mathbb{R}^{1}$ (the real line) and $\mathbb{R}^{2}$ (the complex plane); the distance in $\mathbb{R}^{\mathrm{k}}$ is defined by

$$
d(\mathbf{x}, \mathbf{y})=|\mathbf{x}-\mathbf{y}| \quad\left(\mathbf{x}, \mathbf{y} \in \mathbb{R}^{\mathrm{k}}\right)
$$

By Theorem 1.37, the conditions of Definition 2.15 are satisfied by (2.19).
It is important to observe that every subset $Y$ of a metric space $X$ is a metric space in its own right, with the same distance function. For it is clear that if conditions (a) to (c) of Definition 2.15 hold for $p, q, r, \in X$, they also hold if we restrict $p, q, r$ to lie in $Y$.

Thus, every subset of a euclidean space is a metric space. Other examples are the spaces $\mathscr{C}(\mathrm{K})$ and $\mathscr{L}^{2}(\mu)$, which are discussed in Chaps. 7 and 11, respectively.
2.17 Definition. By the segment $(a, b)$ we mean the set of all real numbers $x$ such that $a<x<b$.

By the interval $[a, b]$ we mean the set of all real numbers $x$ such that $a \leq x \leq b$.
Occasionally we shall also encounter "half-open intervals" $[a, b)$ and $(a, b]$; the first consists of all $x$ such that $a \leq x<b$, the second of all $x$ such that $a<x \leq b$.

If $a_{i}<b_{i}$ for $i=1, \ldots, k$, the set of all points $x=\left(x_{1}, \ldots, x_{k}\right)$ in $\mathbb{R}^{k}$ whose coordinates satisfy the inequalities $a_{i} \leq x_{i} \leq b_{i}(1 \leq i \leq k)$ is called a $k$-cell. Thus a 1-cell is an interval, a 2-cell is a rectangle, etc.

If $\mathbf{x} \in \mathbb{R}^{\mathrm{k}}$ and $\tau>0$, the open (or closed) ball B with center at $\mathbf{x}$ and radius $\tau$ is defined to be the set of all $\mathbf{y} \in \mathbb{R}^{\mathrm{k}}$ such that $|\mathbf{y}-\mathbf{x}|<\tau($ or $|\mathbf{y}-\mathbf{x}| \leq \tau)$.

We call a set $E \subset \mathbb{R}^{\mathrm{k}}$ convex if

$$
\lambda \mathbf{x}+(1-\lambda) \mathbf{y} \in E
$$

whenever $\mathbf{x} \in \mathrm{E}, \mathbf{y} \in \mathrm{E}$, and $0<\lambda<1$.

For example, balls are convex. For if $|\mathbf{y}-\mathbf{x}|<\mathrm{r},|\mathbf{z}-\mathbf{x}|<\mathrm{r}$, and $0<\lambda<1$, we have

$$
\begin{aligned}
|\lambda \mathbf{y}+(1-\lambda) \mathbf{z}-\mathbf{x}| & =|\lambda(\mathbf{y}-\mathbf{x})+(1-\lambda)(\mathbf{z}-\mathbf{x})| \\
& \leq \lambda|\mathbf{y}-\mathbf{x}|+(1-\lambda)|\mathbf{z}-\mathbf{x}|<\lambda \mathrm{r}+(1-\lambda) \mathrm{r} \\
& =\mathrm{r}
\end{aligned}
$$

The same proof applies to closed balls. It is also easy to see that k-cells are convex.
2.18 Definition. Let $X$ be a metric space. All points and sets mentioned below are understood to be elements and subsets of $X$.
(a) A neighborhood of p is a set $\mathrm{N}_{\mathrm{r}}(\mathrm{p})$ consisting of all q such that $\mathrm{d}(\mathrm{p}, \mathrm{q})<\mathrm{r}$ for some $r>0$. The number $r$ is called the radius of $N_{r}(p)$.
(b) A point $p$ is a limit point of the set $E$ if every neighborhood of $p$ contains a point $\mathrm{q} \neq \mathrm{p}$ such that $\mathrm{q} \in \mathrm{E}$.
(c) If $\mathrm{p} \in \mathrm{E}$ and p is not a limit point of E , then p is called an isolated point of E .
(d) E is closed if every limit point of E is a point of E .
(e) A point $p$ is an interior point of $E$ if there is a neighborhood $N$ of $p$ such that $\mathrm{N} \subset \mathrm{E}$.
(f) E is open if every point of E is an interior point of E .
(g) The complement of E (denoted by $\mathrm{E}^{\mathrm{c}}$ ) is the set of all points $\mathrm{p} \in \mathrm{X}$ such that $\mathrm{p} \notin \mathrm{E}$.
(h) E is perfect if E is closed and if every point of E is a limit point of E .
(i) E is bounded if there is a real number $M$ and a point $q \in X$ such that $d(p, q)<$ $M$ for all $p \in E$.
(j) E is dense in X if every point of X is a limit point of E , or a point of E (or both).

Let us note that in $\mathbb{R}^{1}$ neighborhoods are segments, whereas in $\mathbb{R}^{2}$ neighborhoods are interiors of circles.
2.19 Theorem. Every neighborhood is an open set.

Proof. Consider a neighborhood $E=N_{r}(p)$, and let $q$ be any point of $E$. Then there is a positive real number $h$ such that

$$
\mathrm{d}(\mathrm{p}, \mathrm{q})=\mathrm{r}-\mathrm{h}
$$

For all points $s$ such that $\mathrm{d}(\mathrm{q}, \mathrm{s})<\mathrm{h}$, we have then

$$
\mathrm{d}(\mathrm{p}, \mathrm{~s}) \leq \mathrm{d}(\mathrm{p}, \mathrm{q})+\mathrm{d}(\mathrm{q}, \mathrm{~s})<\mathrm{r}-\mathrm{h}+\mathrm{h}=\mathrm{r}
$$

so that $s \in E$. Thus $q$ is an interior point of $E$.
2.20 Theorem. If p is a limit point of a set E , then every neighborhood of p contains infinitely many points of E .

Proof. Suppose there is a neighborhood N of p which contains only a finite number of points of E. Let $\mathrm{q}_{1}, \ldots, \mathrm{q}_{\mathrm{n}}$ be those points of $\mathrm{N} \cap \mathrm{E}$ which are distinct from p , and put

$$
r=\min _{1 \leq m \leq n} d\left(p, q_{m}\right)
$$

[We use this notation to denote the smallest of the numbers $\left.d\left(p, q_{1}\right), \ldots, d\left(p, q_{n}\right).\right]$ The minimum of a finite set of positive numbers is clearly positive, so that $r>0$.

The neighborhood $\mathrm{N}_{\mathrm{r}}(\mathrm{p})$ contains no point q of E such that $\mathrm{q} \neq \mathrm{p}$, so that p is not a limit point of E. This contradiction establishes the theorem.

Corollary. A finite point set has no limit points.
2.21 Examples. Let us consider the following subset of $\mathbb{R}^{2}$ :
(a) The set of all complex $z$ such that $|z|<1$.
(b) The set of all complex $z$ such that $|z| \leq 1$.
(c) A nonempty finite set.
(d) The set of all integers.
(e) The set consisting of the numbers $1 / n(n=1,2,3, \ldots)$. Let us note that this set E has a limit point (namely, $z=0$ ) but that no point of E is a limit point of E; we wish to stress the difference between having a limit point and containing one.
(f) The set of all complex numbers (that is, $\mathbb{R}^{2}$ ).
(g) The segment $(a, b)$.

Let us note that (d), (e), (g) can be regarded also as subsets of $\mathbb{R}^{1}$.
Some properties of these sets are tabulated below:

|  | Closed | Open | Perfect | Bounded |
| :-- | :--: | :--: | :--: | :--: |
| (a) | No | Yes | No | Yes |
| (b) | Yes | No | Yes | Yes |
| (c) | Yes | No | No | Yes |
| (d) | Yes | No | No | No |
| (e) | No | No | No | Yes |
| (f) | Yes | Yes | Yes | No |
| (g) | No |  | No | Yes |

In (g), we left the second entry blank. The reason is that the segment $(a, b)$ is not open if we regard it as a subset of $\mathbb{R}^{2}$, but it is an open subset of $\mathbb{R}^{1}$.
2.22 Theorem. Let $\left\{E_{\alpha}\right\}$ be a (finite or infinite) collection of sets $\mathrm{E}_{\alpha}$. Then

$$
\left(\bigcup_{\alpha} E_{\alpha}\right)^{c}=\bigcap_{\alpha}\left\{E_{\alpha}^{c}\right\}
$$

Proof. Let $A$ and $B$ be the left and right members of (2.20). If $x \in A$, then $x \notin$ $\bigcup_{\alpha} E_{\alpha}$, hence $x \notin E_{\alpha}$ for any $\alpha$, hence $x \in E_{\alpha}^{c}$ for every $\alpha$, so that $x \in \cap E_{\alpha}^{c}$. Thus $A \subset B$.

Conversely, if $x \in B$, then $x \in E_{\alpha}^{c}$ for every $\alpha$, hence $x \notin E_{\alpha}$ for any $\alpha$, hence $x \notin \bigcup_{\alpha} E_{\alpha}$, so that $x \in\left(\bigcup_{\alpha} E_{\alpha}\right)^{c}$. Thus $B \subset A$.

It follows that $A=B$.
2.23 Theorem. A set E is open if and only if its complement is closed.

Proof. First, suppose $E^{c}$ is closed. Choose $x \in E$. Then $x \notin E^{c}$, and $x$ is not a limit point of $E^{c}$. Hence there exists a neighborhood $N$ of $x$ such that $E^{c} \cap N$ is empty, that is, $N \subset E$. Thus $x$ is an interior point of $E$, and $E$ is open.

Next, suppose $E$ is open. Let $x$ be a limit point of $E^{c}$. Then every neighborhood of $x$ contains a point of $E^{c}$, so that $x$ is not an interior point of $E$. Since $E$ is open, this means that $x \in E^{c}$. It follows that $E^{c}$ is closed.

Corollary. A set $F$ is closed if and only if its complement is open.

# 2.24 Theorem. 

(a) For any collection $\left\{\mathrm{G}_{\alpha}\right\}$ of open sets, $\bigcup_{\alpha} \mathrm{G}_{\alpha}$ is open.
(b) For any collection $\left\{F_{\alpha}\right\}$ of closed sets, $\bigcap_{\alpha} F_{\alpha}$ is closed.
(c) For any finite collection $G_{1}, \ldots, G_{n}$ of open sets, $\bigcap_{i=1}^{n} G_{i}$ is open.
(d) For any finite collection $F_{1}, \ldots, F_{n}$ of closed sets, $\bigcup_{i=1}^{n} F_{i}$ is closed.

Proof. Put $G=\bigcup_{\alpha} G_{\alpha}$. If $x \in G$ then $x \in G_{\alpha}$ for some $\alpha$. Since $x$ is an interior point of $G_{\alpha}, x$ is also an interior point of $G$, and $G$ is open. This proves (a).

By Theorem 2.22,

$$
\left(\bigcap_{\alpha} F_{\alpha}\right)^{c}=\bigcup_{\alpha}\left(F_{\alpha}^{c}\right)
$$

and $F_{\alpha}^{c}$ is open, by Theorem 2.23. Hence (a) implies that (2.21) is open so that $\bigcap_{\alpha} F_{\alpha}$ is closed.

Next, put $H=\bigcap_{i=1}^{n} G_{i}$. For any $x \in H$, there exist neighborhoods $N_{i}$ of $x$, with radii $r_{i}$, such that $N_{i} \subset G_{i}(i=1, \ldots, n)$. Put

$$
r=\min \left\{r_{1}, \ldots, r_{n}\right\}
$$

and let $N$ be the neighborhood of $x$ of radius $r$. Then $N \subset G_{i}$ for $i=1, \ldots, n$, so that $N \subset H$, and $H$ is open.

By taking complements, (d) follows from (c):

$$
\left(\bigcup_{i=1}^{n} F_{i}\right)^{c}=\bigcap_{i=1}^{n}\left(F_{i}^{c}\right)
$$

2.25 Example. In parts (c) and (d) of the preceding theorem, the finiteness of the collections is essential. For let $G_{n}$ be the segment $(-1 / n, 1 / n)(n=1,2,3, \ldots)$. Then $G_{n}$ is an open subset of $\mathbb{R}^{1}$. Put $G=\bigcap_{n=1}^{\infty} G_{n}$. Then $G$ consists of a single point (namely, $x=0$ ) and is therefore not an open subset of $\mathbb{R}^{1}$.

Thus the intersection of an infinite collection of open sets need not be open. Similarly, the union of an infinite collection of closed sets need not be closed.
2.26 Definition. If $X$ is a metric space, if $E \subset X$, and if $E^{\prime}$ denotes the set of all limit points of $E$ in $X$, then the closure of $E$ is the set $\overline{\mathrm{E}}=\mathrm{E} \cup \mathrm{E}^{\prime}$.
2.27 Theorem. If $X$ is a metric space and $E \subset X$, then
(a) $\overline{\mathrm{E}}$ is closed,
(b) $E=\overline{\mathrm{E}}$ if and only if E is closed,
(c) $\overline{\mathrm{E}} \subset \mathrm{F}$ for every closed set $\mathrm{F} \subset \mathrm{X}$ such that $\mathrm{E} \subset \mathrm{F}$.

By (a) and (c), $\overline{\mathrm{E}}$ is the smallest closed subset of X that contains E .
Proof.
(a) If $p \in X$ and $p \notin \bar{E}$ then $P$ is neither a point of $E$ nor a limit point of $E$. Hence $p$ has a neighborhood which does not intersect $E$. The complement of $\bar{E}$ is therefore open. Hence $\bar{E}$ is closed.
(b) If $E=\bar{E}$, (a) implies that $E$ is closed. If $E$ is closed, then $E^{\prime} \subset E$ [by Definitions 2.18(d) and 2.26], hence $\overline{\mathrm{E}}=\mathrm{E}$.
(c) If $F$ is closed and $F \supset E$, then $F \supset F^{\prime}$, hence $F \supset E^{\prime}$. Thus $F \supset \bar{E}$.
2.28 Theorem. Let E be a nonempty set of real numbers which is bounded above. Let $y=\sup E$. Then $y \in \bar{E}$. Hence $y \in E$ if $E$ is closed.

Compare this with the examples in Sec. 1.9.
Proof. If $y \in E$ then $y \in \bar{E}$. Assume $y \notin E$. For every $h>0$ there exists then a point $x \in E$ such that $y-h<x<y$, for otherwise $y-h$ would be an upper bound of $E$. Thus $y$ is a limit point of $E$. Hence $y \in \bar{E}$.
2.29 Remark. Suppose $E \subset Y \subset X$, where $X$ is a metric space. To say that $E$ is an open subset of $X$ means that to each point $p \in E$ there is associated a positive number $r$ such that the conditions $d(p, q)<r, q \in X$ imply that $q \in E$. But we have already observed (Example 2.16) that $Y$ is also a metric space, so that our definitions may equally well be made within $Y$. To be quite explicit, let us say that $E$ is open relative to $Y$ if to each $p \in E$ there is associated an $r>0$ such that $q \in E$ whenever $d(p, q)<r$ and $q \in Y$. Example $2.21(\mathrm{~g})$ showed that a set may be open relative to $Y$ without being an open subset of $X$. However, there is a simple relation between these concepts, which we now state.
2.30 Theorem. Suppose $Y \subset X$. A subset $E$ of $Y$ is open relative to $Y$ if and only if $E=Y \cap G$ for some open subset $G$ of $X$.

Proof. Suppose E is open relative to Y . To each $\mathrm{p} \in \mathrm{E}$ there is a positive number $\mathrm{r}_{\mathrm{p}}$ such that the conditions $\mathrm{d}(\mathrm{p}, \mathrm{q})<\mathrm{r}_{\mathrm{p}}, \mathrm{q} \in \mathrm{Y}$ imply that $\mathrm{q} \in \mathrm{E}$. Let $\mathrm{V}_{\mathrm{p}}$ be the set of all $\mathrm{q} \in \mathrm{X}$ such that $\mathrm{d}(\mathrm{p}, \mathrm{q})<\mathrm{r}_{\mathrm{p}}$ and define

$$
\mathrm{G}=\bigcup_{\mathrm{p} \in \mathrm{E}} \mathrm{~V}_{\mathrm{p}}
$$

Then G is an open subset of X , by Theorems 2.19 and 2.24.
Since $\mathrm{p} \in \mathrm{V}_{\mathrm{p}}$ for all $\mathrm{p} \in \mathrm{E}$, it is clear that $\mathrm{E} \subset \mathrm{G} \cap \mathrm{Y}$.
By our choice of $V_{p}$, we have $V_{p} \cap Y \subset E$ for every $p \in E$, so that $G \cap Y \subset E$. Thus $E=G \cap Y$, and one half of the theorem is proved.

Conversely, if G is open in X and $\mathrm{E}=\mathrm{G} \cap \mathrm{Y}$, every $\mathrm{p} \in \mathrm{E}$ has a neighborhood $V_{p} \subset G$. Then $V_{p} \cap Y \subset E$, so that $E$ is open relative to $Y$.

# COMPACT SETS 

2.31 Definition. By an open cover of a set $E$ in a metric space $X$ we mean a collection $\left\{\mathrm{G}_{\alpha}\right\}$ of open subset of X such that $\mathrm{E} \subset \bigcup_{\alpha} \mathrm{G}_{\alpha}$.
2.32 Definition. A subset K of a metric space X is said to be compact if every open cover of K contains a finite subcover.

More explicitly, this requirement is that if $\left\{\mathrm{G}_{\alpha}\right\}$ is an open cover of K , then there are finitely many indices $\alpha_{1}, \ldots, \alpha_{n}$ such that

$$
\mathrm{K} \subset \mathrm{G}_{\alpha_{1}} \cup \cdots \cup \mathrm{G}_{\alpha_{n}}
$$

The notion of compactness is of great importance in analysis, especially in connection with continuity (Chap. 4).

It is clear that every finite set is compact. The existence of a large class of infinite compact sets in $\mathbb{R}^{\mathrm{k}}$ will follow from Theorem 2.41.

We observed earlier (in Remark 2.29) that if $\mathrm{E} \subset \mathrm{Y} \subset \mathrm{X}$, then E may be open relative to Y without being open relative to X . The property of being open thus depends on the space in which E is embedded. The same is true of the property of being closed.

Compactness, however, behaves better, as we shall now see. To formulate the next theorem, let us say, temporarily, that K is compact relative to X if the requirements of Definition 2.32 are met.
2.33 Theorem. Suppose $\mathrm{K} \subset \mathrm{Y} \subset \mathrm{X}$. Then K is compact relative to X if and only if K is compact relative to Y .

By virtue of this theorem we are able, in many situations, to regard compact sets as metric spaces in their own right, without paying any attention to any embedding space. In particular, although it makes little sense to talk of open spaces, or of closed spaces (every metric space X is an open subset of itself, and is a closed subset of itself), it does make sense to talk of compact metric spaces.

Proof. Suppose K is compact relative to X , and let $\left\{V_{\alpha}\right\}$ be a collection of sets, open relative to $Y$, such that $K \subset \bigcup_{\alpha} V_{\alpha}$. By Theorem 2.30, there are sets $G_{\alpha}$, open relative to $X$, such that $V_{\alpha}=Y \cap G_{\alpha}$, for all $\alpha$; and since $K$ is compact relative to $X$, we have

$$
K \subset G_{\alpha_{1}} \cup \cdots \cup G_{\alpha_{n}}
$$

for some choice of finitely many indices $\alpha_{1}, \ldots, \alpha_{n}$. Since $K \subset Y$, (2.22) implies

$$
K \subset V_{\alpha_{1}} \cup \cdots \cup V_{\alpha_{n}}
$$

This proves that K is compact relative to Y .
Conversely, suppose K is compact relative to Y , let $\left\{G_{\alpha}\right\}$ be a collection of open subset of $X$ which covers $K$ and put $V_{\alpha}=Y \cap G_{\alpha}$. Then (2.23) will hold for some choice of $\alpha_{1}, \ldots, \alpha_{n}$; since $V_{\alpha} \subset G_{\alpha}$, (2.23) implies (2.22).

This completes the proof.
2.34 Theorem. Compact subsets of metric spaces are closed.

Proof. Let K be a compact subset of a metric space X . We shall prove that the complement of K is an open subset of X .

Suppose $\mathrm{p} \in \mathrm{X}, \mathrm{p} \notin \mathrm{K}$. If $\mathrm{q} \in \mathrm{K}$, let $\mathrm{V}_{\mathrm{q}}$ and $\mathrm{W}_{\mathrm{q}}$ be neighborhoods of p and q , respectively, of radius less than $\frac{1}{2} \mathrm{~d}(\mathrm{p}, \mathrm{q})$ [see Definition 2.18(a). Since K is compact, there are finitely many points $q_{1}, \ldots, q_{n}$ in $K$ such that

$$
K \subset W_{q_{1}} \cup \cdots \cup W_{q_{n}}=W
$$

If $V=V_{q_{1}} \cap \cdots \cap V_{q_{n}}$, then $V$ is a neighborhood of $p$ which does not intersect $W$. Hence $V \in K^{c}$, so that $p$ is an interior point of $K^{c}$. The theorem follows.
2.35 Theorem. Closed subsets of compact sets are compact.

Proof. Suppose $F \subset K \subset X, F$ is closed (relative to $X$ ), and $K$ is compact. Let $\left\{V_{\alpha}\right\}$ be an open cover of $F$. If $F^{c}$ is adjoined to $\left\{V_{\alpha}\right\}$, we obtain an open cover $\Omega$ of $K$. Since K is compact, there is a finite subcollection $\Phi$ of $\Omega$ which covers K , and hence F . If $F^{c}$ is a member of $\Phi$, we may remove it from $\Phi$ and still retain an open cover of $F$. We have thus shown that a finite subcollection of $\left\{V_{\alpha}\right\}$ covers $F$.

Corollary. If F is closed and K is compact, then $\mathrm{F} \cap \mathrm{K}$ is compact.
Proof. Theorems 2.24(b) and 2.34 show that $F \cap K$ is closed; since $F \cap K \subset K$, Theorem 2.35 shows that $F \cap K$ is compact.
2.36 Theorem. If $\left\{K_{\alpha}\right\}$ is a collection of compact subsets of a metric space $X$ such that the intersection of every finite subcollection of $\left\{K_{\alpha}\right\}$ is nonempty, then $\cap K_{\alpha}$ is nonempty.

Proof. Fix a member $K_{1}$ of $\left\{K_{\alpha}\right\}$ and put $G_{\alpha}=K_{\alpha}^{c}$. Assume that no point of $K_{1}$ belongs to every $\mathrm{K}_{\alpha}$. Then the sets $\mathrm{G}_{\alpha}$ form an open cover of $\mathrm{K}_{1}$; since $\mathrm{K}_{1}$ is compact, there are finitely many indices $\alpha_{1}, \ldots, \alpha_{n}$ such that $K_{1} \subset G_{\alpha_{1}} \cup \cdots \cup$ $G_{\alpha_{n}}$. But this means that

$$
\mathrm{K}_{1} \cap \mathrm{~K}_{\alpha_{1}} \cap \cdots \cap \mathrm{~K}_{\alpha_{n}}
$$

is empty, in contradiction to our hypothesis.
Corollary. If $\left\{K_{n}\right\}$ is a countable collection of nonempty compact sets such that $K_{n} \supset$ $\mathrm{K}_{n+1}(\mathrm{n}=1,2,3, \ldots)$, then $\bigcap_{n=1}^{\infty} \mathrm{K}_{n}$ is not empty.
2.37 Theorem. If E is an infinite subset of a compact set K , then E has a limit point in K .

Proof. If no point of K were a limit point of E , then each $\mathrm{q} \in \mathrm{K}$ would have a neighborhood $\mathrm{V}_{\mathrm{q}}$ which contains at most one point of E (namely, q , if $\mathrm{q} \in \mathrm{E}$ ). It is clear that no finite subcollection of $\left\{V_{q}\right\}$ can cover E ; and the same is true of K , since $\mathrm{E} \subset \mathrm{K}$. This contradicts the compactness of K .
2.38 Theorem. If $\left\{I_{n}\right\}$ is a sequence of intervals in $\mathbb{R}^{1}$, such that $I_{n} \supset I_{n+1}$ ( $\mathrm{n}=1,2,3, \ldots$ ), then $\bigcap_{n=1}^{\infty} I_{n}$ is not empty.

Proof. If $I_{n}=\left[a_{n}, b_{n}\right]$, let $E$ be the set of all $a_{n}$. Then $E$ is nonempty and bounded above (by $b_{1}$ ). Let $x$ be the sup of $E$. If $m$ and $n$ are positive integers, then

$$
a_{n} \leq a_{m+n} \leq b_{m+n} \leq b_{m}
$$

so that $x \leq b_{m}$ for each $m$. Since it is obvious that $a_{m} \leq x$, we see that $x \in I_{m}$ for $\mathrm{m}=1,2,3, \ldots$
2.39 Theorem. Let k be a positive integer. If $\left\{I_{n}\right\}$ is a sequence of k -cells such that $\mathrm{I}_{n} \supset \mathrm{I}_{n+1}(\mathrm{n}=1,2,3, \ldots)$, then $\bigcap_{n=1}^{\infty} \mathrm{I}_{n}$ is not empty.

Proof. Let $I_{n}$ consist of all points $\mathbf{x}=\left\{\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{k}}\right\}$ such that

$$
a_{n, j} \leq x_{j} \leq b_{n, j} \quad(1 \leq j \leq k ; n=1,2,3, \ldots)
$$

and put $\mathrm{I}_{n, j}=\left[a_{n, j}, b_{n, j}\right]$. For each $j$, the collection $\left\{I_{n, j}\right\}$ satisfies the hypotheses of Theorem 2.38. Hence there are real numbers $x_{j}^{*}(1 \leq j \leq k)$ such that

$$
a_{n, j} \leq x_{j}^{*} \leq b_{n, j} \quad(1 \leq j \leq k ; n=1,2,3, \ldots)
$$

Setting $\mathbf{x}^{*}=\left\{\mathrm{x}_{1}^{*}, \ldots, \mathrm{x}_{\mathrm{k}}^{*}\right\}$, we see that $\mathbf{x}^{*} \in \mathrm{I}_{n}$ for $\mathrm{n}=1,2,3, \ldots$ The theorem follows.
2.40 Theorem. Every k -cell is compact.

Proof. Let I be a k-cell, consisting of all points $\mathbf{x}=\left(x_{1}, \ldots, x_{k}\right)$ such that $a_{j} \leq x_{j} \leq b_{j}(I \leq j \leq k)$. Put

$$
\delta=\left\{\sum_{I}^{k}\left(b_{j}-a_{j}\right)^{2}\right\}^{1 / 2}
$$

Then $|\mathbf{x}-\mathbf{y}| \leq \delta$, if $\mathbf{x} \in \mathrm{I}, \mathbf{y} \in \mathrm{I}$.
Suppose, to get a contradiction, that there exists an open cover $\left\{G_{\alpha}\right\}$ of I which contains no finite subcover of I. Put $c_{j}=\left(a_{j}+b_{j}\right) / 2$. The intervals $\left\{a_{j}, c_{j}\right\}$ and $\left\{c_{j}, b_{j}\right\}$ then determine $2^{k} k$-cells $Q_{i}$ whose union is $I$. At least one of these sets $Q_{i}$, call it $I_{I}$, cannot be covered by any finite subcollection of $\left\{G_{\alpha}\right\}$ (otherwise I could be so covered). We next subdivide $I_{I}$ and continue the process. We obtain a sequence $\left\{I_{n}\right\}$ with the following properties:
(a) $\mathrm{I} \supset \mathrm{I}_{1} \supset \mathrm{I}_{2} \supset \mathrm{I}_{3} \supset \cdots$;
(b) $\mathrm{I}_{n}$ is not covered by any finite subcollection of $\left\{G_{\alpha}\right\}$;
(c) If $\mathbf{x} \in \mathrm{I}_{n}$ and $\mathbf{y} \in \mathrm{I}_{n}$, then $|\mathbf{x}-\mathbf{y}| \leq 2^{-n} \delta$.

By (a) and Theorem 2.39, there is a point $\mathbf{x}^{*}$ which lies in every $\mathrm{I}_{n}$. For some $\alpha, \mathbf{x}^{*} \in G_{\alpha}$. Since $G_{\alpha}$ is open, there exists $r>0$ such that $\left|\mathbf{y}-\mathbf{x}^{*}\right|<r$ implies that $y \in G_{\alpha}$. If $n$ is so large that $2^{-n} \delta<r$ (there is such an $n$, for otherwise $2^{n} \leq \delta / r$ for all positive integers $n$, which is absurd since $\mathbb{R}$ is archimedean), then (c) implies that $\mathrm{I}_{n} \subset G_{\alpha}$, which contradicts (b).

This completes the proof.
The equivalence of (a) and (b) in the next theorem is known as the Heine-Borel theorem.
2.41 Theorem. If a set E in $\mathbb{R}^{\mathrm{k}}$ has one of the following three properties, then it has the other two:
(a) E is closed and bounded.
(b) E is compact.
(c) Every infinite subset of E has a limit point in E .

Proof. If (a) holds, then $E \subset I$ for some k-cell I, and (b) follows from Theorems 2.40 and 2.35. Theorem 2.37 shows that (b) implies (c). It remains to be shown that (c) implies (a).

If $E$ is not bounded, then $E$ contains points $\mathbf{x}_{n}$ with

$$
\left|\mathbf{x}_{n}\right|>n \quad(n=1,2,3, \ldots)
$$

The set $S$ consisting of these points $\mathbf{x}_{n}$ is infinite and clearly has no limit point in $\mathbb{R}^{\mathrm{k}}$, hence has none in E . Thus (c) implies that E is bounded.

If $E$ is not closed, then there is a point $\mathbf{x}_{0} \in \mathbb{R}^{\mathrm{k}}$ which is a limit point of $E$ but not a point of E. For $n=1,2,3, \ldots$, there are points $\mathbf{x}_{n} \in E$ such that $\left|\mathbf{x}_{n}-\mathbf{x}_{0}\right|<1 / n$.

Let $S$ be the set of these points $\mathbf{x}_{n}$. Then $S$ is infinite (otherwise $\left|\mathbf{x}_{n}-\mathbf{x}_{0}\right|$ would have a constant positive value, for infinitely many $n$ ), $S$ has $\mathbf{x}_{0}$ as a limit point, and $S$ has no other limit point in $\mathbb{R}^{\mathrm{k}}$. For if $\mathbf{y} \neq \mathbf{x}_{0}$, then

$$
\begin{aligned}
\left|\mathbf{x}_{n}-\mathbf{y}\right| & \geq\left|\mathbf{x}_{0}-\mathbf{y}\right|-\left|\mathbf{x}_{n}-\mathbf{x}_{0}\right| \\
& \geq\left|\mathbf{x}_{0}-\mathbf{y}\right|-\frac{1}{n} \geq \frac{1}{2}\left|\mathbf{x}_{0}-\mathbf{y}\right|
\end{aligned}
$$

for all but finitely many n ; this shows that $\mathbf{y}$ is not a limit point of $S$ (Theorem 2.20).
Thus $S$ has no limit point in E ; hence E must be closed if (c) holds.
We should remark, at this point, that (b) and (c) are equivalent in any metric space (Exercise 2.26), but that (a) does not, in general, imply (b) and (c). Examples are furnished by Exercise 2.16 and by the space $\mathscr{L}^{2}$, which is discussed in Chap. 11.
2.42 Theorem (Weierstrass). Every bounded infinite subset of $\mathbb{R}^{\mathrm{k}}$ has a limit point in $\mathbb{R}^{\mathrm{k}}$.

Proof. Being bounded, the set E in question is a subset of a k -cell $\mathrm{I} \subset \mathbb{R}^{\mathrm{k}}$. By Theorem 2.40, I is compact, and so E has a limit point in I, by Theorem 2.37.

# PERFECT SETS 

2.43 Theorem. Let P be a nonempty perfect set in $\mathbb{R}^{\mathrm{k}}$. Then P is uncountable.

Proof. Since P has limit points, P must be infinite. Suppose P is countable, and denote the points of P by $\mathbf{x}_{1}, \mathbf{x}_{2}, \mathbf{x}_{3}, \ldots$. We shall construct a countable collection $\left\{V_{n}\right\}$ of neighborhoods, as follows.

Let $V_{1}$ be any neighborhood of $\mathbf{x}_{1}$. If $V_{1}$ consists of all $\mathbf{y} \in \mathbb{R}^{\mathrm{k}}$ such that $\left|\mathbf{y}-\mathbf{x}_{1}\right|<\tau$, then closure $\overline{\mathrm{V}}_{1}$ of $\mathrm{V}_{1}$ is the set of all $\mathbf{y} \in \mathbb{R}^{\mathrm{k}}$ such that $\left|\mathbf{y}-\mathbf{x}_{1}\right| \leq \tau$.

Suppose $V_{n}$ has been constructed, so that $V_{n} \cap P$ is not empty. Since every point of $P$ is a limit point of $P$, there is a neighborhood $V_{n+1}$ such that (i) $\bar{V}_{n+1} \subset V_{n}$, (ii) $\mathbf{x}_{n} \notin \bar{V}_{n+1}$, (iii) $\bar{V}_{n+1} \cap P$ is not empty. By (iii), $V_{n+1}$ satisfies our induction hypothesis, and the construction can proceed.

Put $\mathrm{K}_{n}=\overline{\mathrm{V}}_{n} \cap \mathrm{P}$. Since $\overline{\mathrm{V}}_{n}$ is closed and bounded, $\overline{\mathrm{V}}_{n}$ is compact. Since $\mathbf{x}_{n} \notin$ $\mathrm{K}_{n+1}$, no point of P lies in $\bigcap_{n=1}^{\infty} \mathrm{K}_{n}$. Since $\mathrm{K}_{n} \subset \mathrm{P}$, this implies that $\bigcap_{n=1}^{\infty} \mathrm{K}_{n}$ is empty. But each $\mathrm{K}_{n}$ is nonempty, by (iii), and $\mathrm{K}_{n} \supset \mathrm{~K}_{n+1}$, by (i); this contradicts the Corollary to Theorem 2.36.

Corollary. Every interval $[\mathrm{a}, \mathrm{b}](\mathrm{a}<\mathrm{b})$ is uncountable. In particular, the set of all real numbers is uncountable.
2.44 The Cantor Set. The set which we are now going to construct shows that there exist perfect sets in $\mathbb{R}^{1}$ which contain no segment.

Let $\mathrm{E}_{0}$ be the interval $[0,1]$. Remove the segment $(1 / 3,2 / 3)$, and let $\mathrm{E}_{1}$ be the union of the intervals

$$
\left[0, \frac{1}{3}\right],\left[\frac{2}{3}, 1\right]
$$

Remove the middle thirds of these intervals, and let $\mathrm{E}_{2}$ be the union of the intervals

$$
\left[0, \frac{1}{\theta}\right],\left[\frac{2}{\theta}, \frac{3}{\theta}\right],\left[\frac{6}{\theta}, \frac{7}{\theta}\right],\left[\frac{8}{\theta}, 1\right]
$$

Continuing in this way, we obtain a sequence of compact sets $\mathrm{E}_{n}$ such that
(a) $\mathrm{E}_{1} \supset \mathrm{E}_{2} \supset \mathrm{E}_{3} \supset \cdots$;
(b) $\mathrm{E}_{n}$ is the union of $2^{n}$ intervals, each of length $3^{-n}$.

The set

$$
P=\bigcap_{n=1}^{\infty} E_{n}
$$

is called the Cantor set. P is clearly compact, and Theorem 2.36 shows that P is not empty.

No segment of the form

$$
\left(\frac{3 k+1}{3^{m}}, \frac{3 k+2}{3^{m}}\right)
$$

where k and m are positive integers, has a point in common with P . Since every segment $(\alpha, \beta)$ contains a segment of the form (2.24), if

$$
3^{-m}<\frac{\beta-\alpha}{6}
$$

P contains no segment.
To show that P is perfect, it is enough to show that P contains no isolated point. Let $x \in P$, and let $S$ be any segment containing $x$. Let $I_{n}$ be that interval of $E_{n}$ which contains x . Choose n large enough, so that $\mathrm{I}_{\mathrm{n}} \subset \mathrm{S}$. Let $\mathrm{x}_{\mathrm{n}}$ be an endpoint of $I_{n}$, such that $x_{n} \neq x$.

It follows from the construction of $P$ that $x_{n} \in P$. Hence $x$ is a limit point of $P$, and P is perfect.

One of the most interesting properties of the Cantor set is that it provides us with an example of an uncountable set of measure zero (the concept of measure will be discussed in Chap. 11).

# CONNECTED SETS 

2.45 Definition. Two subsets $A$ ad $B$ of a metric space $X$ are said to be separated if both $A \cap \bar{B}$ and $\bar{A} \cap B$ are empty, i.e., if no point of $A$ lies in the closure of $B$ and no point of B lies in the closure of A .

A set $E \subset X$ is said to be connected if $E$ is not a union of two nonempty separated sets.
2.46 Remark. Separated sets are of course disjoint, but disjoint sets need not be separated. For example, the interval $[0,1]$ and the segment $(1,2)$ are not separated, since 1 is a limit point of $(1,2)$. However, the segments $(0,1)$ and $(1,2)$ are separated.

The connected subsets of the line have a particularly simple structure:
2.47 Theorem. A subset $E$ of the real line $\mathbb{R}^{1}$ is connected if and only if it has the following property: If $x \in E, y \in E$, and $x<z<y$, then $z \in E$.

Proof. If there exist $x \in E, y \in E$, and some $z \in(x, y)$ such that $z \notin E$, then $E=A_{z} \cup B_{z}$ where

$$
A_{z}=E \cap(-\infty, z), \quad B_{z}=E \cap(z, \infty)
$$

Since $x \in A_{z}$ and $y \in B_{z}, A$ and $B$ are nonempty. Since $A_{z} \subset(-\infty, z)$ and $B_{z} \subset(z, \infty)$, they are separated. Hence $E$ is not connected.

To prove the converse, suppose $E$ is not connected. Then there are nonempty separated sets $A$ and $B$ such that $A \cup B=E$. Pick $x \in A, y \in B$, and assume (without loss of generality) that $x<y$. Define

$$
z=\sup (A \cap[x, y])
$$

By Theorem 2.28, $z \in \bar{A}$; hence $z \notin B$. In particular, $x \leq z<y$.
If $z \notin A$, it follows that $x<z<y$ and $z \notin E$.
If $z \in A$, then $z \notin \bar{B}$, hence there exists $z_{1}$ such that $z<z_{1}<y$ and $z_{1} \notin B$. Then $x<z_{1}<y$ and $z_{1} \notin E$.

# EXERCISES 

2.1. Prove that the empty set is a subset of every set.
2.2. A complex number $z$ is said to be algebraic if there are integers $a_{0}, \ldots, a_{n}$, not all zero, such that

$$
a_{0} z^{n}+a_{1} z^{n-1}+\cdots+a_{n-1} z+a_{n}=0
$$

Prove that the set of all algebraic numbers is countable. Hint: For every positive integer N there are only finitely many equations with

$$
n+\left|a_{0}\right|+\left|a_{1}\right|+\cdots+\left|a_{n}\right|=N
$$

2.3. Prove that there exist real numbers which are not algebraic.
2.4. Is the set of all irrational real numbers countable?
2.5. Construct a bounded set of real numbers with exactly three limit points.
2.6. Let $E^{\prime}$ be the set of all limit points of a set $E$. Prove that $E^{\prime}$ is closed. Prove that $E$ and $\bar{E}$ have the same limit points. (Recall that $\bar{E}=E \cup E^{\prime}$.) Do $E$ and $E^{\prime}$ always have the same limit points?

2.7. Let $A_{1}, A_{2}, A_{3}, \ldots$ be subsets of a metric space.
(a) If $B_{n}=\bigcup_{i=1}^{n} A_{i}$, prove that $\bar{B}_{n}=\bigcup_{i=1}^{n} \bar{A}_{i}$ for $n=1,2,3, \ldots$.
(b) If $B_{n}=\bigcup_{i=1}^{\infty} A_{i}$, prove that $\bar{B}_{n} \supset \bigcup_{i=1}^{\infty} \bar{A}_{i}$.

Show, by an example, that this inclusion can be proper.
2.8. Is every point of every open set $E \subset \mathbb{R}^{2}$ a limit point of $E$ ? Answer the same question for closed sets in $\mathbb{R}^{2}$.
2.9. Let $E^{\circ}$ denote the set of all interior points of a set $E$. [See Definition 2.18(e); $E^{\circ}$ is called the interior of E.]
(a) Prove that $E^{\circ}$ is always open.
(b) Prove that $E$ is open if and only if $E^{\circ}=E$.
(c) If $G \subset E$ and $G$ is open, prove that $G \subset E^{\circ}$.
(d) Prove that the complement of $E^{\circ}$ is the closure of the complement of $E$.
(e) Do $E$ and $\bar{E}$ always have the same interiors?
(f) Do $E$ and $E^{\circ}$ always have the same closures?
2.10. Let $X$ be an infinite set. For $p \in X$ and $q \in X$, define

$$
d(p, q)= \begin{cases}1 & \text { (if } p \neq q) \\ 0 & \text { (if } p=q)\end{cases}
$$

Prove that this is a metric. Which subsets of the resulting metric space are open? Which are closed? Which are compact?
2.11. For $x \in \mathbb{R}^{1}$ and $y \in \mathbb{R}^{1}$, define

$$
\begin{aligned}
& d_{1}(x, y)=(x-y)^{2} \\
& d_{2}(x, y)=\sqrt{|x-y|} \\
& d_{3}(x, y)=\left|x^{2}-y^{2}\right| \\
& d_{4}(x, y)=|x-2 y| \\
& d_{5}(x, y)=\frac{|x-y|}{1+|x-y|}
\end{aligned}
$$

Determine, for each of these, whether it is a metric or not.
2.12. Let $K \subset \mathbb{R}^{1}$ consist of 0 and the numbers $1 / n$ for $n=1,2,3, \ldots$ Prove that $K$ is compact directly from the definition (without using the Heine-Borel theorem).
2.13. Construct a compact set of real numbers whose limit points form a countable set.
2.14. Give an example of an open cover of the segment $(0,1)$ which has no finite subcover.
2.15. Show that Theorem 2.36 and its Corollary become false (in $\mathbb{R}^{1}$, for example) if the word "compact" is replaced by "closed" or by "bounded."
2.16. Regard $\mathbb{Q}$, the set of all rational numbers, as a metric space, with $d(p, q)=|p-q|$. Let $E$ be the set of all $p \in \mathbb{Q}$ such that $2<p^{2}<3$. Show that $E$ is closed and bounded in $\mathbb{Q}$, but that $E$ is not compact. Is $E$ open in $Q$ ?
2.17. Let $E$ be the set of all $x \in[0,1]$ whose decimal expansion contains only the digits 4 and 7. Is E countable? Is E dense in $[0,1]$ ? Is E compact? Is E perfect?
2.18. Is there a nonempty perfect set in $\mathbb{R}^{1}$ which contains no rational number?
2.19.
(a) If $A$ and $B$ are disjoint closed sets in some metric space $X$, prove that they are separated.
(b) Prove the same for disjoint open sets.

(c) Fix $p \in X, \delta>0$, define $A$ to be the set of all $q \in X$ for which $d(p, q)<\delta$, define $B$ similarly, with $>$ in place of $<$. Prove that $A$ and $B$ are separated.
(d) Prove that every connected metric space with at least two points is uncountable. Hint: Use (c).
2.20. Are closures and interiors of connected sets always connected? (Look at subsets of $\mathbb{R}^{2}$.)
2.21. Let $A$ and $B$ be separated subsets of some $\mathbb{R}^{k}$, suppose $\mathbf{a} \in A, \mathbf{b} \in B$, and define

$$
\mathbf{p}(\mathrm{t})=(1-\mathrm{t}) \mathbf{a}+\mathrm{t} \mathbf{b}
$$

for $t \in \mathbb{R}^{1}$. Put $A_{0}=\mathbf{p}^{-1}(A), B_{0}=\mathbf{p}^{-1}(B)$. [Thus $t \in A_{0}$ if and only if $\mathbf{p}(t) \in A$.]
(a) Prove that $A_{0}$ and $B_{0}$ are separated subsets of $\mathbb{R}^{1}$.
(b) Prove that there exists $t_{0} \in(0,1)$ such that $\mathbf{p}\left(t_{0}\right) \notin A \cup B$.
(c) Prove that every convex subset of $\mathbb{R}^{k}$ is connected.
2.22. A metric space is called separable if it contains a countable dense subset. Show that $\mathbb{R}^{k}$ is separable. Hint: Consider the set of points which have only rational coordinates.
2.23. A collection $\left\{V_{\alpha}\right\}$ of open subsets of $X$ is said to be a base for $X$ if the following is true: For every $x \in X$ and every open set $G \subset X$ such that $x \in G$, we have $x \in V_{\alpha} \subset G$ for some $\alpha$. In other words, every open set in $X$ is the union of a subcollection of $\left\{V_{\alpha}\right\}$.

Prove that every separable metric space has a countable base. Hint: Take all neighborhoods with rational radius and center in some countable dense subset of $X$.
2.24. Let $X$ be a metric space in which every infinite subset has a limit point. Prove that $X$ is separable. Hint: Fix $\delta>0$, and pick $x_{1} \in X$. Having chosen $x_{1}, \ldots, x_{i} \in X$, choose $x_{i+1} \in X$, if possible, so that $d\left(x_{i}, x_{i+1}\right) \geq \delta$ for $i=1, \ldots$, . Show that this process must stop after a finite number of steps, and that $X$ can therefore be covered by finitely many neighborhoods of radius $\delta$. Take $\delta=1 / n(n=1,2,3, \ldots)$, and consider the centers of the corresponding neighborhoods.
2.25. Prove that every compact metric space $K$ has a countable base, and that $K$ is therefore separable Hint: For every positive integer $n$, there are finitely many neighborhoods of radius $1 / n$ whose union covers $K$.
2.26. Let $X$ be a metric space in which every infinite subset has a limit point. Prove that $X$ is compact. Hint: By Exercises 2.23 and $2.24, X$ has a countable base. It follows that every open cover of $X$ has a countable subcover $\left\{G_{n}\right\}, n=1,2,3, \ldots$ If no finite subcollection of the $\left\{G_{n}\right\}$ covers $X$, then the complement $F_{n}$ of $G_{1} \cup \cdots \cup G_{n}$ is nonempty for each $n$, but $\bigcap_{n=1}^{\infty} F_{n}$ is empty. If $E$ is a set which contains a point from each $F_{n}$, consider a limit point of $E$, and obtain a contradiction.
2.27. Define a point $p$ in a metric space $X$ to be a condensation point of a set $E \subset X$ if every neighborhood of $p$ contains uncountably many points of $E$.

Suppose $E \subset \mathbb{R}^{k}, E$ is uncountable, and let $P$ be the set of all condensation points of $E$. Prove that $P$ is perfect and that at most countably many points of $E$ are not in $P$. In other words, show that $P^{c} \cap E$ is at most countable. Hint: Let $\left\{V_{n}\right\}$ be a countable base of $\mathbb{R}^{k}$, let $W$ be the union of those $V_{n}$ for which $E \cap V_{n}$ is at most countable, and show that $P=W^{c}$.
2.28. Prove that every closed set in a separable metric space is the union of a (possibly empty) perfect set and a set which is at most countable. (Corollary: Every countable closed set in $\mathbb{R}^{k}$ has isolated points.) Hint: Use Exercise 2.27.
2.29. Prove that every open set in $\mathbb{R}^{1}$ is the union of an at most countable collection of disjoint segments. Hint: Use Exercise 2.22.

2.30. Imitate the proof of Theorem 2.43 to obtain the following result:

If $\mathbb{R}^{\mathrm{k}}=\bigcup_{n=1}^{\infty} \mathrm{F}_{n}$, where each $\mathrm{F}_{n}$ is a closed subset of $\mathbb{R}^{\mathrm{k}}$, then at least one $\mathrm{F}_{n}$ has a nonempty interior.
Equivalent statement: If $G_{n}$ is a dense open subset of $\mathbb{R}^{k}$ for $n=1,2,3, \ldots$, then $\bigcap_{n=1}^{\infty} G_{n}$ is not empty (in fact, it is dense in $\mathbb{R}^{k}$ ).
(This is a special case of Baire's theorem; see Exercise 3.22 for the general case.)

# Chapter 3 

## NUMERICAL SEQUENCES AND SERIES

As the title indicates, this chapter will deal primarily with sequences and series of complex numbers. The basic facts about convergence, however, are just as easily explained in a more general setting. The first three sections will therefore be concerned with sequences in euclidean spaces, or even in metric spaces.

## CONVERGENT SEQUENCES

3.1 Definition. A sequence $\left(p_{n}\right)$ in a metric space $X$ is said to converge if there is a point $\mathrm{p} \in \mathrm{X}$ with the following property: For every $\varepsilon>0$ there is an integer N such that $\mathrm{n} \geq \mathrm{N}$ implies that $\mathrm{d}\left(\mathrm{p}_{\mathrm{n}}, \mathrm{p}\right)<\varepsilon$. (Here d denotes the distance in X .)

In this case, we also say that $\left(p_{n}\right)$ converges to $p$, or that $p$ is the limit of $\left(p_{n}\right)$ [see Theorem 3.2(b), and we write $\mathrm{p}_{\mathrm{n}} \rightarrow \mathrm{p}$, or

$$
\lim _{n \rightarrow \infty} p_{n}=p
$$

If $\left(p_{n}\right)$ does not converge, it is said to diverge.
It might be well to point out that our definition of "convergent sequence" depends not only on $\left(p_{n}\right)$ but also on $X$; for instance, the sequence $(1 / n)$ converges in $\mathbb{R}^{1}$ (to 0 ), but fails to converge in the set of all positive real numbers [with $\mathrm{d}(\mathrm{x}, \mathrm{y})=|\mathrm{x}-\mathrm{y}|]$. In cases of possible ambiguity, we can be more precise and specify "convergent in X" rather that "convergent."

We recall that the set of points $\mathrm{p}_{n}(\mathrm{n}=1,2,3, \ldots)$ is the range of $\left(\mathrm{p}_{\mathrm{n}}\right)$. The range of a sequence may be a finite set, or it may be infinite. The sequence $\left(p_{n}\right)$ is said to be bounded if its range is bounded.

As examples, consider the following sequences of complex numbers (that is, $\left.X=\mathbb{R}^{2}\right):$

(a) If $s_{n}=1 / n$, then $\lim _{n \rightarrow \infty} s_{n}=0$; the range is infinite, and the sequence is bounded.
(b) If $s_{n}=n^{2}$, the sequence $s_{n}$ is unbounded, is divergent, and has infinite range.
(c) If $s_{n}=1+\left[(-1)^{n} / n\right]$, the sequence $\left(s_{n}\right)$ converges to 1 , is bounded, and has infinite range.
(d) If $s_{n}=i^{n}$, the sequence $\left(s_{n}\right)$ is divergent, is bounded, and has finite range.
(e) If $s_{n}=1(n=1,2,3, \ldots)$, then $\left(s_{n}\right)$ converges to 1 , is bounded, and has finite range.

We now summarize some important properties of convergent sequences in metric spaces.
3.2 Theorem. Let $\left(p_{n}\right)$ be a sequence in a metric space $X$.
(a) $\left(p_{n}\right)$ converges to $p \in X$ if and only if every neighborhood of $p$ contains $p_{n}$ for all but finitely many n .
(b) If $p \in X, p^{\prime} \in X$, and if $\left(p_{n}\right)$ converges to $p$ and to $p^{\prime}$, then $p^{\prime}=p$.
(c) If $\left(p_{n}\right)$ converges, then $\left(p_{n}\right)$ is bounded.
(d) If $E \subset X$ and if $p$ is a limit point of $E$, then there is a sequence $\left(p_{n}\right)$ in $E$ such that $\mathrm{p}=\lim _{n \rightarrow \infty} \mathrm{p}_{n}$.
Proof.
(a) Suppose $p_{n} \rightarrow p$ and let $V$ be a neighborhood of $p$. For some $\varepsilon>0$, the conditions $d(q, p)<\varepsilon, q \in X$ imply $q \in V$. Corresponding to this $\varepsilon$, there exists $N$ such that $n \geq N$ implies $d\left(p_{n}, p\right)<\varepsilon$. Thus $n \geq N$ implies $p_{n} \in V$.

Conversely, suppose every neighborhood of $p$ contains all but finitely many of the $p_{n}$. Fix $\varepsilon>0$ and let $V$ be the set of all $q \in X$ such that $d(p, q)<$ $\varepsilon$. By assumption, there exists $N$ (corresponding to this $V$ ) such that $p_{n} \in V$ if $n \geq N$. Thus $d\left(p_{n}, p\right)<\varepsilon$ if $n \geq N$; hence $p_{n} \rightarrow p$.
(b) Let $\varepsilon>0$ be given. There exist integers $N, N^{\prime}$ such that

$$
\begin{array}{lll}
n \geq N & \text { implies } & d\left(p_{n}, p\right)<\frac{\varepsilon}{2} \\
n \geq N^{\prime} & \text { implies } & d\left(p_{n}, p^{\prime}\right)<\frac{\varepsilon}{2}
\end{array}
$$

Hence if $n \geq \max \left\{N, N^{\prime}\right\}$, we have

$$
d\left(p, p^{\prime}\right) \leq d\left(p, p_{n}\right)+d\left(p_{n}, p^{\prime}\right)<\varepsilon
$$

Since $\varepsilon$ was arbitrary, we conclude that $d\left(p, p^{\prime}\right)=0$.
(c) Suppose $p_{n} \rightarrow p$. Then there is an integer $N$ such that $n>N$ implies $d\left(p_{n}, p\right)<1$. Put

$$
r=\max \left\{1, d\left(p_{1}, p\right), \ldots, d\left(p_{N}, p\right)\right\}
$$

Then $d\left(p_{n}, p\right) \leq r$ for $n=1,2,3, \ldots$

(d) For each positive integer $n$, there is a point $p_{n} \in E$ such that $d\left(p_{n}, p\right)<1 / n$. Given $\varepsilon>0$, choose N so that $\mathrm{N} \varepsilon>1$. If $\mathrm{n}>\mathrm{N}$, it follows that $\mathrm{d}\left(\mathrm{p}_{\mathrm{n}}, \mathrm{p}\right)<\varepsilon$. Hence $\mathrm{p}_{\mathrm{n}} \rightarrow \mathrm{p}$.

This completes the proof.
For sequences in $\mathrm{Et}^{\mathrm{k}}$ we can study the relation between congruence, on the one hand, and the algebraic operations on the other. We first consider sequences of complex numbers.
3.3 Theorem. Suppose $\left(s_{n}\right),\left(t_{n}\right)$ are complex sequences and $\lim _{n \rightarrow \infty} s_{n}=s, \lim _{n \rightarrow \infty} t_{n}=$ t. Then
(a) $\lim _{n \rightarrow \infty}\left(s_{n}+t_{n}\right)=s+t$;
(b) $\lim _{n \rightarrow \infty} c s_{n}=c s, \lim _{n \rightarrow \infty}\left(c+s_{n}\right)=c+s$ for any number $c$;
(c) $\lim _{n \rightarrow \infty} s_{n} t_{n}=s t$;
(d) $\lim _{n \rightarrow \infty}\left(1 / s^{n}\right)=1 / s$, provided $s_{n} \neq 0(n=1,2,3, \ldots)$ and $s \neq 0$.

Proof.
(a) Given $\varepsilon>0$, there exist integers $\mathrm{N}_{1}, \mathrm{~N}_{2}$ such that

$$
\begin{array}{ll}
n \geq N_{1} & \text { implies } \quad\left|s_{n}-s\right|<\frac{\varepsilon}{2} \\
n \geq N_{2} & \text { implies } \quad\left|t_{n}-t\right|<\frac{\varepsilon}{2}
\end{array}
$$

If $\mathrm{N}=\max \left\{\mathrm{N}_{1}, \mathrm{~N}_{2}\right\}$, then $\mathrm{n} \geq \mathrm{N}$ implies

$$
\left|\left(s_{n}+t_{n}\right)-(s+t)\right| \leq\left|s_{n}-s\right|+\left|t_{n}-t\right|<\varepsilon
$$

This proves (a). The proof of (b) is trivial.
(c) We use the identity

$$
s_{n} t_{n}-s t=\left(s_{n}-s\right)\left(t_{n}-t\right)+s\left(t_{n}-t\right)+t\left(s_{n}-s\right)
$$

Given $\varepsilon>0$, there are integers $\mathrm{N}_{1}, \mathrm{~N}_{2}$ such that

$$
\begin{array}{lll}
n \geq N_{1} & \text { implies } & \left|s_{n}-s\right|<\sqrt{\varepsilon} \\
n \geq N_{2} & \text { implies } & \left|t_{n}-t\right|<\sqrt{\varepsilon}
\end{array}
$$

If we take $\mathrm{N}=\max \left\{\mathrm{N}_{1}, \mathrm{~N}_{2}\right\}, \mathrm{n} \geq \mathrm{N}$ implies

$$
\left|\left(s_{n}-s\right)\left(t_{n}-t\right)\right|<\varepsilon
$$

so that

$$
\lim _{n \rightarrow \infty}\left(s_{n}-s\right)\left(t_{n}-t\right)=0
$$

We now apply (a) and (b) to (3.1) and conclude that

$$
\lim _{n \rightarrow \infty}\left(s_{n} t_{n}-s t\right)=0
$$

(d) Choosing $m$ such that $\left|s_{n}-s\right|<|s| / 2$ if $n \geq m$, we see that

$$
\left|s_{n}\right|>\frac{1}{2}|s| \quad(n \geq m)
$$

Give $\varepsilon>0$, there is an integer $N>m$ such that $n \geq N$ implies

$$
\left|s_{n}-s\right|<\frac{1}{2}|s|^{2} \varepsilon
$$

Hence, for $n \geq N$,

$$
\left|\frac{1}{s_{n}}-\frac{1}{s}\right|=\left|\frac{s_{n}-s}{s_{n} s}\right|<\frac{2}{|s|^{2}}\left|s_{n}-s\right|<\varepsilon
$$

# 3.4 Theorem. 

(a) Suppose $\mathbf{x}_{n} \in \mathbb{R}^{\mathrm{k}}(\mathrm{n}=1,2,3, \ldots)$ and

$$
\mathbf{x}_{n}=\left(\alpha_{1, n}, \ldots, \alpha_{k, n}\right)
$$

Then $\left(\mathbf{x}_{n}\right)$ converges to $\mathbf{x}=\left(\alpha_{1}, \ldots, \alpha_{k}\right)$ if and only if

$$
\lim _{n \rightarrow \infty} \alpha_{j, n}=\alpha_{j} \quad(1 \leq j \leq k)
$$

(b) Suppose $\left(\mathbf{x}_{n}\right),\left(\mathbf{y}_{n}\right)$ are sequences in $\mathbb{R}^{\mathrm{k}},\left(\beta_{n}\right)$ is a sequence of real numbers, and $\mathbf{x}_{n} \rightarrow \mathbf{x}, \mathbf{y}_{n} \rightarrow \mathbf{y}, \beta_{n} \rightarrow \beta$. Then

$$
\lim _{n \rightarrow \infty}\left(\mathbf{x}_{n}+\mathbf{y}_{n}\right)=\mathbf{x}+\mathbf{y}, \quad \lim _{n \rightarrow \infty} \mathbf{x}_{n} \cdot \mathbf{y}_{n}=\mathbf{x} \cdot \mathbf{y}, \quad \lim _{n \rightarrow \infty} \beta_{n} \mathbf{x}_{n}=\beta \mathbf{x}
$$

Proof.
(a) If $\mathbf{x}_{n} \rightarrow \mathbf{x}$, the inequalities

$$
\left|\alpha_{j, n}-\alpha_{j}\right| \leq\left|\mathbf{x}_{n}-\mathbf{x}\right|
$$

which follow immediately from the definition of the norm in $\mathbb{R}^{\mathrm{k}}$, show that (3.2) holds.

Conversely, if (3.2) holds, then to each $\varepsilon>0$, there corresponds an integer N such that $\mathrm{n} \geq \mathrm{N}$ implies

$$
\left|\alpha_{j, n}-\alpha_{j}\right|<\frac{\varepsilon}{\sqrt{k}} \quad(1 \leq j \leq k)
$$

Hence $\mathrm{n} \geq \mathrm{N}$ implies

$$
\left|\mathbf{x}_{\mathrm{n}}-\mathbf{x}\right|=\left\{\sum_{\mathrm{j}=1}^{\mathrm{k}}\left|\alpha_{\mathrm{j}, \mathrm{n}}-\alpha_{\mathrm{j}}\right|^{2}\right\}^{1 / 2}<\varepsilon
$$

so that $\mathbf{x}_{\mathrm{n}} \rightarrow \mathbf{x}$. This proves (a).
Part (b) follows from (a) and Theorem 3.3.

# SUBSEQUENCES 

3.5 Definition. Given a sequence $\left(p_{n}\right)$, consider a sequence $\left(n_{k}\right)$ of positive integers such that $n_{1}<n_{2}<n_{3}<\cdots$. Then the sequence $\left(p_{n_{i}}\right)$ is called a subsequence of $\left(p_{n}\right)$. If $\left(p_{n_{i}}\right)$ converges, its limit is called it subsequential limit of $\left(p_{n}\right)$.

It is clear that $\left(p_{n}\right)$ converges to $p$ if and only if every subsequence of $\left(p_{n}\right)$ converges to $p$. We leave the details of the proof to the reader.

### 3.6 Theorem.

(a) If $\left(\mathrm{p}_{\mathrm{n}}\right)$ is a sequence in a compact metric space X , then some subsequence of $\left(\mathrm{p}_{\mathrm{n}}\right)$ converges to a point of X .
(b) Every bounded sequence in $\mathbb{R}^{\mathrm{k}}$ contains a convergent subsequence.

Proof.
(a) Let $E$ be the range of $\left(p_{n}\right)$. If $E$ is finite then there is a $p \in E$ and a sequence $\left(n_{i}\right)$ with $n_{1}<n_{2}<n_{3}<\cdots$ such that

$$
p_{n_{1}}=p_{n_{2}}=\cdots=p
$$

The subsequence $\left(\mathrm{p}_{\mathrm{n}_{\mathrm{i}}}\right)$ so obtained converges evidently to p .
If $E$ is infinite, Theorem 2.37 shows that $E$ has a limit point $p \in X$. Choose $n_{1}$ so that $d\left(p, p_{n_{1}}\right)<1$. Having chosen $n_{1}, \ldots, n_{i-1}$, we see from Theorem 2.20 that there is an integer $n_{i}>n_{i-1}$ such that $d\left(p, p_{n_{i}}\right)<1 / i$. Then $\left(p_{n_{i}}\right)$ converges to $p$.
(b) This follows from (a) since Theorem 2.41 implies that every bounded subset of $\mathbb{R}^{\mathrm{k}}$ lies in a compact subset of $\mathbb{R}^{\mathrm{k}}$.
3.7 Theorem. The subsequential limits of a sequence $\left(\mathrm{p}_{\mathrm{n}}\right)$ in a metric space form a closed subset of X .

Proof. Let $E^{*}$ be the set of all subsequential limits of $\left(p_{n}\right)$ and let $q$ be a limit point of $E^{*}$. We have to show that $q \in E^{*}$.

Choose $n_{1}$ so that $p_{n_{1}} \neq q$. (If no such $n_{1}$ exists, then $E^{*}$ has only one point, and there is nothing to prove.) Put $\delta=\mathrm{d}\left(\mathrm{q}, \mathrm{p}_{\mathrm{n}_{1}}\right)$. Suppose $\mathrm{n}_{1}, \ldots, \mathrm{n}_{\mathrm{i}-1}$ are chosen. Since $q$ is a limit point of $E^{*}$, there is an $x \in E^{*}$ with $d(x, q)<2^{-i} \delta$. Since $x \in E^{*}$, there is an $n_{i}>n_{i-1}$ such that $d\left(x, p_{n_{i}}\right)<2^{-i} \delta$. Thus

$$
\mathrm{d}\left(\mathrm{q}, \mathrm{p}_{\mathrm{n}_{\mathrm{i}}}\right) \leq 2^{1-\mathrm{i}} \delta
$$

for $\mathrm{i}=1,2,3, \ldots$ This says that $\left(\mathrm{p}_{\mathrm{n}_{\mathrm{i}}}\right)$ converges to q . Hence $\mathrm{q} \in \mathrm{E}^{*}$.

# CAUCHY SEQUENCES 

3.8 Definition. A sequence $\left(p_{n}\right)$ in a metric space $X$ is said to be a Cauchy sequence if for every $\varepsilon>0$ there is an integer $N$ such that $d\left(p_{n}, p_{m}\right)<\varepsilon$ if $n \geq N$ and $m \geq N$.

In our discussion of Cauchy sequences, as well as other situations which will arise later, the following geometric concept will be useful.
3.9 Definition. Let $E$ be a nonempty subset of a metric space $X$ and let $S$ be the set of all real numbers of the form $d(p, q)$ with $p \in E$ and $q \in E$. The sup of $S$ is called the diameter of E .

If $\left(p_{n}\right)$ is a sequence in $X$ and if $E_{N}$ consists of the points $p_{N}, p_{N+1}, p_{N+2}, \ldots$, it is clear from the two preceding definitions that $\left(p_{n}\right)$ is a Cauchy sequence if and only if

$$
\lim _{N \rightarrow \infty} \operatorname{diam} E_{N}=0
$$

### 3.10 Theorem.

(a) If $\overline{\mathrm{E}}$ is the closure of a set E in a metric space X , then

$$
\operatorname{diam} \overline{\mathrm{E}}=\operatorname{diam} \mathrm{E}
$$

(b) If $\mathrm{K}_{\mathrm{n}}$ is a sequence of compact sets in X such that $\mathrm{K}_{\mathrm{n}} \supset \mathrm{K}_{\mathrm{n}+1}(\mathrm{n}=1,2,3, \ldots)$ and if

$$
\lim _{n \rightarrow \infty} \operatorname{diam} K_{n}=0
$$

then $\bigcap_{n=1}^{\infty} K_{n}$ consists of exactly one point.
Proof.
(a) Since $E \subset \bar{E}$, it is clear that

$$
\operatorname{diam} E \leq \operatorname{diam} \bar{E}
$$

Fix $\varepsilon>0$, and choose $p \in \overline{\mathrm{E}}, \mathrm{q} \in \overline{\mathrm{E}}$. By the definition of $\overline{\mathrm{E}}$, there are points $\mathrm{p}^{\prime}, \mathrm{q}^{\prime}$ in E such that $\mathrm{d}\left(\mathrm{p}, \mathrm{p}^{\prime}\right)<\varepsilon, \mathrm{d}\left(\mathrm{q}, \mathrm{q}^{\prime}\right)<\varepsilon$. Hence

$$
\begin{aligned}
\mathrm{d}(\mathrm{p}, \mathrm{q}) & \leq \mathrm{d}\left(\mathrm{p}, \mathrm{p}^{\prime}\right)+\mathrm{d}\left(\mathrm{p}^{\prime}, \mathrm{q}^{\prime}\right)+\mathrm{d}\left(\mathrm{q}^{\prime}, \mathrm{q}\right) \\
& <2 \varepsilon+\mathrm{d}\left(\mathrm{p}^{\prime}, \mathrm{q}^{\prime}\right) \leq 2 \varepsilon+\operatorname{diam} \mathrm{E}
\end{aligned}
$$

It follows that

$$
\operatorname{diam} \overline{\mathrm{E}} \leq 2 \varepsilon+\operatorname{diam} \mathrm{E}
$$

and since $\varepsilon$ was arbitrary, (a) is proved.
(b) Put $\mathrm{K}=\bigcap_{n=1}^{\infty} \mathrm{K}_{n}$. By Theorem 2.36, K is not empty. If K contains more than one point, then diam $\mathrm{K}>0$. But for each $\mathrm{n}, \mathrm{K}_{\mathrm{n}} \supset \mathrm{K}$ so that diam $\mathrm{K}_{\mathrm{n}} \geq$ diam K. This contradicts the assumption that diam $\mathrm{K}_{\mathrm{n}} \rightarrow 0$.

# 3.11 Theorem. 

(a) In any metric space X , every convergent sequence is a Cauchy sequence.
(b) If X is a compact metric space and if $\left(\mathrm{p}_{n}\right)$ is a Cauchy sequence in X , then $\left(\mathrm{p}_{n}\right)$ converges to some point of X .
(c) In $\mathbb{R}^{\mathrm{k}}$, every Cauchy sequence converges.

Note: The difference between the definition of convergence and the definition of a Cauchy sequence is that the limit is explicitly involved in the former, but not in the latter. Thus Theorem 3.11(b) may enable us to decide whether or not a given sequence converges without knowledge of the limit to which it may converge.

The fact (contained in Theorem 3.11) that a sequence converges in $\mathbb{R}^{\mathrm{k}}$ if and only if it is a Cauchy sequence is usually called the Cauchy criterion for convergence.

Proof.
(a) If $\mathrm{p}_{n} \rightarrow \mathrm{p}$ and if $\varepsilon>0$, there is an integer N such that $\mathrm{d}\left(\mathrm{p}, \mathrm{p}_{n}\right)<\varepsilon$ for all $\mathrm{n} \geq \mathrm{N}$. Hence

$$
\mathrm{d}\left(\mathrm{p}_{\mathrm{n}}, \mathrm{p}_{\mathrm{m}}\right) \leq \mathrm{d}\left(\mathrm{p}_{\mathrm{n}}, \mathrm{p}\right)+\mathrm{d}\left(\mathrm{p}, \mathrm{p}_{\mathrm{m}}\right)<2 \varepsilon
$$

as soon as $\mathrm{n} \geq \mathrm{N}$ and $\mathrm{n} \geq \mathrm{N}$. Thus $\left(\mathrm{p}_{\mathrm{n}}\right)$ is a Cauchy sequence.
(b) Let $\left(\mathrm{p}_{\mathrm{n}}\right)$ be a Cauchy sequence in the compact space X . For $\mathrm{N}=1,2,3, \ldots$, let $\mathrm{E}_{\mathrm{N}}$ be the set consisting of $\mathrm{p}_{\mathrm{N}}, \mathrm{p}_{\mathrm{N}+1}, \mathrm{p}_{\mathrm{N}+2}, \ldots$. Then

$$
\lim _{\mathrm{N} \rightarrow \infty} \operatorname{diam} \overline{\mathrm{E}}_{\mathrm{N}}=0
$$

by Definition 3.9 and Theorem 3.10(a). Being a closed subset of a compact space X , each $\overline{\mathrm{E}}_{\mathrm{N}}$ is compact (Theorem 2.35). Also, $\mathrm{E}_{\mathrm{N}} \supset \mathrm{E}_{\mathrm{N}+1}$, so that $\overline{\mathrm{E}}_{\mathrm{N}} \supset \overline{\mathrm{E}}_{\mathrm{N}+1}$.

Theorem 3.10(b) shows now that there is a unique $\mathrm{p} \in \mathrm{X}$ which lies in every $\bar{E}_{\mathrm{N}}$.

Let $\varepsilon>0$ be given. By (3.3) there is an integer $N_{0}$ such that $\operatorname{diam} \bar{E}_{N}<\varepsilon$ if $N \geq N_{0}$. Since $p \in \bar{E}_{N}$, it follows that $d(p, q)<\varepsilon$ for every $q \in \bar{E}_{N}$, hence for every $q \in E_{N}$. In other words, $d\left(p, p_{n}\right)<\varepsilon$ if $n \geq N_{0}$. This says precisely that $p_{n} \rightarrow p$.
(c) Let $\left(\mathbf{x}_{n}\right)$ be a Cauchy sequence in $\mathbb{R}^{\mathrm{k}}$. Define $\mathrm{E}_{\mathrm{N}}$ as in (b), with $\mathbf{x}_{\mathrm{i}}$ in place of $p_{i}$. For some $N$, diam $E_{N}<1$. The range of $\left(\mathbf{x}_{n}\right)$ is the union of $E_{N}$ and the finite set $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{N-1}\right\}$. Hence $\left(\mathbf{x}_{n}\right)$ is bounded. Since every bounded subset of $\mathbb{R}^{\mathrm{k}}$ has compact closure in $\mathbb{R}^{\mathrm{k}}$ (Theorem 2.41), (c) follows from (b).
3.12 Definition. A metric space in which every Cauchy sequence converges is said to be complete

Thus Theorem 3.11 says that all compact metric spaces and all euclidean spaces are complete. Theorem 3.11 implies also that every closed subset E of a complete metric space X is complete. (Every Cauchy sequence in E is a Cauchy sequence in X , hence it converges to some $\mathrm{p} \in \mathrm{X}$, and actually $\mathrm{p} \in \mathrm{E}$ since E is closed.) An example of a metric space which is not complete is the space of all rational numbers with $\mathrm{d}(\mathrm{x}, \mathrm{y})=|\mathrm{x}-\mathrm{y}|$.

Theorem 3.2(c) and example (d) after Definition 3.1 show that convergent sequences are bounded, but that bounded sequences in $\mathbb{R}^{\mathrm{k}}$ need not converge. However, there is one important case in which convergence is equivalent to boundedness; this happens for monotonic sequences in $\mathbb{R}^{1}$.
3.13 Definition. A sequence $\left(s_{n}\right)$ of real numbers is said to be
(a) monotonically increasing if $s_{n} \leq s_{n+1}(n=1,2,3, \ldots)$;
(b) monotonically decreasing if $s_{n} \geq s_{n+1}(n=1,2,3, \ldots)$.

The class of monotonic sequences consists of the increasing and decreasing sequences.
3.14 Theorem. Suppose $\left(s_{n}\right)$ is monotonic. Then $\left(s_{n}\right)$ converges if and only if it is bounded.

Proof. Suppose $s_{n} \leq s_{n+1}$ (the proof is analogous in the other case). Let $E$ be the range of $\left(s_{n}\right)$. If $\left(s_{n}\right)$ is bounded, let $s$ be the upper bound of $E$. Then

$$
s_{n} \leq s \quad(n=1,2,3, \ldots)
$$

For every $\varepsilon>0$, there is an integer $N$ such that

$$
s-\varepsilon<s_{N} \leq s
$$

for otherwise $s-\varepsilon$ would be an upper bound of $E$. Since $\left(s_{n}\right)$ increases $n \geq N$ therefore implies

$$
s-\varepsilon<s_{n} \leq s
$$

which shows that $\left(s_{n}\right)$ converges (to $s$ ).
The converse follows from Theorem 3.2(c).

# UPPER AND LOWER LIMITS 

3.15 Definition. Let $\left(s_{n}\right)$ be a sequence of real numbers with the following property: For every real $M$ there is an integer $N$ such that $n \geq N$ implies $s_{n} \geq M$. We then write

$$
s_{n} \rightarrow+\infty
$$

Similarly, if for every real $M$ there exists an integer $N$ such that $n \geq N$ implies $s_{n} \leq M$, we write

$$
s_{n} \rightarrow-\infty
$$

It should be noted that we now use the symbol $\rightarrow$ (introduced in Definition 3.1) for certain types of divergent sequences, as well as for convergent sequences, but that the definitions of convergence and of limit, given in Definition 3.1 are unchanged.
3.16 Definition. Let $\left(s_{n}\right)$ be a sequence of real numbers. Let $E$ be the set of numbers $x$ (in the extended real number system) such that $s_{n_{k}} \rightarrow x$ for some subsequence $\left(s_{n_{k}}\right)$. This set $E$ contains all subsequential limits as defined in Definition 3.5, plus possibly the numbers $+\infty,-\infty$.

We now recall Definitions 1.8 and 1.23 and put

$$
\begin{aligned}
& s^{*}=\sup E, \\
& s_{*}=\inf E .
\end{aligned}
$$

The numbers $s^{*}, s_{*}$ are called the upper and lower limits of $\left(s_{n}\right)$; we use the notation

$$
\limsup _{n \rightarrow \infty} s_{n}=s^{*}, \quad \liminf _{n \rightarrow \infty} s_{n}=s_{*}
$$

3.17 Theorem. Let $\left(s_{n}\right)$ be a sequence of real numbers. Let E and $s^{*}$ have the same meaning as in Definition 3.16. Then $s^{*}$ has the following two properties:
(a) $s^{*} \in E$.
(b) If $x>s^{*}$, there is an integer N such that $n \geq N$ implies $s_{n}<x$.

Moreover, $s^{*}$ is the only number with the properties (a) and (b).
Of course, an analogous result is true for $s_{*}$.
Proof.
(a) If $s^{*}=+\infty$, then $E$ is not bounded above; hence $\left(s_{n}\right)$ is not bounded above, and there is a subsequence $\left(s_{n_{k}}\right)$ such that $s_{n_{k}} \rightarrow+\infty$.

If $s^{*}$ is real, then $E$ is bounded above, and at least one subsequential limit exists, so that (a) follows from Theorems 3.7 and 2.28.

If $s^{*}=-\infty$, then $E$ contains only one element, namely $-\infty$, and there is no subsequential limit. Hence, for any real $M, s_{n}>M$ for at most a finite number of values of $n$, so that $s_{n} \rightarrow-\infty$.

This establishes (a) in all cases.
(b) Suppose there is a number $x>s^{*}$ such that $s_{n} \geq x$ for infinitely many values of $n$. In that case, there is a number $y \in E$ such that $y \geq x>s^{*}$, contradicting the definition of $s^{*}$.

Thus $s^{*}$ satisfies (a) and (b). To show the uniqueness, suppose there are two numbers, $p$ and $q$, which satisfy (a) and (b), and suppose $p<q$. Choose $x$ such that $\mathrm{p}<\mathrm{x}<\mathrm{q}$. Since p satisfies (b), we have $s_{n}<\mathrm{x}$ for $\mathrm{n} \geq \mathrm{N}$. But then q cannot satisfy (a).

# 3.18 Examples. 

(a) Let $\left(s_{n}\right)$ be a sequence containing all rationals. Then every real number is a subsequential limit, and

$$
\limsup _{n \rightarrow \infty} s_{n}=+\infty, \quad \liminf _{n \rightarrow \infty} s_{n}=-\infty
$$

(b) Let $s_{n}=(-1)^{n} /[1+(1 / n)]$. Then

$$
\limsup _{n \rightarrow \infty} s_{n}=1, \quad \liminf _{n \rightarrow \infty} s_{n}=-1
$$

(c) For a real-valued sequence $\left\{s_{n}\right\}, \lim _{n \rightarrow \infty} s_{n}=s$ if and only if

$$
\limsup _{n \rightarrow \infty} s_{n}=\liminf _{n \rightarrow \infty} s_{n}=s
$$

We close this section with a theorem which is useful and whose proof is quite trivial:
3.19 Theorem. If $s_{n} \leq t_{n}$ for $n \geq N$, where $N$ is fixed, then

$$
\begin{aligned}
& \liminf _{n \rightarrow \infty} s_{n} \leq \liminf _{n \rightarrow \infty} t_{n} \\
& \limsup _{n \rightarrow \infty} s_{n} \leq \limsup _{n \rightarrow \infty} t_{n}
\end{aligned}
$$

## SOME SPECIAL SEQUENCES

We shall now compute the limits of some sequences which occur frequently. The proofs will all be based on the following remark: If $0 \leq x_{n} \leq s_{n}$ for $n \geq N$, where $N$ is some fixed number, and if $s_{n} \rightarrow 0$, then $x_{n} \rightarrow 0$.

# 3.20 Theorem. 

(a) If $\mathrm{p}>0$, then $\lim _{n \rightarrow \infty} 1 / n^{p}=0$.
(b) If $\mathrm{p}>0$, then $\lim _{n \rightarrow \infty} \sqrt[n]{p}=1$.
(c) $\lim _{n \rightarrow \infty} \sqrt[n]{n}=1$.
(d) If $\mathrm{p}>0$ and $\alpha$ is real, then $\lim _{n \rightarrow \infty} n^{\alpha} /(1+p)^{n}=0$.
(e) If $|x|<1$, then $\lim _{n \rightarrow \infty} x^{n}=0$.

Proof.
(a) Take $n>(1 / \varepsilon)^{1 / p}$. (Note that the archimedean property of the real number system is used here.)
(b) If $\mathrm{p}>1$, put $\mathrm{x}_{\mathrm{n}}=\sqrt[n]{\mathrm{p}}-1$. Then $\mathrm{x}_{\mathrm{n}}>0$ and, by the binomial theorem,

$$
1+n x_{n} \leq\left(1+x_{n}\right)^{n}=p
$$

so that

$$
0<x_{n} \leq \frac{p-1}{n}
$$

Hence $x_{n} \rightarrow 0$. If $p=1$, (b) is trivial, and if $0<p<1$, the result is obtained by taking reciprocals.
(c) Put $x_{n}=\sqrt[n]{n}-1$. Then $x_{n} \geq 0$ and, by the binomial theorem,

$$
n=\left(1+x_{n}\right)^{n} \geq \frac{n(n-1)}{2} x_{n}^{2}
$$

Hence

$$
0 \leq x_{n} \leq \sqrt{\frac{2}{n-1}} \quad(n \geq 2)
$$

(d) Let $k$ be an integer such that $k>\alpha, k>0$. For $n>2 k$,

$$
(1+p)^{n}>\binom{n}{k} p^{k}=\frac{n(n-1) \cdots(n-k+1)}{k!} p^{k}>\frac{n^{k} p^{k}}{2^{k} k!}
$$

Hence

$$
0<\frac{n^{\alpha}}{(1+p)^{n}}<\frac{2^{k} k!}{p^{k}} n^{\alpha-k} \quad(n>2 k)
$$

Since $\alpha-k<0, n^{\alpha-k} \rightarrow 0$, by (a).
(e) Take $\alpha=0$ in (d).

# SERIES 

In the remainder of this chapter, all sequences and series under consideration will be complex-valued, unless the contrary is explicitly stated. Extensions of some of the theorems which follow, to series with terms in $\mathbb{R}^{\mathrm{k}}$, are mentioned in Exercise 3.15 .
3.21 Definition. Given a sequence $\left(a_{n}\right)$, we use the notation

$$
\sum_{n=p}^{q} a_{n} \quad(p \leq q)
$$

to denote the sum $a_{p}+a_{p+1}+\cdots+a_{q}$. With $\left(a_{n}\right)$, we associate a sequence $\left(s_{n}\right)$, where

$$
s_{n}=\sum_{k=1}^{n} a_{k}
$$

For $\left(s_{n}\right)$ we also use the symbolic expression

$$
a_{1}+a_{2}+a_{3}+\cdots
$$

or, more concisely,

$$
\sum_{n=1}^{\infty} a_{n}
$$

The symbol in (3.4) we call an infinite series or just a series. The numbers $s_{n}$ are called the partial sums of the series. If $\left(s_{n}\right)$ converges to $s$, we say that the series converges, and write

$$
\sum_{n=1}^{\infty} a_{n}=s
$$

The number $s$ is called the sum of the series; but it should be clearly understood that $s$ is the limit of a sequence of sums, and is not obtained simply by addition.

If $\left(s_{n}\right)$ diverges, the series is said to diverge.
Sometimes, for convenience of notation, we shall consider series of the form

$$
\sum_{n=0}^{\infty} a_{n}
$$

And frequently, when there is no possible ambiguity, or when the distinction is immaterial, we shall simply write $\Sigma a_{n}$ in place of (3.4) or (3.5).

It is clear that every theorem about sequences can be stated in terms of series (putting $a_{1}=s_{1}$ and $a_{n}=s_{n}-s_{n-1}$ for $n>1$ ), and vice versa. But it is nevertheless useful to consider both concepts.

The Cauchy criterion (Theorem 3.11) can be restated in the following form:

3.22 Theorem. $\Sigma a_{n}$ converges if and only if for every $\varepsilon>0$ there is an integer N such that

$$
\left|\sum_{k=n}^{m} a_{k}\right| \leq \varepsilon
$$

if $\mathrm{m} \geq \mathrm{n} \geq \mathrm{N}$.
In particular, by taking $m=n,(3.6)$ becomes

$$
\left|a_{n}\right| \leq \varepsilon \quad(n \geq N)
$$

In other words:
3.23 Theorem. If $\sum a_{n}$ converges, then $\lim _{n \rightarrow \infty} a_{n}=0$.

The condition $a_{n} \rightarrow 0$ is not, however, sufficient to ensure convergence of $\Sigma a_{n}$. For instance, the series

$$
\sum_{n=1}^{\infty} \frac{1}{n}
$$

diverges; for the proof, we refer to Theorem 3.28.
Theorem 3.14, concerning monotonic sequences, also has an immediate counterpart for series.
3.24 Theorem. A series of nonnegative ${ }^{1}$ terms converges if and only if its partial sums form a bounded sequence.

We now turn to a convergence test of a different nature, the so-called "comparison test."

# 3.25 Theorem. 

(a) If $\left|a_{n}\right| \leq c_{n}$ for $n \geq N_{0}$, where $N_{0}$ is some fixed integer, and if $\Sigma c_{n}$ converges, then $\Sigma a_{n}$ converges.
(b) If $a_{n} \geq d_{n} \geq 0$ for $n \geq N_{0}$ and if $\Sigma d_{n}$ diverges, then $\Sigma a_{n}$ diverges.

Note that (b) applies only to series of nonnegative terms $a_{n}$.
Proof. Given $\varepsilon>0$, there exists $\mathrm{N} \geq \mathrm{N}_{0}$ such that $\mathrm{m} \geq \mathrm{n} \geq \mathrm{N}$ implies

$$
\sum_{k=n}^{m} c_{k} \leq \varepsilon
$$

by the Cauchy criterion. Hence

$$
\left|\sum_{k=n}^{m} a_{k}\right| \leq \sum_{k=n}^{m}\left|a_{k}\right| \leq \sum_{k=n}^{m} c_{k} \leq \varepsilon
$$

[^0]
[^0]:    ${ }^{1}$ The expression "nonnegative" always refers to real numbers.

and (a) follows.
Next, (b) follows from (a), for if $\Sigma a_{n}$ converges, so must $\Sigma d_{n}$ [note that (b) also follows from Theorem 3.24].

The comparison test is a very useful one; to use it efficiently, we have to become familiar with a number of series of nonnegative terms whose convergence or divergence is known.

# SERIES OF NONNEGATIVE TERMS 

The simplest of all is perhaps the geometric series.
3.26 Theorem. If $0 \leq x<1$, then

$$
\sum_{n=0}^{\infty} x^{n}=\frac{1}{1-x}
$$

If $x \geq 1$, the series diverges.
Proof. If $x \neq 1$,

$$
s_{n}=\sum_{k=0}^{n} x^{k}=\frac{1-x^{n+1}}{1-x}
$$

The result follows if we let $n \rightarrow \infty$. For $x=1$, we get

$$
1+1+1+\cdots
$$

which evidently diverges.
In many cases which occur in applications, the terms of the series decrease monotonically. The following theorem of Cauchy is therefore of a particular interest. The striking feature of the theorem is that a rather "thin" subsequence of $\left(a_{n}\right)$ determines the convergence or divergence of $\Sigma a_{n}$.
3.27 Theorem. Suppose $a_{1} \geq a_{2} \geq a_{3} \geq \cdots \geq 0$. Then the series $\sum_{n=1}^{\infty} a_{n}$ converges if and only if the series

$$
\sum_{k=0}^{\infty} 2^{k} a_{2^{k}}=a_{1}+2 a_{2}+4 a_{4}+8 a_{8}+\cdots
$$

converges.
Proof. By Theorem 3.24, it suffices to consider the boundedness of the partial sums. Let

$$
\begin{aligned}
s_{n} & =a_{1}+a_{2}+\cdots+a_{n} \\
t_{k} & =a_{1}+2 a_{2}+\cdots+2^{k} a_{2^{k}}
\end{aligned}
$$

For $\mathrm{n}<2^{\mathrm{k}}$,

$$
\begin{aligned}
s_{n} & \leq a_{1}+\left(a_{2}+a_{3}\right)+\cdots+\left(a_{2 k}+\cdots+a_{2 k+1}-1\right) \\
& \leq a_{1}+2 a_{2}+\cdots+2^{k} a_{2 k} \\
& =t_{k}
\end{aligned}
$$

so that

$$
s_{n} \leq t_{k}
$$

On the other hand, if $\mathrm{n}>2^{\mathrm{k}}$,

$$
\begin{aligned}
s_{n} & \geq a_{1}+a_{2}+\left(a_{3}+a_{4}\right)+\cdots+\left(a_{2 k-1}+1+\cdots+a_{2 k}\right) \\
& \geq \frac{1}{2} a_{1}+a_{2}+2 a_{4}+\cdots+2^{k-1} a_{2 k} \\
& =\frac{1}{2} t^{k}
\end{aligned}
$$

so that

$$
2 s_{n} \geq t_{k}
$$

By (3.8) and (3.9), the sequences $\left\{s_{n}\right\}$ and $\left\{t_{n}\right\}$ are either both bounded or both unbounded. This completes the proof.
3.28 Theorem. $\sum \frac{1}{n^{p}}$ converges if $p>1$ and diverges if $p \leq 1$.

Proof. If $\mathrm{p} \leq 0$, divergence follows from Theorem 3.23. If $\mathrm{p}>0$, Theorem 3.27 is applicable, and we are led to the series

$$
\sum_{k=0}^{\infty} 2^{k} \cdot \frac{1}{2^{k p}}=\sum_{k=0}^{\infty} 2^{(1-p) k}
$$

Now, $2^{1-p}<1$ if and only if $1-p<0$, and the result follows by comparison with the geometric series (take $x=2^{1-p}$ in Theorem 3.26).

As a further application of Theorem 3.27, we prove:
3.29 Theorem. If $\mathrm{p}>1$,

$$
\sum_{n=2}^{\infty} \frac{1}{n(\log n)^{p}}
$$

converges; if $\mathrm{p} \leq 1$, the series diverges.
Remark. " $\log \mathrm{n}$ " denotes the logarithm of n to the base e (compare Exercise 1.7); the number e will be defined in a moment (see Definition 3.30). We let the series start with $\mathrm{n}=2$ since $\log 1=0$.

Proof. The monotonicity of the logarithmic function (which will be discussed in more detail in Chap. 8) implies that $(\log n)_{n=1}^{\infty}$ increases. Hence $\left(1 /[n(\log n)^{p}]\right)_{n=1}^{\infty}$ decreases, and we can apply Theorem 3.27 to (3.10); this leads us to the series

$$
\sum_{k=1}^{\infty} 2^{k} \cdot \frac{1}{2^{k}\left(\log 2^{k}\right)^{p}}=\sum_{k=1}^{\infty} \frac{1}{(k \log 2)^{p}}=\frac{1}{(\log 2)^{p}} \sum_{k=1}^{\infty} \frac{1}{k^{p}}
$$

and Theorem 3.29 follows from Theorem 3.28.
This procedure may evidently be continued. For instance,

$$
\sum_{n=3}^{\infty} \frac{1}{n \log (n) \log (\log (n))}
$$

diverges, whereas

$$
\sum_{n=3}^{\infty} \frac{1}{n \log (n)(\log (\log n))^{2}}
$$

converges.
We may now observe that the terms of the series (3.12) differ very little from those of (3.13). Still, one diverges, the other converges. If we continue the process which led us from Theorem 3.28 to Theorem 3.29, and then to (3.12) and (3.13), we get pairs of convergent and divergent series whose terms differ even less than those of (3.12) and (3.13). One might thus be led to the conjecture that there is a limiting situation of some sort, a "boundary" with all convergent series on one side, all divergent series on the other side-at least as far as series with monotonic coefficients are concerned. This notion of a "boundary" is of course quite vague. The point we wish to make is this: No matter how we make this notion precise, the conjecture is false. Exercises 3.11(b) and 3.12(b) may serve as illustrations.

We do not wish to go any deeper into this aspect of convergence theory, and refer the reader to Knopp's "Theory and Application of Infinite Series," Chap. IX, particularly Sec. 41 [Kno28].

# THE NUMBER $e$ 

3.30 Definition. $e=\sum_{n=0}^{\infty} \frac{1}{n!}$.

Here, $n!=1 \cdot 2 \cdot 3 \cdots n$ if $n \geq 1$, and $0!=1$. Since

$$
\begin{aligned}
s_{n} & =1+1+\frac{1}{1 \cdot 2}+\frac{1}{1 \cdot 2 \cdot 3}+\cdots+\frac{1}{1 \cdot 2 \cdots n} \\
& <1+1+\frac{1}{2}+\frac{1}{2^{2}}+\cdots+\frac{1}{2^{n-1}}<3
\end{aligned}
$$

the series converges and the definition makes sense. In fact, the series converges very rapidly and allows us to compute e with great accuracy.

It is of interest to note that e can also be defined by means of another limit process; the proof provides a good illustration of operations with limits:
3.31 Theorem. $\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e$.

Proof. Let

$$
s_{n}=\sum_{k=0}^{n} \frac{1}{k!}, \quad t_{n}=\left(1+\frac{1}{n}\right)^{n}
$$

By the binomial theorem,

$$
\begin{aligned}
t_{n}=1+1+\frac{1}{2!}\left(1-\frac{1}{n}\right) & +\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\cdots \\
& +\frac{1}{n!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \cdots\left(1-\frac{n-1}{n}\right)
\end{aligned}
$$

Hence $t_{n} \leq s_{n}$, so that

$$
\limsup _{n \rightarrow \infty} t_{n} \leq e
$$

by Theorem 3.19. Next, if $n \geq m$,

$$
t_{n} \geq 1+1+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\cdots+\frac{1}{m!}\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{m-1}{n}\right)
$$

Let $n \rightarrow \infty$, keeping $m$ fixed. We get

$$
\liminf _{n \rightarrow \infty} t_{n} \geq 1+1+\frac{1}{2!}+\cdots+\frac{1}{m!}
$$

so that

$$
s_{m} \leq \liminf _{n \rightarrow \infty} t_{n}
$$

Letting $m \rightarrow \infty$, we finally get

$$
e \leq \liminf _{n \rightarrow \infty} t_{n}
$$

The theorem follows from (3.14) and (3.15).
The rapidity with which the series $\sum 1 / n$ ! converges can be estimated as follows: If $s_{n}$ has the same meaning as above, we have

$$
\begin{aligned}
e-s_{n} & =\frac{1}{(n+1)!}+\frac{1}{(n+2)!}+\frac{1}{(n+3)!}+\cdots \\
& <\frac{1}{(n+1)!}\left\{1+\frac{1}{n+1}+\frac{1}{(n+1)^{2}}+\cdots\right\}=\frac{1}{n!n}
\end{aligned}
$$

so that

$$
0<e-s_{n}<\frac{1}{n!n}
$$

Thus $s_{10}$, for instance, approximates e with an error less than $10^{-7}$. The inequality (3.16) is of theoretical interest as well since it enables us to prove the irrationality of e very easily.
3.32 Theorem. e is irrational.

Proof. Suppose e is rational. Then $\mathrm{e}=\mathrm{p} / \mathrm{q}$, where p and q are positive integers. By (3.16),

$$
0<q!\left(e-s_{q}\right)<\frac{1}{q}
$$

By our assumption, $q!e$ is an integer. Since

$$
q!s_{q}=q!\left(1+1+\frac{1}{2!}+\cdots+\frac{1}{q!}\right)
$$

is an integer, we see that $q!\left(e-s_{q}\right)$ is an integer.
Since $q \geq 1$, (3.17) implies the existence of an integer between 0 and 1 . We have thus reached a contradiction.

Actually, e is not even an algebraic number. For a simple proof of this, see page 25 of Niven's book [Niv65], or page 176 of Herstein's [Her64] cited in the Bibliography.

# THE ROOT AND RATIO TESTS 

3.33 Theorem. Given $\Sigma a_{n}$, put $\alpha=\lim \sup _{n \rightarrow \infty} \sqrt[n]{\left|a_{n}\right|}$.
(a) If $\alpha<1, \Sigma a_{n}$ converges;
(b) If $\alpha>1, \Sigma a_{n}$ diverges;
(c) If $\alpha=1$, the test gives no information.

Proof. If $\alpha<1$, we can choose $\beta$ so that $\alpha<\beta<1$, and an integer N such that

$$
\sqrt[n]{\left|a_{n}\right|}<\beta
$$

for $\mathrm{n} \geq \mathrm{N}$ [by Theorem 3.17(b)]. That is, $\mathrm{n} \geq \mathrm{N}$ implies

$$
\left|a_{n}\right|<\beta^{n}
$$

Since $0<\beta<1, \Sigma \beta_{n}$ converges. Convergence of $\Sigma a_{n}$ follows now from the comparison test.

If $\alpha>1$, then, again by Theorem 3.17 , there is a sequence $\left(n_{k}\right)$ such that

$$
\sqrt[n_{k}]{\left|a_{n_{k}}\right|} \rightarrow \alpha
$$

Hence $\left|a_{n}\right|>1$ for infinitely many values of $n$, so that the condition $a_{n} \rightarrow 0$, necessary for convergence of $\Sigma a_{n}$, does not hold (Theorem 3.23).

To prove (c), we consider the series

$$
\sum \frac{1}{n}, \quad \sum \frac{1}{n^{2}}
$$

For each of these series, $\alpha=1$, but the first diverges and the second converges.
3.34 Theorem. The series $\Sigma a_{n}$
(a) converges if $\lim \sup _{n \rightarrow \infty}\left|a_{n+1} / a_{n}\right|<1$,
(b) diverges if $\left|a_{n+1} / a_{n}\right| \geq 1$ for all $n \geq n_{0}$, where $n_{0}$ is some fixed integer.

Proof. If condition (a) holds, we can find $\beta<1$, and an integer N such that

$$
\left|\frac{a_{n+1}}{a_{n}}\right|<\beta
$$

for $\mathrm{n} \geq \mathrm{N}$. In particular,

$$
\begin{aligned}
& \left|a_{N+1}\right|<\beta\left|a_{N}\right| \\
& \left|a_{N+2}\right|<\beta\left|a_{N+1}\right|<\beta^{2}\left|a_{N}\right| \\
& \vdots \\
& \left|a_{N+p}\right|<\beta^{p}\left|a_{N}\right|
\end{aligned}
$$

That is,

$$
\left|a_{n}\right|<\left|a_{N}\right| \beta^{-N} \cdot \beta^{n}
$$

for $\mathrm{n} \geq \mathrm{N}$, and (a) follows from the comparison test, since $\Sigma \beta^{n}$ converges.
If $\left|a_{n+1}\right| \geq\left|a_{n}\right|$ for $n \geq n_{0}$, it is easily seen that the condition $a_{n} \rightarrow 0$ does not hold, and (b) follows.

Note: the knowledge that $\lim a_{n+1} / a_{n}=1$ implies nothing about the convergence of $\Sigma a_{n}$. The series $\sum 1 / n$ and $\sum 1 / n^{2}$ demonstrate this.

# 3.35 Examples. 

(a) Consider the series

$$
\frac{1}{2}+\frac{1}{3}+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\frac{1}{2^{3}}+\frac{1}{3^{3}}+\frac{1}{2^{4}}+\frac{1}{3^{4}}+\cdots
$$

for which

$$
\begin{aligned}
& \liminf _{n \rightarrow \infty} \frac{a_{n+1}}{a_{n}}=\lim _{n \rightarrow \infty}\left(\frac{2}{3}\right)^{n}=0, \\
& \liminf _{n \rightarrow \infty} \sqrt[n]{n}=\lim _{n \rightarrow \infty} \sqrt[2 n]{\frac{1}{3^{n}}}=\frac{1}{\sqrt{3}}, \\
& \limsup _{n \rightarrow \infty} \sqrt[n]{a_{n}}=\lim _{n \rightarrow \infty} \sqrt[2 n]{\frac{1}{2^{n}}}=\frac{1}{\sqrt{2}}, \\
& \limsup _{n \rightarrow \infty} \frac{a_{n+1}}{a_{n}}=\lim _{n \rightarrow \infty} \frac{1}{2}\left(\frac{3}{2}\right)^{n}=+\infty .
\end{aligned}
$$

The root test indicates convergence; the ratio test does not apply.
(b) The same is true for the series

$$
\frac{1}{2}+1+\frac{1}{8}+\frac{1}{4}+\frac{1}{32}+\frac{1}{16}+\frac{1}{128}+\frac{1}{64}+\cdots
$$

where

$$
\begin{aligned}
& \liminf _{n \rightarrow \infty} \frac{a_{n+1}}{a_{n}}=\frac{1}{8} \\
& \limsup _{n \rightarrow \infty} \frac{a_{n+1}}{a_{n}}=2
\end{aligned}
$$

but

$$
\lim _{n \rightarrow \infty} \sqrt[n]{a_{n}}=\frac{1}{2}
$$

3.36 Remarks. The ratio test is frequently easier to apply than the root test since it is usually easier to compute ratios than nth roots. However, the root test has wider scope. More precisely: Whenever the ratio test shows convergence, the root test does too; whenever the root test is inconclusive, the ratio test is too. This is a consequence of Theorem 3.37 and is illustrated by the above examples.

Neither of the two tests is subtle with regard to divergence. Both deduce divergence from the fact that $a_{n}$ does not tend to zero as $n \rightarrow \infty$.
3.37 Theorem. For any sequence $\left(c_{n}\right)$ of positive numbers,

$$
\begin{aligned}
& \liminf _{n \rightarrow \infty} \frac{c_{n+1}}{c_{n}} \leq \liminf _{n \rightarrow \infty} \sqrt[n]{c_{n}} \\
& \limsup _{n \rightarrow \infty} \sqrt[n]{c_{n}} \leq \limsup _{n \rightarrow \infty} \frac{c_{n+1}}{c_{n}}
\end{aligned}
$$

Proof. We shall prove the second inequality; the proof of the first is quite similar. Put

$$
\alpha=\limsup _{n \rightarrow \infty} \frac{c_{n+1}}{c_{n}}
$$

If $\alpha=+\infty$, there is nothing to prove. If $\alpha$ is finite, choose $\beta>\alpha$. There is an integer N such that

$$
\frac{c_{n+1}}{c_{n}} \leq \beta
$$

for $\mathrm{n} \geq \mathrm{N}$. In particular, for any $\mathrm{p}>0$,

$$
c_{N+k+1} \leq \beta c_{N+k} \quad(k=0,1, \ldots, p-1)
$$

Multiplying these inequalities, we obtain

$$
c_{N+p} \leq \beta^{p} c_{N}
$$

or

$$
c_{n} \leq c_{N} \beta^{-N} \cdot \beta^{n} \quad(n \geq N)
$$

Hence

$$
\sqrt[n]{c_{n}} \leq \sqrt[n]{c_{N} \beta^{-N}} \cdot \beta
$$

so that

$$
\limsup _{n \rightarrow \infty} \sqrt[n]{c_{n}} \leq \beta
$$

by Theorem 3.20(b). Since (3.18) is true for every $\beta>\alpha$, we have

$$
\limsup _{n \rightarrow \infty} \sqrt[n]{c_{n}} \leq \alpha
$$

# POWER SERIES 

3.38 Definition. Given a sequence $\left(c_{n}\right)$ of complex numbers, the series

$$
\sum_{n=0}^{\infty} c_{n} z^{n}
$$

is called a power series. The numbers $c_{n}$ are called the coefficients of the series; $z$ is a complex number.

In general, the series will converge or diverge depending on the choice of $z$. More specifically, with every power series there is associated a circle, the circle of convergence, such that (3.19) converges if $z$ is in the interior of the circle and diverges if $z$ is in the exterior of the circle (to cover all cases, we have to consider the plane as the interior of a circle with infinite radius, and a point as a circle with radius zero). The behavior on the circle of convergence is much more varied and cannot be described so simply.

3.39 Theorem. Given the power series $\Sigma c_{n} z^{n}$, put

$$
\alpha=\limsup _{n \rightarrow \infty} \sqrt[n]{\left|c_{n}\right|}, \quad R=\frac{1}{\alpha}
$$

(If $\alpha=0, R=+\infty$; if $\alpha=+\infty, R=0$.) Then $\Sigma c_{n} z^{n}$ converges if $|z|<R$ and diverges if $|z|>R$.

Proof. Put $a_{n}=c_{n} z^{n}$ and apply the root test:

$$
\limsup _{n \rightarrow \infty} \sqrt[n]{\left|a_{n}\right|}=|z| \limsup _{n \rightarrow \infty} \sqrt[n]{\left|c_{n}\right|}=\frac{|z|}{R}
$$

Note: $R$ is called the radius of convergence of $\Sigma c_{n} z^{n}$.

# 3.40 Examples. 

(a) The series $\sum n^{n} z^{n}$ has $R=0$.
(b) The series $\sum z^{n} / n$ ! has $R=+\infty$. (In this case the ratio test is easier to apply than the root test.)
(c) The series $\sum z^{n}$ has $R=1$. If $|z|=1$, the series diverges, since $\left(z^{n}\right)$ does not tend to 0 as $n \rightarrow \infty$.
(d) The series $\sum z^{n} / n$ has $R=1$. It diverges if $z=1$. It converges for all other $z$ with $|z|=1$. (The last assertion will be proved in Theorem 3.44.)
(e) The series $\sum z^{n} / n^{2}$ has $R=1$. It converges for all $z$ with $|z|=1$, by the comparison test, since $\left|z^{n} / n^{2}\right|=1 / n^{2}$.

## SUMMATION BY PARTS

3.41 Theorem. Given two sequences $\left(a_{n}\right)$ and $\left(b_{n}\right)$, put

$$
A_{n}=\sum_{k=0}^{n} a_{k}
$$

if $\mathrm{n} \geq 0$; put $\mathrm{A}_{-1}=0$. Then, if $\mathrm{O} \leq \mathrm{p} \leq \mathrm{q}$, we have

$$
\sum_{n=p}^{q} a_{n} b_{n}=\sum_{n=p}^{q-1} A_{n}\left(b_{n}-b_{n+1}\right)+A_{q} b_{q}-A_{p-1} b_{p}
$$

Proof.

$$
\sum_{n=p}^{q} a_{n} b_{n}=\sum_{n=p}^{q}\left(A_{n}-A_{n-1}\right) b_{n}=\sum_{n=p}^{q} A_{n} b_{n}-\sum_{n=p-1}^{q-1} A_{n} b_{n+1}
$$

and the last expression on the right is clearly equal to the right side of (3.20).

Formula (3.20), the so-called "partial summation formula," is useful in the investigation of series of the form $\Sigma a_{n} b_{n}$, particularly when $b_{n}$ is monotonic. We shall now give applications.

# 3.42 Theorem. Suppose 

(a) the partial sums $A_{n}$ of $\Sigma a_{n}$ form a bounded sequence;
(b) $b_{0} \geq b_{1} \geq b_{2} \geq \cdots$;
(c) $\lim _{n \rightarrow \infty} b_{n}=0$.

Then $\Sigma a_{n} b_{n}$ converges.
Proof. Choose $M$ such that $\left|A_{n}\right| \leq M$ for all $n$. Given $\varepsilon>0$, there is an integer $N$ such that $b_{N} \leq \varepsilon /(2 M)$. For $N \leq p \leq q$, we have

$$
\begin{aligned}
\left|\sum_{n=p}^{q} a_{n} b_{n}\right| & =\left|\sum_{n=p}^{q-1} A_{n}\left(b_{n}-b_{n+1}\right)+A_{q} b_{q}-A_{p-1} b_{p}\right| \\
& \leq M\left|\sum_{n=p}^{q-1}\left(b_{n}-b_{n+1}+b_{q}+b_{p}\right)\right| \\
& =2 M b_{p} \leq 2 M b_{N} \leq \varepsilon
\end{aligned}
$$

Convergence now follows from the Cauchy criterion. We now that the first inequality in the above chain depends of course on the fact that $b_{n}-b_{n+1} \geq 0$.

### 3.43 Theorem. Suppose

(a) $\left|c_{1}\right| \geq\left|c_{2}\right| \geq\left|c_{3}\right| \geq \cdots$;
(b) $c_{2 m-1} \geq 0, c_{2 m} \leq 0 \quad(m=1,2,3, \ldots)$;
(c) $\lim _{n \rightarrow \infty} c_{n}=0$.

Then $\Sigma c_{n}$ converges.
Series for which (b) holds are called "alternating series"; the theorem was known to Leibnitz.

Proof. Apply Theorem 3.42 with $a_{n}=(-1)^{n+1}, b_{n}=\left|c_{n}\right|$.
3.44 Theorem. Suppose the radius of convergence of $\Sigma c_{n} z^{n}$ is 1 , and suppose $c_{0} \geq c_{1} \geq$ $c_{2} \geq \cdots, \lim _{n \rightarrow \infty} c_{n}=0$. Then $\Sigma c_{n} z^{n}$ converges at every point on the circle $|z|=1$, except possibly at $z=1$.

Proof. Put $a_{n}=z^{n}, b_{n}=c_{n}$. The hypotheses of Theorem 3.42 are then satisfied, since

$$
\left|A_{n}\right|=\left|\sum_{n=0}^{n} z^{m}\right|=\left|\frac{1-z^{n+1}}{1-z}\right| \leq \frac{2}{|1-z|}
$$

if $|z|=1$ and $z \neq 1$.

# ABSOLUTE CONVERGENCE 

The series $\Sigma a_{n}$ is said to converge absolutely if the series $\Sigma\left|a_{n}\right|$ converges.
3.45 Theorem. If $\Sigma a_{n}$ converges absolutely, then $\Sigma a_{n}$ converges.

Proof. The assertion follows from the inequality

$$
\left|\sum_{k=n}^{m} a_{k}\right| \leq \sum_{k=n}^{m}\left|a_{k}\right|
$$

plus the Cauchy criterion.
3.46 Remarks. For series of positive terms, absolute convergence is the same as convergence.

If $\Sigma a_{n}$ converges, but $\Sigma\left|a_{n}\right|$ diverges, we say that $\Sigma a_{n}$ converges conditionally [[nonabsolutely]]. For instance, the series

$$
\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n}
$$

converges conditionally (Theorem 3.43).
The comparison test, as well as the root and ratio tests, is really a test for absolute convergence and therefore cannot give any information about conditionally convergent series. Summation by parts can sometimes be used to handle the latter. In particular, power series converge absolutely in the interior of the circle of convergence.

We shall see that we may operate with absolutely convergent series very much as with finite sums. We may multiply them term by term and we may change the order in which the additions are carried out, without affecting the sum of the series. But for conditionally convergent series, this is no longer true, and more care has to be taken when dealing with them.

## ADDITION AND MULTIPLICATION OF SERIES

3.47 Theorem. If $\Sigma a_{n}=A$ and $\Sigma b_{n}=B$, then $\Sigma\left(a_{n}+b_{n}\right)=A+B$ and $\Sigma\left(c a_{n}\right)=c A$ for any fixed $c$.

Proof. Let

$$
A_{n}=\sum_{k=0}^{n} a_{k}, \quad B_{n}=\sum_{k=0}^{n} b_{k}
$$

Then

$$
A_{n}+B_{n}=\sum_{k=0}^{n}\left(a_{k}+b_{k}\right)
$$

Since $\lim _{n \rightarrow \infty} A_{n}=A$ and $\lim _{n \rightarrow \infty} B_{n}=B$, we see that

$$
\lim _{n \rightarrow \infty}\left(A_{n}+B_{n}\right)=A+B
$$

The proof of the second assertion is even simpler.
Thus two convergent series may be added term by term, and the resulting series converges to the sum of the two series. The situation becomes more complicated when we consider multiplication of two series. To begin with, we have to define the product. This can be done in several ways; we shall consider the socalled "Cauchy product."
3.48 Definition. Given $\Sigma a_{n}$ and $\Sigma b_{n}$, we put

$$
c_{n}=\sum_{k=0}^{n} a_{k} b_{n-k} \quad(n=0,1,2, \ldots)
$$

and call $\Sigma c_{n}$ the product of the two given series.
This definition may be motivated as follows. If we take two power series $\sum a_{n} z^{n}$ and $\sum b_{n} z^{n}$, multiply them term by term, and collect terms containing the same power of $z$, we get

$$
\begin{aligned}
\sum_{n=0}^{\infty} a_{n} z^{n} \cdot \sum_{n=0}^{\infty} b_{n} z^{n} & =\left(a_{0}+a_{1} z+a_{2} z^{2}+\cdots\right)\left(b_{0}+b_{1} z+b_{2} z^{2}+\cdots\right) \\
& =a_{0} b_{0}+\left(a_{0} b_{1}+a_{1} b_{0}\right) z+\left(a_{0} b_{2}+a_{1} b_{1}+a_{2} b_{0}\right) z^{2}+\cdots \\
& =c_{0}+c_{1} z+c_{2} z^{2}+\cdots
\end{aligned}
$$

Setting $z=1$, we arrive at the above definition.
3.49 Example. If

$$
A_{n}=\sum_{k=0}^{n} a_{k}, \quad B_{n}=\sum_{k=0}^{n} b_{k}, \quad \sum_{k=0}^{n} c_{k}
$$

and $A_{n} \rightarrow A, B_{n} \rightarrow B$, then it is not at all clear that $\left(C_{n}\right)$ will converge to $A B$, since we do not have $C_{n}=A_{n} B_{n}$. The dependence of $\left(C_{n}\right)$ on $\left(A_{n}\right)$ and $\left(B_{n}\right)$ is quite a complicated one (see the proof of Theorem 3.50). We shall now show that the product of two convergent series may actually diverge.

The series

$$
\sum_{n=0}^{\infty} \frac{(-1)^{n}}{\sqrt{n+1}}=1-\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{3}}-\frac{1}{\sqrt{4}}+\cdots
$$

converges (Theorem 3.43). We form the product of this series with itself and obtain

$$
\begin{aligned}
\sum_{n=0}^{\infty} c_{n}=1-\left(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}\right) & +\left(\frac{1}{\sqrt{3}}+\frac{1}{\sqrt{2} \sqrt{2}}+\frac{1}{\sqrt{3}}\right) \\
& -\left(\frac{1}{\sqrt{4}}+\frac{1}{\sqrt{3} \sqrt{2}}+\frac{1}{\sqrt{2} \sqrt{3}}+\frac{1}{\sqrt{4}}\right)+\cdots
\end{aligned}
$$

so that

$$
c_{n}=(-1)^{n} \sum_{k=0}^{n} \frac{1}{\sqrt{(n-k+1)(k+1)}}
$$

Since

$$
(n-k+1)(k+1)=\left(\frac{n}{2}+1\right)^{2}-\left(\frac{n}{2}-k\right)^{2} \leq\left(\frac{n}{2}+1\right)^{2}
$$

we have

$$
\left|c_{n}\right| \geq \sum_{k=0}^{n} \frac{2}{n+2}=\frac{2(n+1)}{n+2}
$$

so that the condition $c_{n} \rightarrow 0$, which is necessary for the convergence of $\Sigma c_{n}$, is not satisfied.

In view of the next theorem, due to Mertens, we note that we have here considered the product of two conditionally convergent series.

# 3.50 Theorem. Suppose 

(a) $\sum_{n=0}^{\infty} a_{n}$ converges absolutely,
(b) $\sum_{n=0}^{\infty} a_{n}=A$,
(c) $\sum_{n=0}^{\infty} b_{n}=B$,
(d) $c_{n}=\sum_{k=0}^{n} a_{k} b_{n-k} \quad(n=0,1,2, \ldots)$.

Then

$$
\sum_{n=0}^{\infty} c_{n}=A B
$$

That is, the product of two convergent series converges, and to the right value, if at least one of the two series converges absolutely.

Proof. Put

$$
A_{n}=\sum_{k=0}^{n} a_{k}, \quad B_{n}=\sum_{k=0}^{n} b_{k}, \quad C_{n}=\sum_{k=0}^{n} c_{k}, \quad \beta_{n}=B_{n}-B
$$

Then

$$
\begin{aligned}
C_{n} & =a_{0} b_{0}+\left(a_{0} b_{1}+a_{1} b_{0}\right)+\cdots+\left(a_{0} b_{n}+a_{1} b_{n-1}+\cdots+a_{n} b_{0}\right) \\
& =a_{0} B_{n}+a_{1} B_{n-1}+\cdots+a_{n} B_{0} \\
& =a_{0}\left(B+\beta_{n}\right)+a_{1}\left(B+\beta_{n-1}\right)+\cdots+a_{n}\left(B+\beta_{0}\right) \\
& =A_{n} B+a_{0} \beta_{n}+a_{1} \beta_{n-1}+\cdots+a_{n} \beta_{0}
\end{aligned}
$$

Put

$$
\gamma_{n}=a_{0} \beta_{n}+a_{1} \beta_{n-1}+\cdots+a_{n} \beta_{0}
$$

We wish to show that $C_{n} \rightarrow A B$. Since $A_{n} B \rightarrow A B$, it suffices to show that

$$
\lim _{n \rightarrow \infty} \gamma_{n}=0
$$

Put

$$
\alpha=\sum_{n=0}^{\infty}\left|a_{n}\right|
$$

[It is here that we use (a).] Let $\varepsilon>0$ be given. By (c), $\beta_{n} \rightarrow 0$. Hence we can choose N such that $\left|\beta_{n}\right| \leq \varepsilon$ for $\mathrm{n} \geq \mathrm{N}$, in which case

$$
\begin{aligned}
\left|\gamma_{n}\right| & \leq\left|\beta_{0} a_{n}+\cdots+\beta_{N} a_{n-N}\right|+\left|\beta_{N+1} a_{n-N-1}+\cdots+\beta_{n} a_{0}\right| \\
& \leq\left|\beta_{0} a_{n}+\cdots+\beta_{n} a_{n-N}\right|+\varepsilon \alpha
\end{aligned}
$$

Keeping N fixed and letting $\mathrm{n} \rightarrow \infty$, we get

$$
\limsup _{n \rightarrow \infty}\left|\gamma_{n}\right| \leq \varepsilon \alpha
$$

since $a_{k} \rightarrow 0$ as $k \rightarrow \infty$. Since $\varepsilon$ is arbitrary, (3.21) follows.
Another question which may be asked is whether the series $\Sigma c_{n}$, if convergent, must have the sum $A B$. Abel showed that the answer is in the affirmative.
3.51 Theorem. If the series $\Sigma a_{n}, \Sigma b_{n}, \Sigma c_{n}$ converge to $A, B, C$, and $c_{n}=a_{0} b_{n}+$ $\cdots+a_{n} b_{0}$, then $C=A B$.

Here no assumption is made concerning absolute convergence. We shall give a simple proof (which depends on the continuity of power series) after Theorem 8.2.

# REARRANGEMENTS 

3.52 Definition. Let $\left(k_{n}\right), n=1,2,3, \ldots$ be a sequence in which every positive integer appears once and only once (that is, $\left(k_{n}\right)$ is a 1-1 function from $\mathbb{N}$ onto $\mathbb{N}$, in the notation of Definition 2.2). Putting

$$
a_{n}^{\prime}=a_{k_{n}} \quad(n=1,2,3, \ldots)
$$

we say that $\Sigma a_{n}^{\prime}$ is a rearrangement of $\Sigma a_{n}$.
If $\left(s_{n}\right),\left(s_{n}^{\prime}\right)$ are the sequences of the partial sums of $\Sigma a_{n}, \Sigma a_{n}^{\prime}$, it is easily seen that, in general, these two sequences consist of entirely different numbers. We are thus lead to the problem of determining under what conditions all rearrangements of a convergent series will converge and whether the sums are necessarily the same.
3.53 Example. Consider the convergent series

$$
1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\cdots
$$

and one of its rearrangements

$$
1+\frac{1}{3}-\frac{1}{2}+\frac{1}{5}+\frac{1}{7}-\frac{1}{4}+\frac{1}{9}+\frac{1}{11}-\frac{1}{6}+\cdots
$$

in which two positive terms are always followed by one negative. If $s$ is the sum of (3.22), then

$$
s<1-\frac{1}{2}+\frac{1}{3}=\frac{5}{6}
$$

Since

$$
\frac{1}{4 k-3}+\frac{1}{4 k-1}-\frac{1}{2 k}>0
$$

for $\mathrm{k} \geq 1$, we see that $\mathrm{s}_{3}^{\prime}<\mathrm{s}_{6}^{\prime}<\mathrm{s}_{9}^{\prime}<\cdots$, where $\mathrm{s}_{\mathrm{n}}^{\prime}$ is the nth partial sum of (3.23). Hence

$$
\limsup _{n \rightarrow \infty} s_{n}^{\prime}>s_{3}^{\prime}=\frac{5}{6}
$$

so that (3.23) certainly does not converge to $s$ [we leave it to the reader to verify that (3.23) does, however, converge].

This example illustrates the following theorem, due to Riemann.
3.54 Theorem. Let $\Sigma a_{n}$ be a series of real numbers which converges, but not absolutely. Suppose

$$
-\infty \leq \alpha \leq \beta \leq \infty
$$

Then there exists a rearrangement $\Sigma a_{n}^{\prime}$ with partial sums $s_{n}^{\prime}$ such that

$$
\liminf _{n \rightarrow \infty} s_{n}^{\prime}=\alpha, \quad \limsup _{n \rightarrow \infty} s_{n}^{\prime}=\beta
$$

Proof. Let

$$
p_{n}=\frac{\left|a_{n}\right|+a_{n}}{2}, \quad q_{n}=\frac{\left|a_{n}\right|-a_{n}}{2} \quad(n=1,2,3, \ldots)
$$

Then $p_{n}-q_{n}=a_{n}, p_{n}+q_{n}=\left|a_{n}\right|, p_{n} \geq 0, q_{n} \geq 0$. The series $\Sigma p_{n}, \Sigma q_{n}$ must

both diverge, for if both were convergent, then

$$
\sum\left(\mathrm{p}_{n}+\mathrm{q}_{n}\right)=\sum\left|a_{n}\right|
$$

would converge, contrary to hypothesis. Since

$$
\sum_{n=1}^{N} a_{n}=\sum_{n=1}^{N}\left(p_{n}-q_{n}\right)=\sum_{n=1}^{N} p_{n}-\sum_{n=1}^{N} q_{n}
$$

divergence of $\Sigma \mathrm{p}_{n}$ and convergence $\Sigma \mathrm{q}_{n}$ (or vice versa) implies divergence of $\Sigma \mathrm{a}_{n}$, again contrary to hypothesis.

Now let $\mathrm{P}_{1}, \mathrm{P}_{2}, \mathrm{P}_{3}, \ldots$ denote the nonnegative terms of $\Sigma \mathrm{a}_{n}$, in the order in which they occur, and let $Q_{1}, Q_{2}, Q_{3}, \ldots$ be the absolute values of the negative terms of $\Sigma \mathrm{a}_{n}$, also in their original order.

The series $\Sigma \mathrm{P}_{n}, \Sigma \mathrm{Q}_{n}$ differ from $\Sigma \mathrm{p}_{n}, \Sigma \mathrm{q}_{n}$ only by zero terms, and are therefore divergent.

We shall construct sequences $\left(m_{n}\right),\left(k_{n}\right)$ such that the series

$$
\begin{aligned}
\mathrm{P}_{1}+\cdots+\mathrm{P}_{\mathrm{m}_{1}}-\mathrm{Q}_{1}-\cdots-\mathrm{Q}_{\mathrm{k}_{1}} & +\mathrm{P}_{\mathrm{m}_{1}+1}+\cdots \\
& +\mathrm{P}_{\mathrm{m}_{2}}-\mathrm{Q}_{\mathrm{k}_{1}+1}-\cdots-\mathrm{Q}_{\mathrm{k}_{2}}+\cdots
\end{aligned}
$$

which clearly is a rearrangement of $\Sigma \mathrm{a}_{n}$, satisfies (3.24).
Choose real-valued sequences $\left(\alpha_{n}\right),\left(\beta_{n}\right)$ such that $\alpha_{n} \rightarrow \alpha, \beta_{n} \rightarrow \beta, \alpha_{n}<$ $\beta_{n}, \beta_{1}>0$.

Let $m_{1}, k_{1}$ be the smallest positive integers such that

$$
\begin{gathered}
\mathrm{P}_{1}+\cdots+\mathrm{P}_{\mathrm{m}_{1}}>\beta_{1} \\
\mathrm{P}_{1}+\cdots+\mathrm{P}_{\mathrm{m}_{1}}-\mathrm{Q}_{1}-\cdots-\mathrm{Q}_{\mathrm{k}_{1}}<\alpha_{1}
\end{gathered}
$$

let $m_{2}, k_{2}$ be the smallest positive integers such that

$$
\begin{gathered}
\mathrm{P}_{1}+\cdots+\mathrm{P}_{\mathrm{m}_{1}}-\mathrm{Q}_{1}-\cdots-\mathrm{Q}_{\mathrm{k}_{1}}+\mathrm{P}_{\mathrm{m}_{1}+1}+\cdots+\mathrm{P}_{\mathrm{m}_{2}}>\beta_{2} \\
\mathrm{P}_{1}+\cdots+\mathrm{P}_{\mathrm{m}_{1}}-\mathrm{Q}_{1}-\cdots-\mathrm{Q}_{\mathrm{k}_{1}}+\mathrm{P}_{\mathrm{m}_{1}+1}+\cdots+\mathrm{P}_{\mathrm{m}_{2}}-\mathrm{Q}_{\mathrm{k}_{1}+1}-\cdots-\mathrm{Q}_{\mathrm{k}_{2}}<\alpha_{2}
\end{gathered}
$$

and continue in this way. This is possible since $\Sigma \mathrm{P}_{n}$ and $\Sigma \mathrm{Q}_{n}$ diverge.
If $x_{n}, y_{n}$ denote the partial sums of (3.25) whose last terms are $P_{m_{n}}-Q_{k_{n}}$, then

$$
\left|x_{n}-\beta_{n}\right| \leq P_{m_{n}}, \quad\left|y_{n}-\alpha_{n}\right| \leq Q_{k_{n}}
$$

Since $P_{n} \rightarrow 0$ and $Q_{n} \rightarrow 0$ as $n \rightarrow \infty$, we see that $x_{n} \rightarrow \beta, y_{n} \rightarrow \alpha$.
Finally, it is clear that no number less than $\alpha$ or greater than $\beta$ can be a subsequential limit of the partial sums (3.25).
3.55 Theorem. If $\Sigma \mathrm{a}_{n}$ is a series of complex numbers which converges absolutely, then every rearrangement of $\Sigma \mathrm{a}_{n}$ converges, and they all converge to the same sum.

Proof. Let $\Sigma a_{n}^{\prime}$ be a rearrangement, with partial sums $s_{n}^{\prime}$. Given $\varepsilon>0$, there exists an integer N such that $\mathrm{m} \geq \mathrm{n} \geq \mathrm{N}$ implies

$$
\sum_{i=n}^{m}\left|a_{i}\right| \leq \varepsilon
$$

Now choose p such that the integers $1,2, \ldots, \mathrm{~N}$ are all contained in the set $\mathrm{k}_{1}, \mathrm{k}_{2}, \ldots, \mathrm{k}_{\mathrm{p}}$ (we use the notation of Definition 3.52). Then if $\mathrm{n}>\mathrm{p}$, the numbers $a_{1}, \ldots, a_{N}$ will cancel in the difference $s_{n}-s_{n}^{\prime}$, so that $\left|s_{n}-s_{n}^{\prime}\right| \leq \varepsilon$, by (3.26). Hence $\left(s_{n}^{\prime}\right)$ converges to the same sum as $\left(s_{n}\right)$.

# EXERCISES 

3.1. Prove that convergence of $\left(s_{n}\right)$ implies convergence of $\left(\left|s_{n}\right|\right)$. Is the converse true?
3.2. Calculate $\lim _{n \rightarrow \infty}\left(\sqrt{n^{2}+n}-n\right)$.
3.3. If $s_{1}=\sqrt{2}$ and

$$
s_{n+1}=\sqrt{2+\sqrt{s_{n}}} \quad(n=1,2,3, \ldots)
$$

prove that $\left(s_{n}\right)$ converges and that $s_{n}<2$ for $n=1,2,3, \ldots$
3.4. Find the upper and lower limits of the sequence $\left(s_{n}\right)$ defined by

$$
s_{1}=0 ; \quad s_{2 m}=\frac{s_{2 m-1}}{2} ; \quad s_{2 m+1}=\frac{1}{2}+s_{2 m}
$$

3.5. For any two real sequences $\left\{a_{n}\right\},\left\{b_{n}\right\}$, prove that

$$
\limsup _{n \rightarrow \infty}\left(a_{n}+b_{n}\right) \leq \limsup _{n \rightarrow \infty} a_{n}+\limsup _{n \rightarrow \infty} b_{n}
$$

provided the sum on the right is not of the form $\infty-\infty$.
3.6. Investigate the behavior (convergence or divergence) of $\Sigma a_{n}$ if
(a) $a_{n}=\sqrt{n+1}-\sqrt{n}$;
(b) $a_{n}=(\sqrt{n+1}-\sqrt{n}) / n$;
(c) $a_{n}=(\sqrt[n]{n}-1)^{n}$;
(d) $a_{n}=1 /\left(1+z^{n}\right)$, for complex values of $z$.
3.7. Prove that the convergence of $\Sigma a_{n}$ implies the convergence of

$$
\sum_{n=1}^{\infty} \frac{\sqrt{a_{n}}}{n}
$$

if $a_{n} \geq 0$.
3.8. If $\Sigma a_{n}$ converges and if $\left(b_{n}\right)$ is monotonic and bounded, prove that $\Sigma a_{n} b_{n}$ converges.
3.9. Find the radius of convergence of each of the following power series:
(a) $\sum n^{3} z^{n}$,
(b) $\sum \frac{2^{n}}{n!} z^{n}$,
(c) $\sum \frac{2^{n}}{n^{2}} z^{n}$,
(d) $\sum \frac{n^{3}}{3^{n}} z^{n}$.

3.10. Suppose that the coefficients of the power series $\Sigma a_{n} z^{n}$ are integers, infinitely many of which are distinct from zero. Prove that the radius of convergence is at most 1.
3.11. Suppose $a_{n}>0, s_{n}=a_{1}+\cdots+a_{n}$, and $\Sigma a_{n}$ diverges.
(a) Prove that $\sum a_{n} /\left(1+a_{n}\right)$ diverges.
(b) Prove that

$$
\frac{a_{N+1}}{s_{N+1}}+\cdots+\frac{a_{N+k}}{s_{N+k}} \geq 1-\frac{s_{N}}{s_{N+k}}
$$

and deduce that $\sum a_{n} / s_{n}$ diverges.
(c) Prove that

$$
\frac{a_{n}}{s_{n}^{2}} \leq \frac{1}{s_{n-1}}-\frac{1}{s_{n}}
$$

and deduce that $\sum a_{n} / s_{n}^{2}$ converges.
(d) What can be said about

$$
\sum \frac{a_{n}}{1+n a_{n}} \quad \text { and } \quad \sum \frac{a_{n}}{1+n^{2} a_{n}} ?
$$

3.12. Suppose $a_{n}>0$ and $\Sigma a_{n}$ converges. Put

$$
r_{n}=\sum_{m=n}^{\infty} a_{m}
$$

(a) Prove that

$$
\frac{a_{m}}{r_{m}}+\cdots+\frac{a_{n}}{r_{n}}>1-\frac{r_{n}}{r_{m}}
$$

if $m<n$, and deduce that $\sum a_{n} / r_{n}$ diverges.
(b) Prove that

$$
\frac{a_{n}}{\sqrt{r_{n}}}<2\left(\sqrt{r_{n}}-\sqrt{r_{n+1}}\right)
$$

and deduce that $\sum a_{n} / \sqrt{r_{n}}$ converges.
3.13. Prove that the Cauchy product of two absolutely convergent series converges absolutely.
3.14. If $\left\{s_{n}\right\}$ is a complex sequence, define its arithmetic means $\sigma_{n}$ by

$$
\sigma_{n}=\frac{s_{0}+s_{1}+\cdots+s_{n}}{n+1} \quad(n=0,1,2, \ldots)
$$

(a) If $\lim s_{n}=s$, prove that $\lim \sigma_{n}=s$.
(b) Construct a sequence $\left\{s_{n}\right\}$ which does not converge, although $\lim \sigma_{n}=0$.
(c) Can it happen that $s_{n}>0$ for all $n$ and that $\lim \sup s_{n}=\infty$, although $\lim \sigma_{n}=0$ ?
(d) Put $a_{n}=s_{n}-s_{n-1}$ for $n \geq 1$. Show that

$$
s_{n}-\sigma_{n}=\frac{1}{n+1} \sum_{k=1}^{n} k a_{k}
$$

Assume that $\lim \left(n a_{n}\right)=0$ and that $\left(\sigma_{n}\right)$ converges. Prove that $\left\{s_{n}\right\}$ converges. [This gives a converse of (a), but under the additional assumption that $n a_{n} \rightarrow 0$.]
(e) Derive the last conclusion from a weaker hypothesis: Assume $M<\infty,\left|n a_{n}\right| \leq M$ for all $n$, and $\lim \sigma_{n}=\sigma$. Prove that $\lim s_{n}=\sigma$ by completing the following outline:

If $m<n$, then

$$
s_{n}-\sigma_{n}=\frac{m+1}{n-m}\left(\sigma_{n}-\sigma_{m}\right)+\frac{1}{n-m} \sum_{i=m+1}^{n}\left(s_{n}-s_{i}\right)
$$

For these $i$,

$$
\left|s_{n}-s_{i}\right| \leq \frac{(n-i) M}{i+1} \leq \frac{(n-m-1) M}{m+2}
$$

Fix $\varepsilon>0$ and associate with each $n$ the integer $m$ that satisfies

$$
m \leq \frac{n-\varepsilon}{1+\varepsilon}<m+1
$$

Then $(m+1) /(n-m) \leq 1 / \varepsilon$ and $\left|s_{n}-s_{i}\right|<M \varepsilon$. Hence

$$
\limsup _{n \rightarrow \infty}\left|s_{n}-\sigma\right| \leq M \varepsilon
$$

Since $\varepsilon$ was arbitrary, $\lim s_{n}=\sigma$.
3.15. Definition 3.21 can be extended to the case in which the $a_{n}$ lie in some fixed $\mathbb{R}^{k}$. Absolute convergence is defined as convergence of $\sum\left|\mathbf{a}_{n}\right|$. Show that Theorems 3.22, 3.33, 3.25(a), $3.33,3.34,3.42,3.45,3.47$, and 3.55 are true in this more general setting. (Only slight modifications are required in any of the proofs.)
3.16. Fix a positive number $\alpha$. Choose $x_{1}>\sqrt{\alpha}$, and define $x_{2}, x_{3}, x_{4}, \ldots$ by the recursion formula

$$
x_{n+1}=\frac{1}{2}\left(x_{n}+\frac{\alpha}{x_{n}}\right)
$$

(a) Prove that $\left(x_{n}\right)$ decreases monotonically and that $\lim x_{n}=\sqrt{\alpha}$.
(b) Put $\varepsilon_{n}=x_{n}-\sqrt{\alpha}$ and show that

$$
\varepsilon_{n+1}=\frac{\varepsilon_{n}^{2}}{2 x_{n}}<\frac{\varepsilon_{n}^{2}}{2 \sqrt{\alpha}}
$$

so that, setting $\beta=2 \sqrt{\alpha}$,

$$
\varepsilon_{n+1}<\beta\left(\frac{\varepsilon_{1}}{\beta}\right)^{2^{n}} \quad(n=1,2,3, \ldots)
$$

(c) This is a good algorithm for computing square roots, since the recursion formula is simple and the convergence is extremely rapid. For example, if $\alpha=3$ and $x_{1}=2$, show that $\varepsilon_{1} / \beta<1 / 10$ and that therefore

$$
\varepsilon_{5}<4 \cdot 10^{-16}, \quad \varepsilon_{6}<4 \cdot 10^{-32}
$$

3.17. Fix $\alpha>1$. Take $x_{1}>\sqrt{\alpha}$ and define

$$
x_{n+1}=\frac{\alpha+x_{n}}{1+x_{n}}=x_{n}+\frac{\alpha-x_{n}^{2}}{1+x_{n}}
$$

(a) Prove that $x_{1}>x_{3}>x_{5}>\cdots$.
(b) Prove that $x_{2}<x_{4}<x_{6}<\cdots$.
(c) Prove that $\lim x_{n}=\sqrt{\alpha}$.
(d) Compare the rapidity of convergence of this process with the one described in Exercise 3.16 .
3.18. Replace the recursion formula of Exercise 3.16 by

$$
x_{n+1}=\frac{p-1}{p} x_{n}+\frac{\alpha}{p} x_{n}^{-p+1}
$$

where $p$ is a fixed positive integer, and describe the behavior of the resulting sequences $\left(x_{n}\right)$.

3.19. Associate to each sequence $a=\left(\alpha_{n}\right)$ in which $\alpha_{n}$ is 0 or 2 , the real number

$$
x(a)=\sum_{n=1}^{\infty} \frac{\alpha_{n}}{3^{n}}
$$

Prove that the set of all $x(a)$ is precisely the Cantor set described in Theorem 2.44
3.20. Suppose $\left(p_{n}\right)$ is a Cauchy sequence in a metric space $X$, and some subsequence $\left(p_{n_{i}}\right)$ converges to a point $\mathrm{p} \in \mathrm{X}$. Prove that the full sequence $\left(\mathrm{p}_{n}\right)$ converges to p .
3.21. Prove the following analogue of Theorem 3.10(b): If $\left(\mathrm{E}_{n}\right)$ is a sequence of closed, nonempty, and bounded sets in a complete metric space $X$, if $E_{n} \supset E_{n+1}$, and if

$$
\lim _{n \rightarrow \infty} \operatorname{diam} E_{n}=0
$$

then $\bigcap_{n=1}^{\infty} E_{n}$ consists of exactly one point.
3.22. Suppose $X$ is a nonempty complete metric space, and $\left(G_{n}\right)$ is a sequence of dense open subsets of X. Prove Baire's theorem, namely, that $\bigcap_{n=1}^{\infty} G_{n}$ is not empty (In fact, it is dense in X.) Hint: Find a shrinking sequence of neighborhoods $E_{n}$ such that $\tilde{E}_{n} \subset G_{n}$, and apply Exercise 3.21.
3.23. Suppose $\left(\mathrm{p}_{n}\right)$ and $\left(\mathrm{q}_{n}\right)$ are Cauchy sequences in a metric space X . Show that the sequence $\left(\mathrm{d}\left(\mathrm{p}_{n}, \mathrm{q}_{n}\right)\right.$ ) converges. Hint: For any $m, n$,

$$
\mathrm{d}\left(\mathrm{p}_{n}, \mathrm{q}_{n}\right) \leq \mathrm{d}\left(\mathrm{p}_{n}, \mathrm{p}_{m}\right)+\mathrm{d}\left(\mathrm{p}_{m}, \mathrm{q}_{m}\right)+\mathrm{d}\left(\mathrm{q}_{m}, \mathrm{q}_{n}\right)
$$

it follows that

$$
\left|\mathrm{d}\left(\mathrm{p}_{n}, \mathrm{q}_{n}\right)-\mathrm{d}\left(\mathrm{p}_{m}, \mathrm{q}_{m}\right)\right|
$$

is small if $m$ and $n$ are large.
3.24. Let $X$ be a metric space.
(a) Call two Cauchy sequences $\left(\mathrm{p}_{n}\right),\left(\mathrm{q}_{n}\right)$ in X equivalent if

$$
\lim _{n \rightarrow \infty} d\left(p_{n}, q_{n}\right)=0
$$

Prove that this is an equivalence relation.
(b) Let $X^{*}$ be the set of all equivalence classes so obtained. If $P \in X^{*}, Q \in X^{*},\left(p_{n}\right) \in P$, $\left(\mathrm{q}_{n}\right) \in \mathrm{Q}$, define

$$
\Delta(\mathrm{P}, \mathrm{Q})=\lim _{n \rightarrow \infty} \mathrm{~d}\left(\mathrm{p}_{n}, \mathrm{q}_{n}\right)
$$

by Exercise 3.23, this limit exists. Show that the number $\Delta(\mathrm{P}, \mathrm{Q})$ is unchanged if $\left(\mathrm{p}_{n}\right)$ and $\left(\mathrm{q}_{n}\right)$ are replaced by equivalent subsequences, and hence that $\Delta$ is a distance function in $X^{*}$.
(c) Prove that the resulting metric space $X^{*}$ is complete.
(d) For each $\mathrm{p} \in \mathrm{X}$, there is a Cauchy sequence all of whose terms are p ; let $\mathrm{P}_{\mathrm{p}}$ be the element of $X^{*}$ which contains this sequence. Prove that

$$
\Delta\left(\mathrm{P}_{\mathrm{p}}, \mathrm{P}_{\mathrm{q}}\right)=\mathrm{d}(\mathrm{p}, \mathrm{q})
$$

for all $\mathrm{p}, \mathrm{q} \in \mathrm{X}$. In other words, the mapping $\varphi$ defined by $\varphi(\mathrm{p})=\mathrm{P}_{\mathrm{p}}$ is an isometry (i.e., a distance-preserving mapping) of $X$ into $X^{*}$.
(e) Prove that $\varphi(\mathrm{X})$ is dense in $\mathrm{X}^{*}$ and that $\varphi(\mathrm{X})=\mathrm{X}^{*}$ if X is complete. By (d), we may identify $X$ and $\varphi(X)$ and thus regard $X$ as embedded in the complete metric space $X^{*}$. We call $X^{*}$ the completion of $X$.
3.25. Let $X$ be the metric space whose points are the rational numbers, with the metric $d(x, y)=$ $|x-y|$. What is the completion of this space? (Compare Exercise 3.24).

# Chapter 4 

## CONTINUITY

The function concept and some of the related terminology were introduced in Definition 2.1 and Definition 2.2. Although we shall (in later chapters) be mainly interested in real and complex functions (i.e., in functions whose values are real or complex numbers) we shall also discuss vector-valued functions (i.e., functions with values in $\mathrm{R}^{\mathrm{k}}$ ) and functions with values in an arbitrary metric space. The theorems we shall discuss in this general setting would not become any easier if we restricted ourselves to real functions, for instance, and it actually simplifies and clarifies the picture to discard unnecessary hypotheses and to state and prove theorems in an appropriately general context.

The domains of definition of our functions will also be metric spaces, suitably specialized in various instances.

## LIMITS OF FUNCTIONS

4.1 Definition. Let $X$ and $Y$ be metric spaces; suppose $E \subset X$, f maps $E$ into $Y$, and $p$ is a limit point of $E$. We write $f(x) \rightarrow q$ as $x \rightarrow p$, or

$$
\lim _{x \rightarrow p} f(x)=q
$$

if there is a point $q \in Y$ with the following property: For every $\varepsilon>0$ there exists a $\delta>0$ such that

$$
\mathrm{d}_{\mathrm{Y}}(\mathrm{f}(\mathrm{x}), \mathrm{q})<\varepsilon
$$

for all points $x \in E$ for which

$$
0<\mathrm{d}_{\mathrm{X}}(\mathrm{x}, \mathrm{p})<\delta
$$

The symbols $\mathrm{d}_{\mathrm{X}}$ and $\mathrm{d}_{\mathrm{Y}}$ refer to the distances in X and Y , respectively.
If X and/or Y are replaced by the real line, the complex plane, or by some

euclidean space $\mathbb{R}^{\mathrm{k}}$, the distances $\mathrm{d}_{\mathrm{X}}, \mathrm{d}_{\mathrm{Y}}$ are of course replaced by absolute values, or by norms of differences (see Example 2.16).

It should be noted that $\mathrm{p} \in \mathrm{X}$, but that p need not be a point of E in the above definition. Moreover, even if $\mathrm{p} \in \mathrm{E}$, we may very well have $\mathrm{f}(\mathrm{p}) \neq \lim _{\mathrm{x} \rightarrow \mathrm{p}} \mathrm{f}(\mathrm{x})$.

We can recast this definition in terms of limits of sequences:
4.2 Theorem. Let $\mathrm{X}, \mathrm{Y}, \mathrm{E}, \mathrm{f}$, and p be as in Definition 4.1. Then

$$
\lim _{x \rightarrow p} f(x)=q
$$

if and only if

$$
\lim _{n \rightarrow \infty} f\left(p_{n}\right)=q
$$

for every sequence $\left(p_{n}\right)$ in E such that

$$
p_{n} \neq p, \quad \lim _{n \rightarrow \infty} p_{n}=p
$$

Proof. Suppose (4.4) holds. Choose $\left(p_{n}\right)$ in E satisfying (4.6). Let $\varepsilon>0$ be given. Then there exists $\delta>0$ such that $d_{Y}(f(x), q)<\varepsilon$ if $x \in E$ and $0<d_{X}(x, p)<\delta$. Also, there exists N such that $\mathrm{n}>\mathrm{N}$ implies $\mathrm{O}<\mathrm{d}_{\mathrm{X}}\left(\mathrm{p}_{\mathrm{n}}, \mathrm{p}\right)<\delta$. Thus, for $\mathrm{n}>\mathrm{N}$, we have $d_{Y}\left(f\left(p_{n}\right), q\right)<\varepsilon$, which shows that (4.5) holds.

Conversely, suppose (4.4) is false. Then there exists some $\varepsilon>0$ such that for every $\delta>0$ there exists a point $x \in E$ (depending on $\delta$ ), for which $d_{Y}(f(x), q) \geq \varepsilon$ but $0<d_{X}(x, p)<\delta$. Taking $\delta_{n}=1 / n(n=1,2,3, \ldots)$, we thus find a sequence in E satisfying (4.6) for which (4.5) is false.

Corollary. If f has a limit at p , this limit is unique.
This follows from Theorems 3.2(b) and 4.2
4.3 Definition. Suppose we have two complex functions, $f$ and $g$, both defined on E. By $\mathrm{f}+\mathrm{g}$ we mean the function which assigns to each point x of E the number $f(x)+g(x)$. Similarly we define the difference $f-g$, the product $f g$, and the quotient $\mathrm{f} / \mathrm{g}$ of two functions, with the understanding that the quotient is defined only at those points $x$ of $E$ at which $g(x) \neq 0$. If $f$ assigns to each point $x$ of $E$ the same number $c$, then $f$ is said to be a constant function, or simply a constant, and we write $f=c$. If $f$ and $g$ are real functions, and if $f(x) \geq g(x)$ for every $x \in E$, we shall sometimes write $f \geq g$ for brevity.

Similarly, if $\mathbf{f}$ and $\mathbf{g}$ map $E$ into $\mathbb{R}^{k}$, we define $\mathbf{f}+\mathbf{g}$ and $\mathbf{f} \cdot \mathbf{g}$ by

$$
(\mathbf{f}+\mathbf{g})(x)=\mathbf{f}(x)+\mathbf{g}(x), \quad(\mathbf{f} \cdot \mathbf{g})(x)=\mathbf{f}(x) \cdot \mathbf{g}(x)
$$

and if $\lambda$ is a real number, $(\lambda \mathbf{f})(x)=\lambda \mathbf{f}(x)$.

4.4 Theorem. Suppose $\mathrm{E} \subset \mathrm{X}$, a metric space, p is a limit point of E , f and g are complex functions on E , and

$$
\lim _{x \rightarrow p} f(x)=A, \quad \lim _{x \rightarrow p} g(x)=B
$$

Then
(a) $\lim _{x \rightarrow p}(f+g)(x)=A+B$;
(b) $\lim _{x \rightarrow p}(f g)(x)=A B$;
(c) $\lim _{x \rightarrow p}\left(\frac{f}{g}\right)(x)=\frac{A}{B}$, if $B \neq 0$.

Proof. In view of Theorem 4.2, these assertions follow immediately from the analogous properties of sequences (Theorem 3.3).

Remark. If $\mathbf{f}$ and $\mathbf{g}$ map $E$ into $R^{k}$, then (a) remains true, and (b) becomes
(b') $\lim _{x \rightarrow p}(f \cdot g)(x)=A \cdot B$.
(Compare Theorem 3.4.)

# CONTINUOUS FUNCTIONS 

4.5 Definition. Suppose $X$ and $Y$ are metric spaces, $E \subset X, p \in E$, and $f$ maps $E$ into $Y$. Then $f$ is said to be continuous at $p$ if for every $\varepsilon>0$ there exists a $\delta>0$ such that

$$
d_{Y}(f(x), f(p))<\varepsilon
$$

for all points $x \in E$ for which $d_{X}(x, p)<\delta$.
If $f$ is continuous at every point of $E$, then $f$ is said to be continuous on $E$.
It should be noted that $f$ has to be defined at the point $p$ in order to be continuous at p . (Compare this with the remark following Definition 4.1.)

If $p$ is an isolated point of $E$, then our definition implies that every function $f$ which has $E$ as its domain of definition is continuous at $p$. For, no matter which $\varepsilon>0$ we choose, we can pick $\delta>0$ so that the only point $x \in E$ for which $d_{X}(x, p)<\delta$ is $x=p$; then

$$
d_{Y}(f(x), f(p))=0<\varepsilon
$$

4.6 Theorem. In the situation given in Definition 4.5, assume also that p is a limit point of E. Then f is continuous at p if and only if $\lim _{x \rightarrow p} f(x)=f(p)$.

Proof. This is clear if we compare Definitions 4.1 and 4.5.
We now turn to compositions of functions. A brief statement of the following theorem is that a continuous function of a continuous function is continuous.

4.7 Theorem. Suppose $X, Y, Z$ are metric spaces, $E \subset X, f$ maps $E$ into $Y$, g maps the range of $\mathrm{f}, \mathrm{f}(\mathrm{E})$, into Z , and h is the mapping of E into Z defined by

$$
h(x)=g(f(x)) \quad(x \in E)
$$

If f is continuous at a point $\mathrm{p} \in \mathrm{E}$ and if g is continuous at the point $\mathrm{f}(\mathrm{p})$, then h is continuous at p .

This function h is called the composition or the composite of f and g . The notation

$$
\mathrm{h}=\mathrm{g} \circ \mathrm{f}
$$

is frequently used in this context.
Proof. Let $\varepsilon>0$ be given. Since $g$ is continuous at $f(p)$, there exists $\eta>0$ such that

$$
d_{Z}(g(y), g(f(p)))<\varepsilon \text { if } d_{Y}(y, f(p))<\eta \text { and } y \in f(E)
$$

Since f is continuous at p , there exists $\delta>0$ such that

$$
d_{Y}(f(x), f(p))<\eta \text { if } d_{X}(x, p)<\delta \text { and } x \in E
$$

It follows that

$$
d_{Z}(h(x), h(p))=d_{Z}(g(f(x)), g(f(p)))<\varepsilon
$$

if $d_{X}(x, p)<\delta$ and $x \in E$. Thus $h$ is continuous at $p$.
4.8 Theorem. A mapping f of a metric space X into a metric space Y is continuous on X if and only if $\mathrm{f}^{-1}(\mathrm{~V})$ is open in X for every open set V in Y .
(Inverse images are defined in Definition 2.2.) This is a very useful characterization of continuity.

Proof. Suppose f is continuous on X and V is an open set in Y . We have to show that every point of $\mathrm{f}^{-1}(\mathrm{~V})$ is an interior point of $\mathrm{f}^{-1}(\mathrm{~V})$. So, suppose $\mathrm{p} \in \mathrm{X}$ and $\mathrm{f}(\mathrm{p}) \in \mathrm{V}$. Since V is open, there exists $\varepsilon>0$ such that $y \in V$ if $d_{Y}(f(p), y)<\varepsilon$; and since f is continuous at p , there exists $\delta>0$ such that $d_{Y}(f(x), f(p))<\varepsilon$ if $d_{X}(x, p)<\delta$. Thus $x \in f^{-1}(V)$ as soon as $d_{X}(x, p)<\delta$.

Conversely, suppose $\mathrm{f}^{-1}(\mathrm{~V})$ is open in X for every open set V in Y . Fix $\mathrm{p} \in \mathrm{X}$ and $\varepsilon>0$, let $V$ be the set of all $y \in Y$ such that $d_{Y}(y, f(p))<\varepsilon$. Then $V$ is open; hence $\mathrm{f}^{-1}(\mathrm{~V})$ is open; hence there exists $\delta>0$ such that $x \in \mathrm{f}^{-1}(\mathrm{~V})$ as soon as $d_{X}(p, x)<\delta$. But if $x \in f^{-1}(V)$, then $f(x) \in V$, so that $d_{Y}(f(x), f(p))<\varepsilon$.

This completes the proof.
Corollary. A mapping f of a metric space X into a metric space Y is continuous if and only if $\mathrm{f}^{-1}(\mathrm{C})$ is closed in X for every closed set C in Y .

This follows from the theorem, since a set is closed if and only if its complement is open, and since $f^{-1}\left(E^{c}\right)=\left[f^{-1}(E)\right]^{c}$ for every $E \subset Y$.

We now turn to complex-valued and vector-valued functions, and to functions defined on subsets of $\mathbb{R}^{\mathrm{k}}$.
4.9 Theorem. Let f and g be complex continuous functions on a metric space X . Then $\mathrm{f}+\mathrm{g}, \mathrm{fg}$, and $\mathrm{f} / \mathrm{g}$ are continuous on X .

In the last case, we must of course assume that $g(x) \neq 0$, for all $x \in X$.
Proof. At isolated points of $X$ there is nothing to prove. At limit points, the statement follows from Theorems 4.4 and 4.6.

# 4.10 Theorem. 

(a) Let $f_{1}, \ldots, f_{k}$ be real functions on a metric space $X$, and let $\mathbf{f}$ be the mapping of $X$ into $\mathbb{R}^{\mathrm{k}}$ defined by

$$
\mathbf{f}(\mathrm{x})=\left(\mathrm{f}_{1}(\mathrm{x}), \ldots, \mathrm{f}_{\mathrm{k}}(\mathrm{x})\right) \quad(\mathrm{x} \in \mathrm{X})
$$

then $\mathbf{f}$ is continuous if and only if each of the functions $f_{1}, \ldots, f_{k}$ is continuous.
(b) If $\mathbf{f}$ and $\mathbf{g}$ are continuous mappings of $X$ into $\mathbb{R}^{\mathrm{k}}$, then $\mathbf{f}+\mathbf{g}$ and $\mathbf{f} \cdot \mathbf{g}$ are continuous on X .

The functions $f_{1}, \ldots, f_{k}$ are called the components of $\mathbf{f}$. Note that $\mathbf{f}+\mathbf{g}$ is a mapping into $\mathbb{R}^{\mathrm{k}}$, whereas $\mathbf{f} \cdot \mathbf{g}$ is a real function on X .

Proof. Part (a) follows from the inequalities

$$
\left|f_{j}(x)-f_{j}(y)\right| \leq|\mathbf{f}(x)-\mathbf{f}(y)|=\left\{\sum_{i=1}^{k}\left|f_{j}(x)-f_{j}(y)\right|^{2}\right\}^{1 / 2}
$$

for $\mathrm{j}=1, \ldots, \mathrm{k}$. Part (b) follows from (a) and Theorem 4.9
4.11 Examples. If $x_{1}, \ldots, x_{k}$ are the coordinates of the point $x \in \mathbb{R}^{k}$, the functions $\phi_{i}$ defined by

$$
\phi_{i}(\mathbf{x})=x_{i} \quad\left(\mathbf{x} \in \mathbb{R}^{\mathrm{k}}\right)
$$

are continuous on $\mathbb{R}^{\mathrm{k}}$, since the inequality

$$
\left|\phi_{i}(\mathbf{x})-\phi_{i}(\mathbf{y})\right| \leq|\mathbf{x}-\mathbf{y}|
$$

shows that we may take $\delta=\varepsilon$ in Definition 4.5. The functions $\phi_{i}$ are sometimes called the coordinate functions.

Repeated application of Theorem 4.9 then shows that every monomial

$$
x_{1}^{n_{1}} x_{2}^{n_{2}} \cdots x_{k}^{n_{k}}
$$

where $n_{1}, \ldots, n_{k}$ are nonnegative integers, is continuous on $\mathbb{R}^{k}$. The same is true of constant multiples of (4.9), since constants are evidently continuous. It follows that every polynomial $P$, given by

$$
P(\mathbf{x})=\sum c_{n_{1} \ldots n_{k}} x_{1}^{n_{1}} \cdots x_{k}^{n_{k}} \quad\left(\mathbf{x} \in \mathbb{R}^{k}\right)
$$

is continuous on $\mathbb{R}^{k}$. Here the coefficients $c_{n_{1} \ldots n_{k}}$ are complex numbers, $n_{1}, \ldots, n_{k}$ are nonnegative integers, and the sum in (4.10) has finitely many terms.

Furthermore, every rational function in $x_{1}, \ldots, x_{k}$, that is, every quotient of two polynomials of the form (4.10), is continuous on $\mathbb{R}^{k}$ wherever the denominator is different from zero.

From the triangle inequality one sees easily that

$$
||\mathbf{x}|-|\mathbf{y}|| \leq|\mathbf{x}-\mathbf{y}| \quad\left(\mathbf{x}, \mathbf{y} \in \mathbb{R}^{k}\right)
$$

Hence the mapping $\mathbf{x} \rightarrow|\mathbf{x}|$ is a continuous real function on $\mathbb{R}^{k}$.
If now $\mathbf{f}$ is a continuous mapping from a metric space $X$ into $\mathbb{R}^{k}$, and if $\phi$ is defined on $X$ by setting $\phi(p)=|\mathbf{f}(p)|$, it follows, by Theorem 4.7, that $\phi$ is a continuous real function on $X$.
4.12 Remark. We defined the notion of continuity for functions defined on a subset $E$ of a metric space $X$. However, the complement of $E$ in $X$ plays no role whatever in this definition (note that the situation was somewhat different for limits of functions). Accordingly, we lose nothing of interest by discarding the complement of the domain of $f$. This means that we may just as well talk only about continuous mappings of one metric space into another, rather than of mappings of subsets. This simplifies statements and proofs of some theorems. We have already made use of this principle in Theorems 4.8 to 4.10 , and will continue to do so in the following section on compactness.

# CONTINUITY AND COMPACTNESS 

4.13 Definition. A mapping $\mathbf{f}$ of a set $E$ into $\mathbb{R}^{k}$ is said to be bounded if there is a real number $M$ such that $|\mathbf{f}(\mathrm{x})| \leq M$ for all $\mathrm{x} \in \mathrm{E}$.
4.14 Theorem. Suppose f is a continuous mapping of a compact metric space X into a metric space $Y$. Then $\mathrm{f}(\mathrm{X})$ is compact.

Proof. Let $\left\{V_{\alpha}\right\}$ be an open cover of $f(X)$. Since $f$ is continuous, Theorem 4.8 shows that each of the sets $f^{-1}\left(V_{\alpha}\right)$ is open. Since $X$ is compact, there are finitely many indices, say $\alpha_{1}, \ldots, \alpha_{n}$, such that

$$
X \subset f^{-1}\left(V_{\alpha_{1}}\right) \cup \cdots \cup f^{-1}\left(V_{\alpha_{n}}\right)
$$

Since $f\left(f^{-1}(E)\right) \subset E$ for every $E \subset Y$, (4.12) implies that

$$
f(X) \subset V_{\alpha_{1}} \cup \cdots \cup V_{\alpha_{n}}
$$

This completes the proof.
Note: We have used the relation $f\left(f^{-1}(E)\right) \subset E$, valid for $E \subset Y$. If $E \subset X$, then $f^{-1}(f(E)) \supset E$; equality need not hold in either case.

We shall now deduce some consequences of Theorem 4.14.
4.15 Theorem. If $\mathbf{f}$ is a continuous mapping of a compact metric space X into $\mathbb{R}^{\mathrm{k}}$, then $\mathbf{f}(\mathrm{X})$ is closed and bounded. Thus, $\mathbf{f}$ is bounded.

This follows from Theorem 2.41. The result is particularly important when $f$ is real:
4.16 Theorem. Suppose f is a continuous real function on a compact metric space X , and

$$
M=\sup _{p \in X} f(p), \quad m=\inf _{p \in X} f(p)
$$

Then there exist points $\mathrm{p}, \mathrm{q} \in \mathrm{X}$ such that $\mathrm{f}(\mathrm{p})=\mathrm{M}$ and $\mathrm{f}(\mathrm{q})=\mathrm{m}$.
The notation in (4.14) means that $M$ is the least upper bound of the set of all numbers $f(p)$, where $p$ ranges over $X$, and that $m$ is the greatest lower bound of this set of numbers.

The conclusion may also be stated as follows: There exist points p and q in X such that $f(q) \leq f(x) \leq f(p)$ for all $x \in X$; that is, $f$ attains its maximum (at $p$ ) and its minimum (at q).

Proof. By Theorem 4.15, $\mathrm{f}(\mathrm{X})$ is a closed and bounded set of real numbers; hence $f(X)$ contains

$$
M=\sup f(X) \quad \text { and } \quad m=\inf f(X)
$$

by Theorem 2.28 .
4.17 Theorem. Suppose f is a continuous 1-1 mapping of a compact metric space X onto a metric space $Y$. Then the inverse mapping $f^{-1}$ defined on $Y$ by

$$
f^{-1}(f(x))=x \quad(x \in X)
$$

is a continuous mapping of Y onto X .
Proof. Applying Theorem 4.8 to $f^{-1}$ in place of $f$, we see that it suffices to prove that $f(V)$ is an open set in $Y$ for every open set $V$ in $X$. Fix such a set $V$.

The complement $V^{c}$ of $V$ is closed in $X$, hence compact (Theorem 2.35); hence $f\left(V^{c}\right)$ is a compact subset of $Y$ (Theorem 4.14) and so is closed in $Y$ (Theorem 2.34). Since $f$ is one-to-one and onto, $f(V)$ is the complement of $f\left(V^{c}\right)$. Hence $f(V)$ is open.

4.18 Definition. Let f be a mapping of a metric space X into a metric space Y . We say that f is uniformly continuous on X if for every $\varepsilon>0$ there exists $\delta>0$ such that

$$
\mathrm{d}_{\mathrm{Y}}(\mathrm{f}(\mathrm{p}), \mathrm{f}(\mathrm{q}))<\varepsilon
$$

for all p and q in X for which $\mathrm{d}_{\mathrm{X}}(\mathrm{p}, \mathrm{q})<\delta$.
Let us consider the differences between the concepts of continuity and of uniform continuity. First, uniform continuity is a property of a function on a set, whereas continuity can be defined at a single point. To ask whether a given function is uniformly continuous at a certain point is meaningless. Second, if f is continuous on X , then it is possible to find, for each $\varepsilon>0$ and for each point p of X , a number $\delta>0$ having the property specified in Definition 4.5. This $\delta$ depends on $\varepsilon$ and on p . If f is, however, uniformly continuous on X , then it is possible, for each $\varepsilon>0$, to find one number $\delta>0$ which will do for all points p of X .

Evidently, every uniformly continuous function is continuous. That the two concepts are equivalent on compact sets follows from the next theorem.
4.19 Theorem. Let f be a continuous mapping of a compact metric space X into a metric space Y. Then f is uniformly continuous on X .

Proof. Let $\varepsilon>0$ be given. Since f is continuous, we can associate to each point $\mathrm{p} \in \mathrm{X}$ a positive number $\phi(\mathrm{p})$ such that

$$
\mathrm{q} \in \mathrm{X}, \mathrm{~d}_{\mathrm{X}}(\mathrm{p}, \mathrm{q})<\phi(\mathrm{p}) \quad \text { implies } \quad \mathrm{d}_{\mathrm{Y}}(\mathrm{f}(\mathrm{p}), \mathrm{f}(\mathrm{q}))<\frac{\varepsilon}{2}
$$

Let $\mathrm{J}(\mathrm{p})$ be the set of all $\mathrm{q} \in \mathrm{X}$ for which

$$
\mathrm{d}_{\mathrm{X}}(\mathrm{p}, \mathrm{q})<\frac{1}{2} \phi(\mathrm{p})
$$

Since $\mathrm{p} \in \mathrm{J}(\mathrm{p})$, the collection of all sets $\mathrm{J}(\mathrm{p})$ is an open cover of X ; since X is compact, there is a finite set of points $\mathrm{p}_{1}, \ldots, \mathrm{p}_{n}$ in X , such that

$$
X \subset J\left(p_{1}\right) \cup \cdots \cup J\left(p_{n}\right)
$$

We put

$$
\delta=\frac{1}{2} \min \left(\phi\left(\mathrm{p}_{1}\right), \ldots, \phi\left(\mathrm{p}_{n}\right)\right)
$$

Then $\delta>0$. (This is one point where the finiteness of the covering, inherent in the definition of compactness, is essential. The minimum of a finite set of positive numbers is positive, whereas the inf of an infinite set of positive numbers may very well be 0 .)

Now let q and p be points of X such that $\mathrm{d}_{\mathrm{X}}(\mathrm{p}, \mathrm{q})<\delta$. By (4.18), there is an

integer $m, 1 \leq m \leq n$, such that $p \in J\left(p_{m}\right)$; hence

$$
\mathrm{d}_{\mathrm{X}}\left(\mathrm{p}, \mathrm{p}_{\mathrm{m}}\right)<\frac{1}{2} \phi\left(\mathrm{p}_{\mathrm{m}}\right)
$$

and we also have

$$
\mathrm{d}_{\mathrm{X}}\left(\mathrm{q}, \mathrm{p}_{\mathrm{m}}\right) \leq \mathrm{d}_{\mathrm{X}}(\mathrm{p}, \mathrm{q})+\mathrm{d}_{\mathrm{X}}\left(\mathrm{p}, \mathrm{p}_{\mathrm{m}}\right)<\delta+\frac{1}{2} \phi\left(\mathrm{p}_{\mathrm{m}}\right) \leq \phi\left(\mathrm{p}_{\mathrm{m}}\right)
$$

Finally, (4.16) shows that therefore

$$
\mathrm{d}_{\mathrm{Y}}(\mathrm{f}(\mathrm{p}), \mathrm{f}(\mathrm{q})) \leq \mathrm{d}_{\mathrm{Y}}\left(\mathrm{f}(\mathrm{p}), \mathrm{f}\left(\mathrm{p}_{\mathrm{m}}\right)\right)+\mathrm{d}_{\mathrm{Y}}\left(\mathrm{f}(\mathrm{q}), \mathrm{f}\left(\mathrm{p}_{\mathrm{m}}\right)\right)<\varepsilon
$$

This completes the proof.
An alternative proof is sketched in Exercise 4.10.
We now proceed to show that compactness is essential in the hypotheses of Theorems 4.14, 4.15, 4.16, and 4.19.
4.20 Theorem. Let E be a noncompact set in $\mathbb{R}^{1}$. Then
(a) there exists a continuous function on E which is not bounded;
(b) there exists a continuous and bounded function on E which has no maximum.

If, in addition, E is bounded, then
(c) there exists a continuous function on E which is not uniformly continuous.

Proof. Suppose first that E is bounded, so that there exists a limit point $\mathrm{x}_{0}$ of E which is not a point of E. Consider

$$
f(x)=\frac{1}{x-x_{0}} \quad(x \in E)
$$

This is continuous on E (Theorem 4.9), but evidently unbounded. To see that (4.21) is not uniformly continuous, let $\varepsilon>0$ and $\delta>0$ be arbitrary, and choose a point $x \in E$ such that $\left|x-x_{0}\right|<\delta$. Taking $t$ close enough to $x_{0}$, we can then make the difference $|f(t)-f(x)|$ greater than $\varepsilon$, although $|t-x|<\delta$. Since this is true for every $\delta>0, f$ is not uniformly continuous on $E$.

The function $g$ given by

$$
g(x)=\frac{1}{1+\left(x-x_{0}\right)^{2}} \quad(x \in E)
$$

is continuous on $E$ and is bounded, since $0<g(x)<1$. It is clear that

$$
\sup _{x \in E} g(x)=1
$$

whereas $g(x)<1$ for all $x \in E$. Thus $g$ has no maximum on $E$.

Having proved the theorem for bounded sets E , let us now suppose that E is unbounded. Then $f(x)=x$ establishes (a), whereas

$$
h(x)=\frac{x^{2}}{1+x^{2}} \quad(x \in E)
$$

establishes (b), since

$$
\sup _{x \in E} h(x)=1
$$

and $h(x)<1$ for all $x \in E$.
Assertion (c) would be false if boundedness were omitted from the hypotheses. For, let $E$ be the set of all integers. Then every function defined on $E$ is uniformly continuous on E. To see this, we need merely take $\delta<1$ in Definition 4.18.

We conclude this section by showing that compactness is also essential in Theorem 4.17 .
4.21 Example. Let $X$ be the half-open interval $[0,2 \pi)$ on the real line, and let $\mathbf{f}$ be the mapping of $X$ onto the circle $Y$ consisting of all points whose distance from the origin is 1 , given by

$$
\mathbf{f}(\mathrm{t})=(\cos \mathrm{t}, \sin \mathrm{t}) \quad(0 \leq \mathrm{t}<2 \pi)
$$

The continuity of the trigonometric functions cosine and sine, as well as their periodicity properties, will be established in Chap. 8. These results show that $\mathbf{f}$ is a continuous 1-1 mapping of $X$ onto $Y$.

However, the inverse mapping (which exists, since $\mathbf{f}$ is one-to-one and onto) fails to be continuous at the point $(1,0)=\mathbf{f}(0)$. Of course, $X$ is not compact in this example. (It may be of interest to observe that $\mathbf{f}^{-1}$ fails to be continuous in spite of the fact that $Y$ is compact!)

# CONTINUITY AND CONNECTEDNESS 

4.22 Theorem. If f is a continuous mapping of a metric space X into a metric space Y , and if E is a connected subset of X , then $\mathrm{f}(\mathrm{E})$ is connected.

Proof. Assume, on the contrary, that $f(E)=A \cup B$, where $A$ and $B$ are nonempty separated subsets of $Y$. Put $G=E \cap f^{-1}(A), H=E \cap f^{-1}(B)$.

Then $E=G \cup H$, and neither $G$ nor $H$ is empty.
Since $A \subset \bar{A}$ (the closure of $A$ ), we have $G \subset f^{-1}(\bar{A})$; the latter set is closed, since $f$ is continuous; hence $\bar{G} \subset f^{-1}(\bar{A})$. It follows that $f(\bar{G}) \subset \bar{A}$. Since $f(H)=B$ and $\bar{A} \cap B$ is empty, we conclude that $\bar{G} \cap H$ is empty.

The same argument shows that $G \cap \bar{H}$ is empty. Thus $G$ and $H$ are separated. This is impossible if $E$ is connected.

4.23 Theorem. Let f be a continuous real function on the interval $[\mathfrak{a}, \mathrm{b}]$. If $\mathrm{f}(\mathfrak{a})<\mathrm{f}(\mathrm{b})$ and if c is a number such that $\mathrm{f}(\mathfrak{a})<\mathrm{c}<\mathrm{f}(\mathrm{b})$, then there exists a point $\mathrm{x} \in(\mathfrak{a}, \mathrm{b})$ such that $\mathrm{f}(\mathrm{x})=\mathrm{c}$

A similar result holds, of course, if $\mathrm{f}(\mathfrak{a})>\mathrm{f}(\mathrm{b})$. Roughly speaking, the theorem says that a continuous real function assumes all intermediate values on an interval.

Proof. By Theorem 2.47, $[\mathfrak{a}, \mathrm{b}]$ is connected; hence Theorem 4.22 shows that $\mathrm{f}([\mathfrak{a}, \mathrm{b}])$ is a connected subset of $\mathbb{R}^{1}$, and the assertion follows if we appeal once more to Theorem 2.47 .
4.24 Remark. At first glance, it might seem that Theorem 4.23 has a converse. That is, one might think that if for any two points $x_{1}<x_{2}$ and for any number c between $\mathrm{f}\left(\mathrm{x}_{1}\right)$ and $\mathrm{f}\left(\mathrm{x}_{2}\right)$ there is a point x in $\left(\mathrm{x}_{1}, \mathrm{x}_{2}\right)$ such that $\mathrm{f}(\mathrm{x})=\mathrm{c}$, then f must be continuous.

That this is not so may be concluded from Example 4.27(d).

# DISCONTINUITIES 

If x is a point in the domain of definition of the function f at which f is not continuous, we say that f is discontinuous at x , or that f has a discontinuity at x . If f is defined on an interval or on a segment, it is customary to divide discontinuities into two types. Before giving this classification, we have to define the right-hand and the left-hand limits of f at x , which we denote by $\mathrm{f}(\mathrm{x}+)$ and $\mathrm{f}(\mathrm{x}-)$, respectively.
4.25 Definition. Let f be defined on $(\mathfrak{a}, \mathrm{b})$. Consider any point x such that $\mathfrak{a} \leq \mathrm{x}<\mathrm{b}$. We write

$$
f(x+)=q
$$

if $\mathrm{f}\left(\mathrm{t}_{\mathrm{n}}\right) \rightarrow \mathrm{q}$ as $\mathrm{n} \rightarrow \infty$, for all sequences $\left(\mathrm{t}_{\mathrm{n}}\right)$ in $(\mathrm{x}, \mathrm{b})$ such that $\mathrm{t}_{\mathrm{n}} \rightarrow \mathrm{x}$. To obtain the definition of $\mathrm{f}(\mathrm{x}-)$, for $\mathfrak{a}<\mathrm{x} \leq \mathrm{b}$, we restrict ourselves to sequences $\left(\mathrm{t}_{\mathrm{n}}\right)$ in $(\mathfrak{a}, \mathrm{x})$.

It is clear that for any point x of $(\mathfrak{a}, \mathrm{b}), \lim _{\mathrm{t} \rightarrow \mathrm{x}} \mathrm{f}(\mathrm{t})$ exists if and only if

$$
f(x+)=f(x-)=\lim _{t \rightarrow x} f(t)
$$

4.26 Definition. Let f be defined on $(\mathfrak{a}, \mathrm{b})$. If f is discontinuous at a point x , and if $\mathrm{f}(\mathrm{x}+)$ and $\mathrm{f}(\mathrm{x}-)$ exist, then f is said to have a discontinuity of the first kind, or a simple discontinuity, at x . Otherwise the discontinuity is said to be of the second kind.

There are two ways in which a function can have a simple discontinuity: either $\mathrm{f}(\mathrm{x}+) \neq \mathrm{f}(\mathrm{x}-)$ [in which case the value $\mathrm{f}(\mathrm{x})$ is immaterial], or $\mathrm{f}(\mathrm{x}+)=$ $\mathrm{f}(\mathrm{x}-) \neq \mathrm{f}(\mathrm{x})$.

### 4.27 Example.

(a) Define

$$
f(x)= \begin{cases}1 & (\mathrm{x} \text { rational }) \\ 0 & (\mathrm{x} \text { irrational })\end{cases}
$$

Then $f$ has a discontinuity of the second kind at every point $x$ since neither $f(x+)$ nor $f(x-)$ exists.
(b) Define

$$
f(x)= \begin{cases}x & (\mathrm{x} \text { rational }) \\ 0 & (\mathrm{x} \text { irrational })\end{cases}
$$

Then $f$ is continuous at $x=0$ and has a discontinuity of the second kind at every other point.
(c) Define

$$
f(x)= \begin{cases}x+2 & (-3<x<-2) \\ -x-2 & (-2 \leq x<0) \\ x+2 & (0 \leq x<1)\end{cases}
$$

Then $f$ has a simple discontinuity at $x=0$ and is continuous at every other point of $(-3,1)$.
(d) Define

$$
f(x)= \begin{cases}\sin \frac{1}{x} & (x \neq 0) \\ 0 & (x=0)\end{cases}
$$

Since neither $f(0+)$ nor $f(0-)$ exists, $f$ has a discontinuity of the second kind at $x=0$. We have not yet shown that $\sin x$ is a continuous function. If we assume this result for the moment, Theorem 4.7 implies that $f$ is continuous at every point $x \neq 0$.

# MONOTONIC FUNCTIONS 

We shall now study those functions which never decrease (or never increase) on a given segment.
4.28 Definition. Let $f$ be real on $(a, b)$. Then $f$ is said to be monotonically increasing on $(a, b)$ if $a<x<y<b$ implies $f(x) \leq f(y)$. If the last inequality is reversed, we obtain the definition of a monotonically decreasing function. The class of monotonic functions consists of both the increasing and the decreasing functions.
4.29 Theorem. Let f be monotonically increasing on (a, b). Then $\mathrm{f}(\mathrm{x}+)$ and $\mathrm{f}(\mathrm{x}-)$ exist at every point of $x$ of $(a, b)$. More precisely,

$$
\sup _{a<t<x} f(t)=f(x-) \leq f(x) \leq f(x+)=\inf _{x<t<b} f(t)
$$

Furthermore, if $\mathfrak{a}<\mathrm{x}<\mathrm{y}<\mathrm{b}$, then

$$
f(x+) \leq f(y-)
$$

Analogous results evidently hold for monotonically decreasing functions.
Proof. By hypothesis, the set of numbers $f(t)$, where $a<t<x$, is bounded above by the number $f(x)$, and therefore has a least upper bound which we shall denote by $A$. Evidently $A \leq f(x)$. We have to show that $A=f(x-)$.

Let $\varepsilon>0$ be given. It follows from the definition of $A$ as a least upper bound that there exists $\delta>0$ such that $\mathfrak{a}<\mathrm{x}-\delta<\mathrm{x}$ and

$$
A-\varepsilon<f(x-\delta) \leq A
$$

Since $f$ is monotonic, we have

$$
f(x-\delta) \leq f(t) \leq A \quad(x-\delta<t<x)
$$

Combining (4.27) and (4.28), we see that

$$
|f(t)-A|<\varepsilon \quad(x-\delta<t<x)
$$

Hence $f(x-)=A$.
The second half of (4.25) is proved in precisely the same way.
Next, if $\mathfrak{a}<\mathrm{x}<\mathrm{y}<\mathrm{b}$, we see from (4.25) that

$$
f(x+) \stackrel{=}{\inf } x<t<b f(t)=\inf _{x<t<y} f(t)
$$

The last equality is obtained by applying (4.25) to $(\mathfrak{a}, \mathfrak{y})$ in place of $(\mathfrak{a}, \mathfrak{b})$. Similarly,

$$
f(y-)=\sup _{\mathfrak{a}<t<y} f(t)=\sup _{x<t<y} f(t)
$$

Comparison of (4.29) and (4.30) gives (4.26).
Corollary. Monotonic functions have no discontinuities of the second kind.
This corollary implies that every monotonic function is discontinuous at a countable set of points at most. Instead of appealing to the general theorem whose proof is sketched in Exercise 4.17, we give here a simple proof which is applicable to monotonic functions.
4.30 Theorem. Let f be monotonic on $(\mathfrak{a}, \mathfrak{b})$. Then the set of points of $(\mathfrak{a}, \mathfrak{b})$ at which f is discontinuous is at most countable.

Proof. Suppose, for the sake of definiteness, that $f$ is increasing, and let $E$ be the set of points at which $f$ is discontinuous.

With every point $x$ of $E$ we associate a rational number $r(x)$ such that

$$
f(x-)<r(x)<f(x+)
$$

Since $x_{1}<x_{2}$ implies $f\left(x_{1}+\right) \leq f\left(x_{2}-\right)$, we see that $r\left(x_{1}\right) \neq r\left(x_{2}\right)$ if $x_{1} \neq x_{2}$.
We have thus established a 1-1 correspondence between the set E and a subset of the set of rational numbers. The latter, as we know, is countable.
4.31 Remark. It should be noted that the discontinuities of a monotonic function need not be isolated. In fact, given any countable subset $E$ of ( $a, b$ ), which may even be dense, we can construct a function $f$, monotonic on ( $a, b$ ), discontinuous at every point of $E$, and at no other point of $(a, b)$.

To show this, let the points of $E$ be arranged in a sequence $\left(x_{n}\right), n=1,2,3, \ldots$ Let $\left(c_{n}\right)$ be a sequence of positive numbers such that $\sum c_{n}$ converges. Define

$$
f(x)=\sum_{x_{n}<x} c_{n} \quad(a<x<b)
$$

The summation is to be understood as follows: Sum over those indices $n$ for which $x_{n}<x$. If there are no points $x_{n}$ to the left of $x$, the sum is empty; following the usual convention, we define it to be zero. Since (4.31) converges absolutely, the order in which the terms are arranged is immaterial.

We leave the verification of the following properties $f$ to the reader:
(a) $f$ is monotonically increasing on $(a, b)$;
(b) $f$ is discontinuous at every point of $E$; in fact,

$$
f\left(x_{n}+\right)-f\left(x_{n}-\right)=c_{n}
$$

(c) $f$ is continuous at every other point of $(a, b)$.

Moreover, it is not hard to see that $f(x-)=f(x)$ at all points of $(a, b)$. If a function satisfies this condition, we say that $f$ is continuous from the left. If the summation in (4.31) were taken over all indices $n$ for which $x_{n} \leq x$, we would have $f(x+)=f(x)$ at every point of $(a, b)$; that is, $f$ would be continuous from the right.

Functions of this sort can also be defined by another method; for an example we refer to Theorem 6.16.

# INFINITE LIMITS AND LIMITS AT INFINITY 

To enable us to operate in the extended real number system, we shall now enlarge the scope of Definition 4.1 by reformulating it in terms of neighborhoods.

For any real number $x$, we have already defined a neighborhood of $x$ to be any segment $(x-\delta, x+\delta)$.

4.32 Definition. For any real $c$, the set of real numbers $x$ such that $x>c$ is called a neighborhood of $+\infty$ and is written $(c,+\infty)$. Similarly, the set $(-\infty, c)$ is a neighborhood of $-\infty$.
4.33 Definition. Let $f$ be a real function defined on $E \subset \mathbb{R}$. We say that

$$
f(t) \rightarrow A \text { as } t \rightarrow x
$$

where $A$ and $x$ are in the extended real number system, if for every neighborhood $U$ of $A$ there is a neighborhood $V$ of $x$ such that $V \cap E$ is not empty, and such that $f(t) \in U$ for all $t \in V \cap E, t \neq x$.

A moment's consideration will show that this coincides with Definition 4.1 when $A$ and $x$ are real.

The analogue of Theorem 4.4 is still true, and the proof offers nothing new. We state it, for the sake of completeness.
4.34 Theorem. Let f and g be defined on $\mathrm{E} \subset \mathbb{R}$. Suppose

$$
f(t) \rightarrow A, \quad g(t) \rightarrow B \quad \text { as } t \rightarrow x
$$

Then
(a) $f(t) \rightarrow A^{\prime}$ implies $A^{\prime}=A$,
(b) $(f+g)(t) \rightarrow A+B$,
(c) $(\mathrm{fg})(\mathrm{t}) \rightarrow \mathrm{AB}$,
(d) $(\mathrm{f} / \mathrm{g})(\mathrm{t}) \rightarrow \mathrm{A} / \mathrm{B}$,
provided the right members of (b), (c), and (d) are defined.
Note that $\infty-\infty, 0 \cdot \infty, \infty / \infty$, and $A / 0$ are not defined (see 1.23).

# EXERCISES 

4.1. Suppose $f$ is a real function defined on $\mathbb{R}^{1}$ which satisfies

$$
\lim _{h \rightarrow 0}[f(x+h)-f(x-h)]=0
$$

for every $x \in \mathbb{R}^{1}$. Does this imply that $f$ is continuous?
4.2. If $f$ is a continuous mapping of a metric space $X$ into a metric space $Y$, prove that

$$
f(\overline{\mathrm{E}}) \subset \overline{\mathrm{f}(\mathrm{E})}
$$

for every set $E \subset X$. ( $\bar{E}$ denotes the closure of $E$.) Show, by an example, that $f(\bar{E})$ can be a proper subset of $\overline{\mathrm{f}(\mathrm{E})}$.
4.3. Let $f$ be a continuous real function on a metric space $X$. Let $Z(f)$ (the zero set of $f$ ) be the set of all $p \in X$ at which $f(p)=0$. Prove that $Z(f)$ is closed.
4.4. Let $f$ and $g$ be continuous mappings of a metric space $X$ into a metric space $Y$, and let $E$ be a dense subset of $X$. Prove that $f(E)$ is dense in $f(X)$. If $g(p)=f(p)$ for all $p \in E$, prove that

$g(p)=f(p)$ for all $p \in X$ (In other words, a continuous function is determined by its values on a dense subset of its domain.)
4.5. If $f$ is a real continuous function defined on a closed set $E \subset \mathbb{R}^{1}$, prove that there exist continuous real functions on $\mathbb{R}^{1}$ such that $g(x)=f(x)$ for all $x \in E$. (Such functions $g$ are called continuous extensions of $f$ from $E$ to $\mathbb{R}^{1}$.) Show that the result becomes false if the world "closed" is omitted. Extend the result to vector-valued functions. Hint: Let the graph of $g$ be a straight line on each of the segments which constitute the complement of $E$ (compare Exercise 2.29). The result remains true if $\mathbb{R}^{1}$ is replaced by any metric space, but the proof is not so simple.
4.6. If $f$ is defined on $E$, the graph of $f$ is the set of points $(x, f(x))$, for $x \in E$. In particular, if $E$ is a set of real numbers and $f$ is real-valued, the graph of $f$ is a subset of the plane.

Suppose $E$ is compact and prove that $f$ is continuous on $E$ if and only if its graph is compact.
4.7. If $E \subset X$ and if $f$ is a function defined on $X$, the restriction of $f$ to $E$ is the function $g$ whose domain of definition is $E$, such that $g(p)=f(p)$ for $p \in E$. Define $f$ and $g$ on $\mathbb{R}^{2}$ by: $f(0,0)=g(0,0)=0, f(x, y)=x y^{2} /\left(x^{2}+y^{4}\right), g(x, y)=x y^{2} /\left(x^{2}+y^{6}\right)$ if $(x, y) \neq(0,0)$. Prove that $f$ is bounded on $\mathbb{R}^{2}$, that $g$ is unbounded in every neighborhood of $(0,0)$, and that $f$ is not continuous at $(0,0)$; nevertheless, the restrictions of both $f$ and $g$ to every straight line in $\mathbb{R}^{2}$ are continuous!
4.8. Let $f$ be a real uniformly continuous function on the bounded set $E$ in $\mathbb{R}^{1}$. Prove that $f$ is bounded on $E$. Show that the conclusion is false if the boundedness of $E$ is omitted from the hypothesis.
4.9. Show that the requirement in the definition of uniform continuity can be rephrased as follows, in terms of diameters of sets: To every $\varepsilon>0$, there exists a $\delta>0$ such that diam $f(E)<\varepsilon$ for all $E \subset X$ with diam $E<\delta$.
4.10. Complete the details of the following alternative proof of Theorem 4.19: If $f$ is not uniformly continuous, then for some $\varepsilon>0$ there are sequences $\left(p_{n}\right),\left(q_{n}\right)$ in $X$ such that $d_{X}\left(p_{n}, q_{n}\right) \rightarrow 0$ but $d_{Y}\left(f\left(p_{n}\right), f\left(q_{n}\right)\right)>\varepsilon$. Use Theorem 2.37 to obtain a contradiction.
4.11. Suppose $f$ is a uniformly continuous mapping of a metric space $X$ into a metric space $Y$ and prove that $\left(f\left(x_{n}\right)\right)$ is a Cauchy sequence in $Y$ for every Cauchy sequence $\left(x_{n}\right)$ in $X$. Use this result to give an alternative proof of the theorem stated in Exercise 4.13.
4.12. A uniformly continuous function of a uniformly continuous function is uniformly continuous. State this more precisely and prove it.
4.13. Let $E$ be a dense subset of a metric space $X$, and let $f$ be a uniformly continuous real function defined on E. Prove that $f$ has a continuous extension from $E$ to $X$ (see Exercise 4.5 for terminology). (Uniqueness follows from Exercise 4.4.) Hint: For each $p \in X$ and each positive integer $n$, let $V_{n}(p)$ be the set of all $q \in E$ with $d(p, q)<1 / n$. Use Exercise 4.9 to show that the intersection of the closures of the sets $f\left(V_{1}(p)\right), f\left(V_{2}(p)\right), \ldots$ consists of a single point, say $g(p)$, of $\mathbb{R}^{1}$. Prove that the function $g$ so defined on $X$ is the desired extension of $f$.

Could the range space $\mathbb{R}^{1}$ be replaced by $\mathbb{R}^{k}$ ? By any compact metric space? By any complete metric space? By any metric space?
4.14. Let $I=\{0,1\}$ be the closed unit interval. Suppose $f$ is a continuous mapping of $I$ into $I$. Prove that $f(x)=x$ for at least one $x \in I$.
4.15. Call a mapping of $X$ into $Y$ open if $f(V)$ is an open set in $Y$ whenever $V$ is an open set in X. Prove that every continuous open mapping of $\mathbb{R}^{1}$ into $\mathbb{R}^{1}$ is monotonic.
4.16. Let $[x]$ denote the largest integer contained in $x$, that is, $[x]$ is the integer such that $x-1<$ $[x] \leq x$, and let $(x)=x-[x]$ denote the fractional part of $x$. What discontinuities do the functions $[x]$ and $(x)$ have?

4.17. Let $f$ be a real function defined on $(a, b)$. Prove that the set of points at which $f$ has a simple discontinuity is at most countable. Hint: Let E be the set on which $f(x-)<f(x+)$. With each point $x$ of $E$, associate a triple $(p, q, r)$ of rational numbers such that
(a) $f(x-)<p<f(x+)$,
(b) $a<q<t<x$ implies $f(t)<p$,
(c) $x<t<r<b$ implies $f(t)>p$.

The set of all such triples is countable. Show that each triple is associated with at most one point of E. Deal similarly with the other possible types of simple discontinuities.
4.18. Every rational $x$ can be written in the form $x=m / n$, where $n>0$, and $m$ and $n$ are integers without any common divisors. When $x=0$, we take $n=1$. Consider the function $f$ defined on $\mathbb{R}^{1}$ by

$$
f(x)=\left\{\begin{array}{lr}
0 & (x \text { irrational }) \\
\frac{1}{n} & \left(x=\frac{m}{n}\right)
\end{array}\right.
$$

Prove that $f$ is continuous at every irrational point, and that $f$ has a simple discontinuity at every rational point.
4.19. Suppose $f$ is a real function with domain $\mathbb{R}^{1}$ which has the intermediate value property: If $f(a)<c<f(b)$, then $f(x)=c$ for some $x$ between $a$ and $b$. Suppose also, for every rational $r$, that the set of all $x$ with $f(x)=r$ is closed. Prove that $f$ is continuous.

Hint: If $x_{n} \rightarrow x_{0}$ but $f\left(x_{n}\right)>r>f\left(x_{0}\right)$ for some $r$ and all $n$, then $f\left(t_{n}\right)=r$ for some $t_{n}$ between $x_{0}$ and $x_{n}$; thus $t_{n} \rightarrow x_{0}$. Find a contradiction. (N.J. Fine, Ameri. Math. Monthly, vol. 73, 1966, p. 782 [GF66]).
4.20. If $E$ is a nonempty subset of a metric space $X$, define the distance from $x \in X$ to $E$ by

$$
\rho_{E}(x)=\inf _{z \in \bar{E}} d(x, z)
$$

(a) Prove that $\rho_{E}(x)=0$ if and only if $x \in \bar{E}$.
(b) Prove that $\rho_{E}$ is a uniformly continuous function on $X$ by showing that

$$
\left|\rho_{E}(x)-\rho_{E}(y)\right| \leq d(x, y)
$$

for all $x \in X, y \in X$.
Hint: $\rho_{E}(x) \leq d(x, z) \leq d(x, y)+d(y, z)$, so that

$$
\rho_{E}(x) \leq d(x, y)+\rho_{E}(y)
$$

4.21. Suppose $K$ and $F$ are disjoint sets in a metric space $X, K$ is compact, $F$ is closed. Prove that there exists $\delta>0$ such that $d(p, q)>\delta$ if $p \in K, q \in F$. Hint: $p_{F}$ is a continuous positive function on $K$.

Show that the conclusion may fail for two disjoint closed sets if neither is compact.
4.22. Let $A$ and $B$ be disjoint nonempty closed sets in a metric space $X$, and define

$$
f(p)=\frac{\rho_{A}(p)}{\rho_{A}(p)+\rho_{B}(p)} \quad(p \in X)
$$

Show that $f$ is a continuous function on $X$ whose range lies in $[0,1]$, that $f(p)=0$ precisely on $A$ and $f(p)=1$ precisely on $B$. This establishes a converse of Exercise 4.3: Every closed set $A \subset X$ is $Z(f)$ for some continuous real $f$ on $X$. Setting

$$
V=f^{-1}((0,1 / 2)), \quad W=f^{-1}((1 / 2,1))
$$

show that $V$ and $W$ are open and disjoint, and that $A \subset V, B \subset W$. (Thus pairs of disjoint closed sets in metric spaces can be covered by pairs of disjoint open sets. This property of metric spaces is called normality.)

4.23. A real-valued function $f$ defined in $(a, b)$ is said to be convex if

$$
f(\lambda x+(1-\lambda) y) \leq \lambda f(x)+(1-\lambda) f(y)
$$

whenever $a<x<b, a<y<b$, and $0<\lambda<1$. Prove that every convex function is continuous. Prove that every increasing convex function of a convex function is convex. (For example, if $f$ is convex, so is $e^{f}$.)

If $f$ is convex in $(a, b)$ and if $a<s<t<u<b$, show that

$$
\frac{f(t)-f(s)}{t-s} \leq \frac{f(u)-f(s)}{u-s} \leq \frac{f(u)-f(t)}{u-t}
$$

4.24. Assume that $f$ is a continuous real function defined in $(a, b)$ such that

$$
f\left(\frac{x+y}{2}\right) \leq \frac{f(x)+f(y)}{2}
$$

for all $x, y \in(a, b)$. Prove that $f$ is convex.
4.25. If $A \subset \mathbb{R}^{k}$ and $B \subset \mathbb{R}^{k}$, define $A+B$ to be the set of all sums $x+y$ with $x \in A, y \in B$.
(a) If $K$ is compact and $C$ is closed in $\mathbb{R}^{k}$, prove that $K+C$ is closed.

Hint: Take $\mathbf{z} \notin K+C$, put $F=\mathbf{z}-C$, the set of all $\mathbf{z}-\mathbf{y}$ with $\mathbf{y} \in C$. Then $K$ and $F$ are disjoint. Choose $\delta$ as in Exercise 4.21. Show that the open ball with center $\mathbf{z}$ and radius $\delta$ does not intersect $K+C$.
(b) Let $\alpha$ be an irrational real number. Let $C_{1}$ be the set of all integers, let $C_{2}$ be the set of all $n \alpha$ with $n \in C_{1}$. Show that $C_{1}$ and $C_{2}$ are closed subsets of $\mathbb{R}^{1}$ whose sum $C_{1}+C_{2}$ is not closed, by showing that $C_{1}+C_{2}$ is a countable dense subset of $\mathbb{R}^{1}$.
4.26. Suppose $X, Y, Z$ are metric spaces, and $Y$ is compact. Let $f$ map $X$ into $Y$, let $g$ be a continuous one-to-one mapping of $Y$ into $Z$, and put $h(x)=g(f(x))$ for $x \in X$. Prove that $f$ is uniformly continuous if $h$ is uniformly continuous. Hint: $g^{-1}$ has compact domain $g(Y)$, and $f(x)=g^{-1}(h(x))$.

Prove also that $f$ is continuous if $h$ is continuous. Show (by modifying Example 4.21, or by finding a different example) that the compactness of $Y$ cannot be omitted from the hypotheses, even when $X$ and $Z$ are compact.

# Chapter 5 

## DIFFERENTIATION

In this chapter we shall (except in the final section) confine our attention to real functions defined on intervals or segments. This is not just a matter of convenience, since genuine differences appear when we pass from real functions to vector-valued ones. Differentiation of functions defined on $\mathbb{R}^{\mathrm{k}}$ will be discussed in Chap. 9.

## THE DERIVATIVE OF A REAL FUNCTION

5.1 Definition. Let $f$ be defined (and real-valued) on $[a, b]$. For any $x \in[a, b]$, form the quotient

$$
\phi(t)=\frac{f(t)-f(x)}{t-x} \quad(a<t<b, t \neq x)
$$

and define

$$
f^{\prime}(x)=\lim _{t \rightarrow x} \phi(t)
$$

provided this limit exists in accordance with Definition 4.1.
We thus associate with the function $f$ a function $f^{\prime}$ whose domain is the set of points $x$ at which the limit (5.2) exists; $f^{\prime}$ is called the derivative of $f$.

If $f^{\prime}$ is defined at a point $x$, we say that $f$ is differentiable at $x$. If $f^{\prime}$ is defined at every point of a set $E \subset[a, b]$, we say that $f$ is differentiable on $E$.

It is possible to consider right-hand and left-hand limits in (5.2); this leads to the definition of right-hand and left-hand derivatives. In particular, at the endpoints $a$ and $b$, the derivative, if it exists, is a right-hand or left-hand derivative, respectively. We shall not, however, discuss one-sided derivatives in any detail.

If $f$ is defined on a segment $(a, b)$ and if $a<x<b$, then $f^{\prime}(x)$ is defined by (5.1) and (5.2), as above. But $f^{\prime}(a)$ and $f^{\prime}(b)$ are not defined in this case.

5.2 Theorem. Let f be defined on [a, b]. If f is differentiable at a point $\mathrm{x} \in[\mathrm{a}, \mathrm{b}]$, then f is continuous at x .

Proof. As $\mathrm{t} \rightarrow \mathrm{x}$, we have, by Theorem 4.4,

$$
f(t)-f(x)=\frac{f(t)-f(x)}{t-x} \cdot(t-x) \rightarrow f^{\prime}(x) \cdot 0=0
$$

The converse of this theorem is not true. It is easy to construct continuous functions which fail to be differentiable at isolated points. In Chap. 7 we shall even become acquainted with a function which is continuous on the whole line without being differentiable at any point!
5.3 Theorem. Suppose f and g are defined on [a, b] and are differentiable at a point $\mathrm{x} \in[\mathrm{a}, \mathrm{b}]$. Then $\mathrm{f}+\mathrm{g}, \mathrm{fg}$, and $\mathrm{f} / \mathrm{g}$ are differentiable at x , and
(a) $(\mathrm{f}+\mathrm{g})^{\prime}(\mathrm{x})=\mathrm{f}^{\prime}(\mathrm{x})+\mathrm{g}^{\prime}(\mathrm{x})$;
(b) $(\mathrm{fg})^{\prime}(\mathrm{x})=\mathrm{f}^{\prime}(\mathrm{x}) \mathrm{g}(\mathrm{x})+\mathrm{f}(\mathrm{x}) \mathrm{g}^{\prime}(\mathrm{x})$;
(c) $\left(\frac{\mathrm{f}}{\mathrm{g}}\right)^{\prime}(\mathrm{x})=\frac{\mathrm{g}(\mathrm{x}) \mathrm{f}^{\prime}(\mathrm{x})-\mathrm{g}^{\prime}(\mathrm{x}) \mathrm{f}(\mathrm{x})}{\mathrm{g}^{2}(\mathrm{x})}$.

In (c), we assume of course that $\mathrm{g}(\mathrm{x}) \neq 0$.
Proof. (a) is clear, by Theorem 4.4. Let $\mathrm{h}=\mathrm{fg}$. Then

$$
h(t)-h(x)=f(t)[g(t)-g(x)]+g(x)[f(t)-f(x)]
$$

If we divide this by $t-x$ and note that $f(t) \rightarrow f(x)$ as $t \rightarrow x$ (Theorem 5.2), (b) follows. Next, let $h=f / g$. Then

$$
\frac{h(t)-h(x)}{t-x}=\frac{1}{g(t) g(x)}\left[g(x) \frac{f(t)-f(x)}{t-x}-f(x) \frac{g(t)-g(x)}{t-x}\right]
$$

Letting $t \rightarrow x$, and applying Theorems 4.4 and 5.2, we obtain (c).
5.4 Examples. The derivative of any constant is clearly zero. If $f$ is defined by $f(x)=x$, then $f^{\prime}(x)=1$. Repeated application of (b) and (c) then shows that $x^{n}$ is differentiable, and that its derivative is $n x^{n-1}$ for any integer $n$ (if $n<0$, we have to restrict ourselves to $\mathrm{x} \neq 0$ ). Thus every polynomial is differentiable and so is every rational function, except at the points where the denominator is zero.

The following theorem is known as the "chain rule" for differentiation. It deals with differentiation of composite functions and is probably the most important theorem about derivatives. We shall meet more general versions of it in Chap. 9.
5.5 Theorem. Suppose f is continuous on [a, b], $\mathrm{f}^{\prime}(\mathrm{x})$ exists at some point $\mathrm{x} \in[\mathrm{a}, \mathrm{b}], \mathrm{g}$ is defined on an interval I which contains the range of f , and g is differentiable at the point $\mathrm{f}(\mathrm{x})$. If

$$
h(t)=g(f(t)) \quad(a \leq t \leq b)
$$

then h is differentiable at x , and

$$
\mathrm{h}^{\prime}(\mathrm{x})=\mathrm{g}^{\prime}(\mathrm{f}(\mathrm{x})) \mathrm{f}^{\prime}(\mathrm{x})
$$

Proof. Let $y=f(x)$. By the definition of the derivative, we have

$$
\begin{aligned}
f(t)-f(x) & =(t-x)\left|f^{\prime}(x)+u(t)\right| \\
g(s)-g(y) & =(s-y)\left[g^{\prime}(y)+v(s)\right]
\end{aligned}
$$

where $t \in[a, b], s \in I$, and $u(t) \rightarrow 0$ as $t \rightarrow x, v(s) \rightarrow 0$ as $s \rightarrow y$. Let $s=f(t)$. Using first (5.5) and then (5.4), we obtain

$$
\begin{aligned}
h(t)-h(x) & =g(f(t))-g(f(x)) \\
& =[f(t)-f(x)] \cdot\left[g^{\prime}(y)+v(s)\right] \\
& =(t-x) \cdot\left[f^{\prime}(x)+u(t)\right] \cdot\left[g^{\prime}(y)+v(s)\right]
\end{aligned}
$$

or, if $t \neq x$,

$$
\frac{h(t)-h(x)}{t-x}=\left[g^{\prime}(y)+v(s)\right] \cdot\left[f^{\prime}(x)+u(t)\right]
$$

Letting $t \rightarrow x$, we see that $s \rightarrow y$, by the continuity of $f$, so that the right side of (5.6) tends to $g^{\prime}(y) f^{\prime}(x)$, which gives (5.3).

# 5.6 Examples. 

(a) Let $f$ be defined by

$$
f(x)= \begin{cases}x \sin \frac{1}{x} & (x \neq 0) \\ 0 & (x=0)\end{cases}
$$

Taking for granted that the derivative of $\sin x$ is $\cos x$ (we shall discuss the trigonometric functions in Chap. 8), we can apply Theorems 5.3 and 5.5 whenever $x \neq 0$, and obtain

$$
f^{\prime}(x)=\sin \frac{1}{x}-\frac{1}{x} \cos \frac{1}{x} \quad(x \neq 0)
$$

At $x=0$, these theorems do not apply any longer, since $1 / x$ is not defined there, and we appeal directly to the definition: for $t \neq 0$,

$$
\frac{f(t)-f(0)}{t-0}=\sin \frac{1}{t}
$$

As $t \rightarrow 0$, this does not tend to any limit, so that $f^{\prime}(0)$ does not exist.

(b) Let $f$ be defined by

$$
f(x)= \begin{cases}x^{2} \sin \frac{1}{x} & (x \neq 0) \\ 0 & (x=0)\end{cases}
$$

As above, we obtain

$$
f^{\prime}(x)=2 x \sin \frac{1}{x}-\cos \frac{1}{x} \quad(x \neq 0)
$$

At $x=0$, we appeal to the definition, and obtain

$$
\left|\frac{f(t)-f(0)}{t-0}\right|=\left|t \sin \frac{1}{t}\right| \leq|t| \quad(t \neq 0)
$$

letting $t \rightarrow 0$, we see that

$$
f^{\prime}(0)=0
$$

Thus $f$ is differentiable at all points $x$, but $f^{\prime}$ is not a continuous function, since $\cos (1 / x)$ in (5.10) does not tend to a limit as $x \rightarrow 0$.

# MEAN VALUE THEOREMS 

5.7 Definition. Let $f$ be a real function defined on a metric space $X$. We say that $f$ has a local maximum at a point $\mathrm{p} \in \mathrm{X}$ if there exists $\delta>0$ such that $\mathrm{f}(\mathrm{q}) \leq \mathrm{f}(\mathrm{p})$ for all $\mathrm{q} \in \mathrm{X}$ with $\mathrm{d}(\mathrm{p}, \mathrm{q})<\delta$. Local minima are defined likewise.

Our next theorem is the basis of many applications of differentiation.
5.8 Theorem. Let f be defined on [a,b]; if f has a local maximum at a point $x \in(a, b)$ and if $f^{\prime}(x)$ exists, then $f^{\prime}(x)=0$.

The analogous statement for local minima is of course true.
Proof. Choose $\delta$ in accordance with Definition 5.7, so that

$$
a<x-\delta<x<x+\delta<b
$$

If $x-\delta<t<x$, then

$$
\frac{f(t)-f(x)}{t-x} \geq 0
$$

Letting $t \rightarrow x$, we see that $f^{\prime}(x) \geq 0$.
If $x<t<x+\delta$, then

$$
\frac{f(t)-f(x)}{t-x} \leq 0
$$

which shows that $f^{\prime}(x) \leq 0$. Hence $f^{\prime}(x)=0$.

5.9 Theorem. If $f$ and $g$ are continuous real functions on $[a, b]$ which are differentiable on $(\mathfrak{a}, \mathfrak{b})$, then there is a point $\mathrm{x} \in(\mathfrak{a}, \mathfrak{b})$ at which

$$
[f(b)-f(\mathfrak{a})] g^{\prime}(\mathrm{x})=[g(b)-g(\mathfrak{a})] f^{\prime}(\mathrm{x})
$$

Note that differentiability is not required at the endpoints.
Proof. Put

$$
h(t)=[f(b)-f(\mathfrak{a})] g(t)-[g(b)-g(\mathfrak{a})] f(t) \quad(\mathfrak{a} \leq \mathfrak{t} \leq \mathfrak{b})
$$

Then $h$ is continuous on $[\mathfrak{a}, \mathfrak{b}], \mathrm{h}$ is differentiable on $(\mathfrak{a}, \mathfrak{b})$, and

$$
h(\mathfrak{a})=f(\mathfrak{b}) g(\mathfrak{a})-f(\mathfrak{a}) g(\mathfrak{b})=h(\mathfrak{b})
$$

To prove the theorem, we have to show that $h^{\prime}(x)=0$ for some $x \in(\mathfrak{a}, \mathfrak{b})$.
If $h$ is a constant, this holds for every $x \in(a, b)$. If $h(t)>h(a)$ for some $t \in(a, b)$, let $x$ be a point in $[a, b]$ at which $h$ attains its maximum (Theorem 4.16). By (5.12), $x \in(a, b)$, and Theorem 5.8 shows that $h^{\prime}(x)=0$. If $h(t)<h(a)$ for some $t \in(a, b)$, the same argument applies if we choose for $x$ a point on $[a, b]$ where $h$ attains its minimum.

This theorem is often called a generalized mean value theorem; the following special case is usually referred to as "the" mean value theorem:
5.10 Theorem. If $f$ is a real continuous function on $[a, b]$ which is differentiable on $(a, b)$, then there is a point $\mathrm{x} \in(\mathfrak{a}, \mathfrak{b})$ at which

$$
f(b)-f(a)=(b-a) f^{\prime}(x)
$$

Proof. Take $g(x)=x$ in Theorem 5.9
5.11 Theorem. Suppose $f$ is differentiable on $(\mathfrak{a}, \mathfrak{b})$.
(a) If $f^{\prime}(x) \geq 0$ for all $x \in(a, b)$, then $f$ is monotonically increasing.
(b) If $f^{\prime}(x)=0$ for all $x \in(a, b)$, then $f$ is constant.
(c) If $f^{\prime}(x) \leq 0$ for all $x \in(a, b)$, then $f$ is monotonically decreasing.

Proof. All conclusions can be read off from the equation

$$
f\left(x_{2}\right)-f\left(x_{1}\right)=\left(x_{2}-x_{1}\right) f^{\prime}(x)
$$

which is valid, for each pair of numbers $x_{1}, x_{2}$ in $(a, b)$, for some $x$ between $x_{1}$ and $\mathrm{x}_{2}$.

# THE CONTINUITY OF DERIVATIVES 

We have already seen [Example 5.6(b)] that a function f may have a derivative $\mathrm{f}^{\prime}$ which exists at every point but is discontinuous at some point. However, not every function is a derivative. In particular, derivatives which exist at every point of an interval have one important property in common with functions which are continuous on an interval: Intermediate values are assumed (compare Theorem 4.23). The precise statement follows.
5.12 Theorem. Suppose f is a real differentiable function on $[\mathfrak{a}, \mathfrak{b}]$ and suppose $\mathrm{f}^{\prime}(\mathfrak{a})<$ $\lambda<\mathrm{f}^{\prime}(\mathfrak{b})$. Then there is a point $\mathrm{x} \in(\mathfrak{a}, \mathfrak{b})$ such that $\mathrm{f}^{\prime}(\mathrm{x})=\lambda$.

A similar result holds of course if $f^{\prime}(\mathfrak{a})>f^{\prime}(\mathfrak{b})$.
Proof. Put $\mathrm{g}(\mathrm{t})=\mathrm{f}(\mathrm{t})-\lambda \mathrm{t}$. Then $\mathrm{g}^{\prime}(\mathfrak{a})<0$ so that $\mathrm{g}\left(\mathrm{t}_{1}\right)<\mathrm{g}(\mathfrak{a})$ for some $\mathrm{t}_{1} \in$ $(\mathfrak{a}, \mathfrak{b})$ and $\mathrm{g}^{\prime}(\mathfrak{b})>0$, so that $\mathrm{g}\left(\mathrm{t}_{2}\right)<\mathrm{g}(\mathfrak{b})$ for some $\mathrm{t}_{2} \in(\mathfrak{a}, \mathfrak{b})$. Hence g attains its minimum on $[\mathfrak{a}, \mathfrak{b}]$ (Theorem 4.16) at some point x such that $\mathfrak{a}<\mathrm{x}<\mathfrak{b}$. By Theorem 5.8, $\mathrm{g}^{\prime}(\mathrm{x})=0$. Hence $\mathrm{f}^{\prime}(\mathrm{x})=\lambda$.

Corollary. If f is differentiable on $[\mathfrak{a}, \mathfrak{b}]$, then $\mathrm{f}^{\prime}$ cannot have any simple discontinuities on $[\mathfrak{a}, \mathfrak{b}]$.

But $f^{\prime}$ may very well have discontinuities of the second kind.

## L'HÔSPITAL'S RULE

The following theorem is frequently used in the evaluation of limits.
5.13 Theorem. Suppose f and g are real and differentiable on $(\mathfrak{a}, \mathfrak{b})$, and $\mathrm{g}^{\prime}(\mathrm{x}) \neq 0$ for all $\mathrm{x} \in(\mathfrak{a}, \mathfrak{b})$, where $-\infty \leq \mathfrak{a}<\mathfrak{b} \leq+\infty$. Suppose

$$
\frac{\mathrm{f}^{\prime}(\mathrm{x})}{\mathrm{g}^{\prime}(\mathrm{x})} \rightarrow \mathrm{A} \text { as } \mathrm{x} \rightarrow \mathfrak{a}
$$

If

$$
f(x) \rightarrow 0 \text { and } g(x) \rightarrow 0 \text { as } x \rightarrow a
$$

or if

$$
g(x) \rightarrow+\infty \text { as } x \rightarrow a
$$

then

$$
\frac{f(x)}{g(x)} \rightarrow A \text { as } x \rightarrow a
$$

The analogous statement is of course also true if $x \rightarrow b$, or if $g(x) \rightarrow-\infty$ in (5.15). Let us note that we now use the limit concept in the extended sense of Definition 4.33

Proof. We first consider the case in which $-\infty \leq A<+\infty$. Choose a real number $q$ such that $A<q$, and then choose $r$ such that $A<r<q$. By (5.13) there is a point $\mathrm{c} \in(\mathrm{a}, \mathrm{b})$ such that $\mathrm{a}<\mathrm{x}<\mathrm{c}$ implies

$$
\frac{f^{\prime}(x)}{g^{\prime}(x)}<r
$$

If $a<x<y<c$, then Theorem 5.9 shows that there is a point $t \in(x, y)$ such that

$$
\frac{f(x)-f(y)}{g(x)-g(y)}=\frac{f^{\prime}(t)}{g^{\prime}(t)}<r
$$

Suppose (5.14) holds. Letting $x \rightarrow a$ in (5.18), we see that

$$
\frac{f(y)}{g(y)} \leq r<q \quad(a<y<c)
$$

Next, suppose (5.15) holds. Keeping $y$ fixed in (5.18), we can choose a point $c_{1} \in$ $(a, y)$ such that $g(x)>g(y)$ and $g(x)>0$ if $a<x<c_{1}$. Multiplying (5.18) by $[g(x)-g(y)] / g(x)$, we obtain

$$
\frac{f(x)}{g(x)}<r-r \frac{g(y)}{g(x)}+\frac{f(y)}{g(x)} \quad\left(a<x<c_{1}\right)
$$

If we let $x \rightarrow a$ in (5.20), (5.15) shows that there is a point $c_{2} \in\left(a, c_{1}\right)$ such that

$$
\frac{f(x)}{g(x)}<q \quad\left(a<x<c_{2}\right)
$$

Summing up, (5.19) and (5.21) show that for any $q$, subject only to the condition $A<q$, there is a point $c_{2}$ such that $f(x) / g(x)<q$ if $a<x<c_{2}$.

In the same manner, if $-\infty<A \leq+\infty$ and $p$ is chosen so that $p<A$, we can find a point $c_{3}$ such that

$$
p<\frac{f(x)}{g(x)} \quad\left(a<x<c_{3}\right)
$$

and (5.16) follows from these two statements.

# DERIVATIVES OF HIGHER ORDER 

5.14 Definition. If $f$ has a derivative $f^{\prime}$ on an interval, and if $f^{\prime}$ is itself differentiable, we denote the derivative of $f^{\prime}$ by $f^{\prime \prime}$ and call $f^{\prime \prime}$ the second derivative of $f$.

Continuing in this manner, we obtain functions

$$
f, f^{\prime}, f^{\prime \prime}, f^{(3)}, \ldots, f^{(n)}
$$

each of which is the derivative of the preceding one. $f^{(n)}$ is called the $n$th derivative of $f$, or the derivative of order $n$, of $f$.

In order for $f^{(n)}(x)$ to exist at a point $x, f^{(n-1)}(t)$ must exist in a neighborhood of $x$ (or in a one-sided neighborhood, if $x$ is an endpoint of the interval on which $f$ is defined), and $f^{(n-1)}$ must be differentiable at $x$. Since $f^{(n-1)}$ must exist in a neighborhood of $x, f^{(n-2)}$ must be differentiable in that neighborhood.

# TAYLOR'S THEOREM 

5.15 Theorem. Suppose $f$ is a real function on $[a, b], n$ is a positive integer, $f^{(n-1)}$ is continuous on $[a, b], f^{(n)}(t)$ exists for every $t \in(a, b)$. Let $\alpha, \beta$ be distinct points of $[a, b]$, and define

$$
P(t)=\sum_{k=0}^{n-1} \frac{f^{(k)}(\alpha)}{k!}(t-\alpha)^{k}
$$

Then there exists a point $x$ between $\alpha$ and $\beta$ such that

$$
f(\beta)=P(\beta)+\frac{f^{(n)}(x)}{n!}(\beta-\alpha)^{n}
$$

For $n=1$, this is just the mean value theorem. In general, the theorem shows that $f$ can be approximated by a polynomial of degree $n-1$, and that (5.24) allows us the estimate the error, if we know the bounds on $\left|f^{(n)}(x)\right|$.

Proof. Let $M$ be the number defined by

$$
f(\beta)=P(\beta)+M(\beta-\alpha)^{n}
$$

and put

$$
g(t)=f(t)-P(t)-M(t-\alpha)^{n} \quad(a \leq t \leq b)
$$

We have to show that $n!M=f^{(n)}(x)$ for some $x$ between $\alpha$ and $\beta$. By (5.23) and (5.26),

$$
g^{(n)}(t)=f^{(n)}(t)-n!M \quad(a<t<b)
$$

Hence the proof will be complete if we can show that $g^{(n)}(x)=0$ for some $x$ between $\alpha$ and $\beta$.

Since $P^{(k)}(\alpha)=f^{(k)}(\alpha)$ for $k=0, \ldots, n-1$, we have

$$
g(\alpha)=g^{\prime}(\alpha)=\cdots=g^{(n-1)}(\alpha)=0
$$

Our choice of $M$ shows that $g(\beta)=0$, so that $g^{\prime}\left(x_{1}\right)=0$ for some $x_{1}$ between $\alpha$ and $\beta$, by the mean value theorem. Since $g^{\prime}(\alpha)=0$, we conclude similarly that $g^{\prime \prime}\left(x_{2}\right)=0$ for some $x_{2}$ between $\alpha$ and $x_{1}$. After $n$ steps we arrive at the conclusion that $g^{(n)}\left(x_{n}\right)=0$ for some $x_{n}$ between $\alpha$ and $x_{n-1}$, that is, between $\alpha$ and $\beta$.

# DIFFERENTIATION OF VECTOR-VALUED FUNCTIONS 

5.16 Remarks. Definition 5.1 applies without any change to complex functions $f$ defined on $[a, b]$, and Theorems 5.2 and 5.3, as well as their proofs, remain valid. If $f_{1}$ and $f_{2}$ are the real and imaginary parts of $f$, that is, if

$$
f(t)=f_{1}(t)+i f_{2}(t)
$$

for $a \leq t \leq b$, where $f_{1}(t)$ and $f_{2}(t)$ are real, then we clearly have

$$
f^{\prime}(x)=f_{1}^{\prime}(x)+i f_{2}^{\prime}(x)
$$

also, $f$ is differentiable at $x$ if and only if both $f_{1}$ and $f_{2}$ are differentiable at $x$.
Passing to vector-valued functions in general, i.e., to functions $\mathbf{f}$ which map $[a, b]$ into some $\mathbb{R}^{k}$, we may still apply Definition 5.1 to define $\mathbf{f}^{\prime}(x)$. The term $\phi(t)$ in (5.1) is now, for each $t$, a point in $\mathbb{R}^{k}$, and the limit in (5.2) is taken with respect to the norm of $\mathbb{R}^{k}$. In other words, $\mathbf{f}^{\prime}(x)$ is that point of $\mathbb{R}^{k}$ (if there is one) for which

$$
\lim _{t \rightarrow x}\left|\frac{\mathbf{f}(t)-\mathbf{f}(x)}{t-x}-\mathbf{f}^{\prime}(x)\right|=0
$$

and $\mathbf{f}^{\prime}$ is again a function with values in $\mathbb{R}^{k}$.
If $f_{1}, \ldots, f_{k}$ are the components of $f$, as defined in Theorem 4.10, then

$$
\mathbf{f}^{\prime}=\left(f_{1}^{\prime}, \ldots, f_{k}^{\prime}\right)
$$

and $\mathbf{f}$ is differentiable at a point $x$ if and only if each of the functions $f_{1}, \ldots, f_{k}$ is differentiable at $x$.

Theorem 5.2 is true in this context as well, and so is Theorem 5.3(a) and (b), if fg is replaced by the inner product $\mathbf{f} \cdot \mathbf{g}$ (see Definition 4.3).

When we turn to the mean value theorem, however, and to one of its consequences, namely L'Hôspital's rule, the situation changes. The next two examples will show that each of these results fails to be true for complex-valued functions.
5.17 Example. Define, for real $x$,

$$
f(x)=e^{i x}=\cos x+i \sin x
$$

(The last expression may be taken as the definition of the complex exponential $e^{i x}$; see Chap. 8 for a full discussion of these functions.) Then

$$
f(2 \pi)-f(0)=1-1=0
$$

but

$$
f^{\prime}(x)=i e^{i x}
$$

so that $\left|f^{\prime}(x)\right|=1$ for all real $x$. Thus Theorem 5.10 fails to hold in this case.
5.18 Example. On the segment $(0,1)$, define $f(x)=x$ and

$$
g(x)=x+x^{2} e^{i / x^{2}}
$$

Since $\left|e^{i t}\right|=1$ for all real $t$, we see that

$$
\lim _{x \rightarrow 0} \frac{f(x)}{g(x)}=1
$$

Next,

$$
g^{\prime}(x)=1+\left\{2 x-\frac{2 i}{x}\right\} e^{i / x^{2}} \quad(0<x<1)
$$

so that

$$
\left|g^{\prime}(x)\right| \geq\left|2 x-\frac{2 i}{x}\right|-1 \geq \frac{2}{x}-1
$$

Hence

$$
\left|\frac{f^{\prime}(x)}{g^{\prime}(x)}\right|=\frac{1}{\left|g^{\prime}(x)\right|} \leq \frac{x}{2-x}
$$

and so

$$
\lim _{x \rightarrow 0} \frac{f^{\prime}(x)}{g^{\prime}(x)}=0
$$

By (5.36) and (5.40), L'Hôspital's rule fails in this case. Note also that $g^{\prime}(x) \neq 0$ on $(0,1)$, by (5.38).

However, there is a consequence of the mean value theorem which, for purposes of applications, is almost as useful as Theorem 5.10, and which remains true for vector valued functions: From Theorem 5.10 it follows that

$$
|f(b)-f(a)| \leq(b-a) \sup _{a<x<b}\left|f^{\prime}(x)\right|
$$

5.19 Theorem. Suppose $\mathbf{f}$ is a continuous mapping of $[a, b]$ into $\mathbb{R}^{\mathrm{k}}$ and $\mathbf{f}$ is differentiable

on (a,b). Then there exists $\mathrm{x} \in(\mathrm{a}, \mathrm{b})$ such that

$$
|\mathbf{f}(\mathrm{b})-\mathbf{f}(\mathrm{a})| \leq(\mathrm{b}-\mathrm{a})\left|\mathbf{f}^{\prime}(\mathrm{x})\right|
$$

Proof(V.P. Havin). Put $\mathbf{z}=\mathbf{f}(\mathrm{b})-\mathbf{f}(\mathrm{a})$ and define

$$
\varphi(\mathrm{t})=\mathbf{z} \cdot \mathbf{f}(\mathrm{t}) \quad(\mathrm{a} \leq \mathrm{t} \leq \mathrm{b})
$$

Then $\varphi$ is a real-valued continuous function on $[a, b]$ which is differentiable on $(a, b)$. The mean value theorem shows therefore that

$$
\varphi(b)-\varphi(a)=(b-a) \varphi^{\prime}(x)=(b-a) \mathbf{z} \cdot \mathbf{f}^{\prime}(x)
$$

for some $x \in(a, b)$. On the other hand,

$$
\varphi(b)-\varphi(a)=\mathbf{z} \cdot \mathbf{f}(b)-\mathbf{z} \cdot \mathbf{f}(a)=\mathbf{z} \cdot \mathbf{z}=|\mathbf{z}|^{2}
$$

The Schwarz inequality now gives

$$
|\mathbf{z}|^{2}=(\mathrm{b}-\mathrm{a})\left|\mathbf{z} \cdot \mathbf{f}^{\prime}(\mathrm{x})\right| \leq(\mathrm{b}-\mathrm{a})|\mathbf{z}|\left|\mathbf{f}^{\prime}(\mathrm{x})\right|
$$

Hence $|\mathbf{z}| \leq(\mathrm{b}-\mathrm{a})\left|\mathbf{f}^{\prime}(\mathrm{x})\right|$, which is the desired conclusion.

# EXERCISES 

5.1. Let $f$ be defined for all real $x$, and suppose that

$$
|f(x)-f(y)| \leq(x-y)^{2}
$$

For all real $x$ and $y$. Prove that $x$ is constant.
5.2. Suppose $f^{\prime}(x)>0$ in $(a, b)$. Prove that $f$ is strictly increasing on $(a, b)$, and let $g$ be its inverse function. Prove that $g$ is differentiable and that

$$
g^{\prime}(f(x))=\frac{1}{f^{\prime}(x)} \quad(a<x<b)
$$

5.3. Suppose $g$ is a real function on $\mathbb{R}^{1}$ with bounded derivative (say $\left|g^{\prime}\right| \leq M$ ). Fix $\varepsilon>0$ and define $f(x)=x+\varepsilon g(x)$. Prove that $f$ is one-to-one if $\varepsilon$ is small enough (A set of admissible values of $\varepsilon$ can be determined which depends only on $M$.)
5.4. If

$$
C_{0}+\frac{C_{1}}{2}+\cdots+\frac{C_{n-1}}{n}+\frac{C_{n}}{n+1}=0
$$

where $C_{0}, \ldots, C_{n}$ are real constants, prove that the equation

$$
C_{0}+C_{1} x+\cdots+C_{n-1} x^{n-1}+C_{n} x^{n}=0
$$

has at least one real root between 0 and 1 .
5.5. Suppose $f$ is defined and differentiable for every $x>0$ and $f^{\prime}(x) \rightarrow 0$ as $x \rightarrow+\infty$. Put $g(x)=f(x+1)-f(x)$. Prove that $g(x) \rightarrow 0$ as $x \rightarrow+\infty$.

# 5.6. Suppose 

(a) $f$ is continuous for $x \geq 0$,
(b) $f^{\prime}(x)$ exists for $x>0$,
(c) $f(0)=0$,
(d) $f^{\prime}$ is monotonically increasing.

Put

$$
g(x)=\frac{f(x)}{x} \quad(x>0)
$$

and prove that $g$ is monotonically increasing.
5.7. Suppose $f^{\prime}(x), g^{\prime}(x)$ exist, $g^{\prime}(x) \neq 0$, and $f(x)=g(x)=0$. Prove that

$$
\lim _{t \rightarrow x} \frac{f(t)}{g(t)}=\frac{f^{\prime}(x)}{g^{\prime}(x)}
$$

(This also holds for complex functions.)
5.8. Suppose $f^{\prime}$ is continuous on $[a, b]$ and $\varepsilon>0$. Prove that there exists $\delta>0$ such that

$$
\left|\frac{f(t)-f(x)}{t-x}-f^{\prime}(x)\right|<\varepsilon
$$

whenever $0<|t-x|<\delta, a \leq x \leq b, a \leq t \leq b$. (This could be expressed by saying that $f$ is uniformly differentiable on $[a, b]$ if $f^{\prime}$ is continuous on $[a, b]$.) Does this hold for vector-valued functions too?
5.9. Let $f$ be a continuous real function on $\mathbb{R}^{1}$, of which it is known that $f^{\prime}(x)$ exists for all $x \neq 0$ and that $f^{\prime}(x) \rightarrow 3$ as $x \rightarrow 0$. Does it follow that $f^{\prime}(0)$ exists?
5.10. Suppose $f$ and $g$ are complex differentiable functions on $(0,1), f(x) \rightarrow 0, g(x) \rightarrow 0$, $f^{\prime}(x) \rightarrow A, g^{\prime}(x) \rightarrow B$ as $x \rightarrow 0$, where $A$ and $B$ are complex numbers and $B \neq 0$. Prove that

$$
\lim _{x \rightarrow 0} \frac{f(x)}{g(x)}=\frac{A}{B}
$$

Compare with Example 5.18. Hint:

$$
\frac{f(x)}{g(x)}=\left\{\frac{f(x)}{x}-A\right\} \cdot \frac{x}{g(x)}+A \cdot \frac{x}{g(x)}
$$

Apply Theorem 5.13 to the real and imaginary parts of $f(x) / x$ and $g(x) / x$.
5.11. Suppose $f$ is defined in a neighborhood of $x$, and suppose $f^{\prime \prime}(x)$ exists. Show that

$$
\lim _{h \rightarrow 0} \frac{f(x+h)+f(x-h)-2 f(x)}{h^{2}}=f^{\prime \prime}(x)
$$

Show by example that the limit may exist even if $f^{\prime \prime}(x)$ does not. Hint: Use Theorem 5.13.
5.12. If $f(x)=|x|^{3}$, compute $f^{\prime}(x), f^{\prime \prime}(x)$ for all real $x$, and show that $f^{(3)}(0)$ does not exist.
5.13. Suppose $a$ and $c$ are real numbers, $c>0$, and $f$ is defined on $[-1,1]$ by

$$
f(x)= \begin{cases}x^{a} \sin \left(|x|^{-c}\right) & (\text { if } x \neq 0) \\ 0 & (\text { if } x=0)\end{cases}
$$

Prove the following statements
(a) $f$ is continuous if and only if $a>0$.
(b) $f^{\prime}(0)$ exists if and only if $a>1$.
(c) $f^{\prime}$ is bounded if and only if $a \geq 1+c$.
(d) $f^{\prime}$ is continuous if and only if $a>1+c$.

(e) $f^{\prime \prime}(0)$ exists if and only if $a>2+c$.
(f) $f^{\prime \prime}$ is bounded if and only if $a \geq 2+2 c$.
(g) $f^{\prime \prime}$ is continuous if and only if $a>2+2 c$.
5.14. Let $f$ be a differentiable real function defined on $(a, b)$. Prove that $f$ is convex if and only if $f^{\prime}$ is monotonically increasing. Assume next that $f^{\prime \prime}(x)$ exists for every $x \in(a, b)$, and prove that $f$ is convex if and only if $f^{\prime \prime}(x) \geq 0$ for all $x \in(a, b)$.
5.15. Suppose $a \in \mathbb{R}^{1}, f$ is a twice-differentiable real function on $(a, \infty)$, and $M_{0}, M_{1}, M_{2}$ are the least upper bounds of $|f(x)|,\left|f^{\prime}(x)\right|,\left|f^{\prime \prime}(x)\right|$, respectively, on $(a, \infty)$. Prove that

$$
M_{1}^{2} \leq 4 M_{0} M_{2}
$$

Hint: If $\mathrm{h}>0$, Taylor's theorem shows that

$$
f^{\prime}(x)=\frac{1}{2 h}|f(x+2 h)-f(x)|-h f^{\prime \prime}(\xi)
$$

for some $\xi \in(x, x+2 h)$. Hence

$$
\left|f^{\prime}(x)\right| \leq h M_{2}+\frac{M_{0}}{h}
$$

To show that $M_{1}^{2}=4 M_{0} M_{2}$ can actually happen, take $a=-1$, define

$$
f(x)= \begin{cases}2 x^{2}-1 & (-1<x<0) \\ \frac{x^{2}-1}{x^{2}+1} & (0 \leq x<\infty)\end{cases}
$$

and show that $M_{0}=1, M_{1}=4$, and $M_{2}=4$.
Does $M_{1}^{2} \leq 4 M_{0} M_{2}$ hold for vector-valued functions too?
5.16. Suppose $f$ is twice-differentiable on $(0, \infty), f^{\prime \prime}$ is bounded on $(0, \infty)$, and $f(x) \rightarrow 0$ as $x \rightarrow \infty$. Prove that $f^{\prime}(x) \rightarrow 0$ as $x \rightarrow \infty$. Hint: Let $a \rightarrow \infty$ in Exercise 5.15
5.17. Suppose $f$ is a real, three times differentiable function on $[-1,1]$, such that

$$
f(-1)=0, \quad f(0)=0, \quad f(1)=1, \quad f^{\prime}(0)=0
$$

Prove that $f^{(3)}(x) \geq 3$ for some $x \in(-1,1)$. Note that equality holds for $\left(x^{3}+x^{2}\right) / 2$.
Hint: Use Theorem 5.15, with $\alpha=0$ and $\beta= \pm 1$, to show that there exist $s \in(0,1)$ and $t \in(-1,0)$ such that

$$
f^{(3)}(s)+f^{(3)}(t)=6
$$

5.18. Suppose $f$ is a real function on $[a, b], n$ is a positive integer, and $f^{(n-1)}$ exists for every $t \in[a, b]$. Let $\alpha, \beta$, and $P$ be as in Taylor's theorem (Theorem 5.15). Define

$$
Q(t)=\frac{f(t)-f(\beta)}{t-\beta}
$$

for $t \in[a, b], t \neq \beta$, differentiate

$$
f(t)-f(\beta)=(t-\beta) Q(t)
$$

$n-1$ times at $t=\alpha$, and derive the following version of Taylor's theorem:

$$
f(\beta)=P(\beta)+\frac{Q^{(n-1)}(\alpha)}{(n-1)!}(\beta-\alpha)^{n}
$$

5.19. Suppose $f$ is defined in $(-1,1)$ and $f^{\prime}(0)$ exists. Suppose $-1<\alpha_{n}<\beta_{n}<1, \alpha_{n} \rightarrow 0$, and $\beta_{n} \rightarrow 0$ as $n \rightarrow \infty$. Define the difference quotients

$$
D_{n}=\frac{f\left(\beta_{n}\right)-f\left(\alpha_{n}\right)}{\beta_{n}-\alpha_{n}}
$$

Prove the following statements:
(a) If $\alpha_{n}<0<\beta_{n}$, then $\lim D_{n}=f^{\prime}(0)$.
(b) If $0<\alpha_{n}<\beta_{n}$ and $\left(\beta_{n} /\left(\beta_{n}-\alpha_{n}\right)\right)_{n=1}^{\infty}$ is bounded, then $\lim D_{n}=f^{\prime}(0)$.
(c) If $f^{\prime}$ is continuous in $(-1,1)$, then $\lim D_{n}=f^{\prime}(0)$.

Give an example in which $f$ is differentiable in $(-1,1)$ (but $f^{\prime}$ is not continuous at 0 ) and in which $\alpha_{n}, \beta_{n}$ tend to 0 in such a way that $\lim D_{n}$ exists but is different from $f^{\prime}(0)$.
5.20. Formulate and prove an inequality which follows from Taylor's theorem and which remains valid for vector-valued functions.
5.21. Let $E$ be a closed subset of $\mathbb{R}^{1}$. We saw in Exercise 4.22 that there is a real continuous function $f$ on $\mathbb{R}^{1}$ whose zero set is $E$. Is it possible, for each closed set $E$, to find such an $f$ which is differentiable on $\mathbb{R}^{1}$, or one which is $n$ times differentiable, or even one which has derivatives of all orders on $\mathbb{R}^{1}$ ?
5.22. Suppose $f$ is a real function on $(-\infty, \infty)$. Call $x$ a fixed point of $f$ if $f(x)=x$.
(a) If $f$ is differentiable and $f^{\prime}(t) \neq 1$ for every real $t$, prove that $f$ has at most one fixed point.
(b) Show that the function $f$ defined by

$$
f^{\prime}(t)=t+\left(1+e^{t}\right)^{-1}
$$

has no fixed point, although $0<f^{\prime}(t)<1$ for all real $t$.
(c) However, if there is a constant $A<1$ such that $\left|f^{\prime}(t)\right| \leq A$ for all real $t$, prove that a fixed point of $f$ exists, and that $x=\lim x_{n}$, where $x_{1}$ is an arbitrary real number and

$$
x_{n+1}=f\left(x_{n}\right)
$$

for $n=1,2,3, \ldots$
(d) Show that the process described in (c) can be visualized by the zig-zag path

$$
\left(x_{1}, x_{2}\right) \rightarrow\left(x_{2}, x_{2}\right) \rightarrow\left(x_{2}, x_{3}\right) \rightarrow\left(x_{3}, x_{3}\right) \rightarrow\left(x_{3}, x_{4}\right) \rightarrow \cdots
$$

5.23. The function $f$ defined by

$$
f(x)=\frac{x^{3}+1}{3}
$$

has three fixed points, say $\alpha, \beta, \gamma$, where

$$
-2<\alpha<-1, \quad 0<\beta<1, \quad 1<\gamma<2
$$

For arbitrarily chosen $x_{1}$, define $\left(x_{n}\right)$ by setting $x_{n+1}=f\left(x_{n}\right)$.
(a) If $x_{1}<\alpha$ prove that $x_{n} \rightarrow-\infty$ as $n \rightarrow \infty$.
(b) If $\alpha<x_{1}<\gamma$, prove that $x_{n} \rightarrow \beta$ as $n \rightarrow \infty$.
(c) If $\gamma<x_{1}$, prove that $x_{n} \rightarrow+\infty$ as $n \rightarrow \infty$.

Thus $\beta$ can be located by this method, but $\alpha$ and $\gamma$ cannot.
5.24. The process described in part (c) of Exercise 5.22 can of course also be applied to functions that map $(0, \infty)$ to $(0, \infty)$.

Fix some $\alpha>1$ and put

$$
f(x)=\frac{1}{2}\left(x+\frac{\alpha}{x}\right), \quad g(x)=\frac{\alpha+x}{1+x}
$$

Both $f$ and $g$ have $\sqrt{\alpha}$ as their only fixed point in $(0, \infty)$. Try to explain, on the basis of properties of $f$ and $g$, why the convergence in Exercise 3.16 is so much more rapid than it is in Exercise 3.17. (Compare $f^{\prime}$ and $g^{\prime}$, draw the zig-zags suggested in Exercise 5.22.) Do the same when $0<\alpha<1$.
5.25. Suppose $f$ is twice-differentiable on $[a, b], f(a)<0, f(b)>0, f^{\prime}(x) \geq \delta>0$, and $0 \leq f^{\prime \prime}(x) \leq M$ for all $x \in[a, b]$. Let $\ell$ be the unique point in $(a, b)$ at which $f(\ell)=0$.

Complete the details of the following outline of Newton's method for computing $\ell$.
(a) Choose $x_{1} \in(\ell, b)$ and define $\left(x_{n}\right)$ by

$$
x_{n+1}=x_{n}-\frac{f\left(x_{n}\right)}{f^{\prime}\left(x_{n}\right)}
$$

Interpret this geometrically, in terms of a tangent to the graph of $f$.
(b) Prove that $x_{n+1}<x_{n}$, and that

$$
\lim _{n \rightarrow \infty} x_{n}=\ell
$$

(c) Use Taylor's theorem to show that

$$
x_{n+1}-\ell=\frac{f^{\prime \prime}\left(t_{n}\right)}{2 f^{\prime}\left(x_{n}\right)}\left(x_{n}-\ell\right)^{2}
$$

for some $t_{n} \in\left(\ell, x_{n}\right)$.
(d) If $A=M / 2 \delta$, deduce that

$$
0 \leq x_{n+1}-\ell \leq \frac{1}{A}\left|A\left(x_{1}-\ell\right)\right|^{2^{n}}
$$

Compare with Exercises 3.16 and 3.18.
(e) Show that Newton's method amounts to finding a fixed point of the function $g$ defined by

$$
g(x)=x-\frac{f(x)}{f^{\prime}(x)}
$$

How does $g^{\prime}(x)$ behave for $x$ near $\ell$ ?
(f) Put $f(x)=x^{1 / 3}$ on $(-\infty, \infty)$ and try Newton's method. What happens?
5.26. Suppose $f$ is differentiable on $[a, b], f(a)=0$, and there is a real number $A$ such that $\left|f^{\prime}(x)\right| \leq A|f(x)|$ on $[a, b]$. Prove that $f(x)=0$ for all $x \in(a, b]$. Hint: Fix $x_{0} \in(a, b]$, let

$$
M_{0}=\sup |f(x)|, \quad M_{1}=\sup \left|f^{\prime}(x)\right|
$$

for $a \leq x \leq x_{0}$. For any such $x$,

$$
|f(x)| \leq M_{1}\left(x_{0}-a\right) \leq A\left(x_{0}-a\right) M_{0}
$$

Hence $M_{0}=0$ if $A\left(x_{0}-a\right)<1$. That is, $f=0$ on $\left(a, x_{0}\right]$. Proceed.
5.27. Let $\phi$ be a real function defined on a rectangle $R$ in the plane given by $a \leq x \leq b$, $\alpha \leq y \leq \beta$. A solution of the initial-value problem

$$
y^{\prime}=\phi(x, y), \quad y(a)=c \quad(\alpha \leq c \leq \beta)
$$

is, by definition, a differentiable function $f$ on $[a, b]$ such that $f(a)=c, \alpha \leq f(x) \leq \beta$, and

$$
f^{\prime}(x)=\phi(x, f(x)) \quad(a \leq x \leq b)
$$

Prove that such a problem has at most one solution if there is a constant $A$ such that

$$
\left|\phi\left(x, y_{2}\right)-\phi\left(x, y_{1}\right)\right| \leq A\left|y_{2}-y_{1}\right|
$$

whenever $\left(x, y_{1}\right) \in R$ and $\left(x, y_{2}\right) \in R$.

Hint: Apply Exercise 5.26 to the difference of two solutions. Note that this uniqueness theorem does not hold for the initial-value problem

$$
y^{\prime}=y^{1 / 2}, \quad y(0)=0
$$

which has two solutions: $f(x)=0$ and $f(x)=x^{2} / 4$. Find all other solutions.
5.28. Formulate and prove an analogous uniqueness theorem for systems of differentiable equations of the form

$$
y_{j}^{\prime}=\phi_{j}\left(x, y_{1}, \ldots, y_{k}\right), \quad y_{j}(a)=c_{j} \quad(j=1, \ldots, k)
$$

Note that this can be rewritten in the form

$$
\mathbf{y}^{\prime}=\boldsymbol{\phi}(\mathrm{x}, \mathbf{y}), \quad \mathbf{y}(\mathfrak{a})=\mathbf{c}
$$

where $\mathbf{y}=\left(y_{1}, \ldots, y_{k}\right)$ ranges over a $k$-cell, $\boldsymbol{\phi}$ is the mapping of a $(k+1)$-cell into the euclidean k -space whose components are the functions $\phi_{1}, \ldots, \phi_{k}$, and $\mathbf{c}$ is the vector $\left(c_{1}, \ldots, c_{k}\right)$. Use Exercise 5.26, for vector-valued functions.
5.29. Specialize Exercise 5.28 by considering the system

$$
\begin{aligned}
y_{j}^{\prime} & =y_{j+1} \quad(j=1, \ldots, k-1) \\
y_{k}^{\prime} & =f(x)-\sum_{j=1}^{k} g_{j}(x) y_{j}
\end{aligned}
$$

where $f, g_{1}, \ldots, g_{k}$ are continuous real functions on $[a, b]$, and derive a uniqueness theorem for solutions of the equation

$$
y^{(k)}+g_{k}(x) y^{(k-1)}+\cdots+g_{2}(x) y^{\prime}+g_{1}(x) y=f(x)
$$

subject to initial conditions

$$
y(a)=c_{1}, \quad y^{\prime}(a)=c_{2}, \quad \ldots, \quad y^{(k-1)}(a)=c_{k}
$$

# Chapter 6 

## THE RIEMANN-STIELTJES INTEGRAL

The present chapter is based on a definition of the Riemann integral which depends very explicitly on the order structure of the real line. Accordingly, we begin by discussing integration of real-valued functions on intervals. Extensions to complex and vector-valued functions on intervals follow in later sections. Integration over sets other than intervals is discussed in Chaps. 10 and 11.

## DEFINITION AND EXISTENCE OF THE INTEGRAL

6.1 Definition. Let $[a, b]$ be a given interval. By a partition $P$ of $[a, b]$, we mean a finite set of points $x_{0}, x_{1}, \ldots, x_{n}$, where

$$
a=x_{0} \leq x_{1} \leq \cdots \leq x_{n-1} \leq x_{n}=b
$$

We write

$$
\Delta x_{i}=x_{i}-x_{i-1} \quad(i=1, \ldots, n)
$$

Now suppose $f$ is a bounded real function defined on $[a, b]$. Corresponding to each partition $P$ of $[a, b]$ we put

$$
\begin{aligned}
M_{i} & =\sup f(x) & & \left(x_{i-1} \leq x \leq x_{i}\right) \\
m_{i} & =\inf f(x) & & \left(x_{i-1} \leq x \leq x_{i}\right) \\
U(P, f) & =\sum_{i=1}^{n} M_{i} \Delta x_{i} & \\
L(P, f) & =\sum_{i=1}^{n} m_{i} \Delta x_{i} & &
\end{aligned}
$$

and finally

$$
\begin{aligned}
& \int_{a}^{b} f d x=\inf U(P, f) \\
& \int_{a}^{b} f d x=\sup L(P, f)
\end{aligned}
$$

where the inf and sup are taken over all partitions $P$ of $[a, b]$. The left members of (6.1) and (6.2) are called the upper and lower Riemann integrals of f over $[a, b]$, respectively.

If the upper and lower integrals are equal, we say that $f$ is Riemann integrable on $[a, b]$, we write $f \in \mathscr{R}$ (that is, $\mathscr{R}$ denotes the set of Riemann-integrable functions), and we denote the common value of (6.1) and (6.2) by

$$
\int_{a}^{b} f d x
$$

or by

$$
\int_{a}^{b} f(x) d x
$$

This is the Riemann integral of f over $[a, b]$.
Since $f$ is bounded, there exist two numbers, $m$ and $M$, such that

$$
m \leq f(x) \leq M \quad(a \leq x \leq b)
$$

Hence, for every $P$,

$$
m(b-a) \leq L(P, f) \leq U(P, f) \leq M(b-a)
$$

so that the numbers $L(P, f)$ and $U(P, f)$ form a bounded set. This shows that the upper and lower integrals are defined for every bounded function $f$. The question of their equality, and hence the question of the integrability of $f$, is a more delicate one. Instead of investigating it separately for the Riemann integral, we shall immediately consider a more general situation.
6.2 Definition. Let $\alpha$ be a monotonically increasing function on $[a, b]$ (since $\alpha(a)$ and $\alpha(b)$ are finite, it follows that $\alpha$ is bounded on $[a, b]$ ). Corresponding to each partition $P$ of $[a, b]$, we write

$$
\Delta \alpha_{i}=\alpha\left(x_{i}\right)-\alpha\left(x_{i-1}\right)
$$

It is clear that $\Delta \alpha_{i} \geq 0$. For any real function $f$ which is bounded on $[a, b]$ we put

$$
\begin{aligned}
& \mathrm{U}(\mathrm{P}, \mathrm{f}, \alpha)=\sum_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{M}_{\mathrm{i}} \Delta \alpha_{\mathrm{i}} \\
& \mathrm{~L}(\mathrm{P}, \mathrm{f}, \alpha)=\sum_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{~m}_{\mathrm{i}} \Delta \alpha_{\mathrm{i}}
\end{aligned}
$$

where $M_{i}, m_{i}$ have the same meaning as in Definition 6.1, and we define

$$
\begin{aligned}
& \int_{a}^{b} f d \alpha=\inf U(P, f, \alpha) \\
& \int_{a}^{b} f d \alpha=\sup L(P, f, \alpha)
\end{aligned}
$$

the inf and sup again being taken over all partitions.
If the left members of (6.5) and (6.6) are equal, we denote their common value by

$$
\int_{a}^{b} f d \alpha
$$

or sometimes by

$$
\int_{a}^{b} f(x) d \alpha(x)
$$

This is the Riemann-Stieltjes integral (or simply the Stieltjes integral) of $f$ with respect to $\alpha$, over $[a, b]$. If (6.7) exists, i.e., if (6.5) and (6.6) are equal, we say that $f$ is integrable with respect to $\alpha$, in the Riemann sense, and write $f \in \mathscr{R}(\alpha)$.

By taking $\alpha(x)=x$, the Riemann integral is seen to be a special case of the Riemann-Stieltjes integral. Let us mention explicitly, however, that in the general case $\alpha$ need not even be continuous.

A few words should be said about the notation. We prefer (6.7) to (6.8), since the letter x which appears in (6.8) adds nothing to the content of (6.7). It is immaterial which letter we use to represent the so-called "variable of integration." For instance, (6.8) is the same as

$$
\int_{a}^{b} f(y) d \alpha(y)
$$

The integral depends on $f, \alpha, a$, and $b$, but not on the variable of integration, which may as well be omitted.

The role played by the variable of integration is quite analogous to that of the

index of summation: The two symbols

$$
\sum_{i=1}^{n} c_{i}, \quad \sum_{k=1}^{n} c_{k}
$$

mean the same thing, since each means $c_{1}+c_{2}+\cdots+c_{n}$.
Of course, no harm is done by inserting the variable of integration, and in many cases it is actually convenient to do so.

We shall now investigate the existence of the integral (6.7). Without saying so every time, $f$ will be assumed real and bounded, and $\alpha$ is monotonically increasing on $[a, b]$; and, when there can be no misunderstanding, we shall write $\int$ in place of $\int_{a}^{b}$.
6.3 Definition. We say that the partition $\mathrm{P}^{*}$ is a refinement of P if $\mathrm{P}^{*} \supset \mathrm{P}$ (that is, if every point of P is a point of $\mathrm{P}^{*}$ ). Given two partitions, $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$, we say that $\mathrm{P}^{*}$ is their common refinement if $\mathrm{P}^{*}=\mathrm{P}_{1} \cup \mathrm{P}_{2}$.
6.4 Theorem. If $\mathrm{P}^{*}$ is a refinement of P , then

$$
L(P, f, \alpha) \leq L\left(P^{*}, f, \alpha\right)
$$

and

$$
U\left(P^{*}, f, \alpha\right) \leq U(P, f, \alpha)
$$

Proof. To prove (6.9), suppose first that $\mathrm{P}^{*}$ contains just one point more than P . Let this extra point be $x^{*}$, and suppose $x_{i-1}<x^{*}<x_{i}$, where $x_{i-1}$ and $x_{i}$ are two consecutive points of P. Put

$$
\begin{array}{ll}
w_{1}=\inf f(x) & \left(x_{i-1} \leq x \leq x^{*}\right) \\
w_{2}=\inf f(x) & \left(x^{*} \leq x \leq x_{i}\right)
\end{array}
$$

Clearly $w_{1} \geq m_{i}$ and $w_{2} \geq m_{i}$, where, as before,

$$
m_{i}=\inf f(x) \quad\left(x_{i-1} \leq x \leq x_{i}\right)
$$

Hence

$$
\begin{aligned}
L\left(P^{*}, f, \alpha\right) & -L(P, f, \alpha) \\
& =w_{1}\left[\alpha\left(x^{*}\right)-\alpha\left(x_{i-1}\right)\right]+w_{2}\left[\alpha\left(x_{i}\right)-\alpha\left(x^{*}\right)\right]-m_{i}\left[\alpha\left(x_{i}\right)-\alpha\left(x_{i-1}\right)\right] \\
& =\left(w_{1}-m_{i}\right)\left[\alpha\left(x^{*}\right)-\alpha\left(x_{i-1}\right)\right]+\left(w_{2}-m_{i}\right)\left[\alpha\left(x_{i}\right)-\alpha\left(x^{*}\right)\right] \geq 0
\end{aligned}
$$

If $\mathrm{P}^{*}$ contains k points more than P , we repeat this reasoning k times, and arrive at (6.9). The proof of (6.10) is analogous.

6.5 Theorem. $\int_{a}^{b} f d \alpha \leq \int_{a}^{b} f d \alpha$.

Proof. Let $\mathrm{P}^{*}$ be the common refinement of two partitions $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$. By Theorem 6.4,

$$
\mathrm{L}\left(\mathrm{P}_{1}, \mathrm{f}, \alpha\right) \leq \mathrm{L}\left(\mathrm{P}^{*}, \mathrm{f}, \alpha\right) \leq \mathrm{U}\left(\mathrm{P}^{*}, \mathrm{f}, \alpha\right) \leq \mathrm{U}\left(\mathrm{P}_{2}, \mathrm{f}, \alpha\right)
$$

Hence

$$
\mathrm{L}\left(\mathrm{P}_{1}, \mathrm{f}, \alpha\right) \leq \mathrm{U}\left(\mathrm{P}_{2}, \mathrm{f}, \alpha\right)
$$

If $\mathrm{P}_{2}$ is fixed and the sup is taken over all $\mathrm{P}_{1}$, (6.11) gives

$$
\int f d \alpha \leq U\left(P_{2}, f, \alpha\right)
$$

The theorem follows by taking the inf over all $\mathrm{P}_{2}$ in (6.12).
6.6 Theorem. $f \in \mathscr{R}(\alpha)$ on $[a, b]$ if and only if for every $\varepsilon>0$, there exists a partition $P$ such that

$$
\mathrm{U}(\mathrm{P}, \mathrm{f}, \alpha)-\mathrm{L}(\mathrm{P}, \mathrm{f}, \alpha)<\varepsilon
$$

Proof. For every P , we have

$$
\mathrm{L}(\mathrm{P}, \mathrm{f}, \alpha) \leq \int \mathrm{f} d \alpha \leq \int \mathrm{f} d \alpha \leq \mathrm{U}(\mathrm{P}, \mathrm{f}, \alpha)
$$

Thus (6.13) implies

$$
0 \leq \int \mathrm{f} d \alpha-\int \mathrm{f} d \alpha<\varepsilon
$$

Hence, if (6.13) can be satisfied for every $\varepsilon>0$, we have

$$
\int f d \alpha=\int f d \alpha
$$

that is, $f \in \mathscr{R}(\alpha)$.
Conversely, suppose $f \in \mathscr{R}(\alpha)$, and let $\varepsilon>0$ be given. Then there exist partitions $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ such that

$$
\begin{aligned}
& \mathrm{U}\left(\mathrm{P}_{2}, \mathrm{f}, \alpha\right)-\int \mathrm{f} d \alpha<\frac{\varepsilon}{2} \\
& \int \mathrm{f} d \alpha-\mathrm{L}\left(\mathrm{P}_{1}, \mathrm{f}, \alpha\right)<\frac{\varepsilon}{2}
\end{aligned}
$$

We choose P to be the common refinement of $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$. Then Theorem 6.4, to-

gether with (6.14) and (6.15), shows that

$$
\mathrm{U}(\mathrm{P}, \mathrm{f}, \alpha) \leq \mathrm{U}\left(\mathrm{P}_{2}, \mathrm{f}, \alpha\right)<\int \mathrm{f} \mathrm{~d} \alpha+\frac{\varepsilon}{2}<\mathrm{L}\left(\mathrm{P}_{1}, \mathrm{f}, \alpha\right)+\varepsilon \leq \mathrm{L}(\mathrm{P}, \mathrm{f}, \alpha)+\varepsilon
$$

so that (6.13) holds for this partition $P$.
Theorem 6.6 furnishes a convenient criterion for integrability. Before we apply it, we state some closely related facts.

# 6.7 Theorem. 

(a) If (6.13) holds for some P and some $\varepsilon$, then (6.13) holds (with the same $\varepsilon$ ) for every refinement of P .
(b) If (6.13) holds for $\mathrm{P}=\left\{\mathrm{x}_{0}, \ldots, \mathrm{x}_{\mathrm{n}}\right\}$ and if $\mathrm{s}_{\mathrm{i}}, \mathrm{t}_{\mathrm{i}}$ are arbitrary points in $\left[\mathrm{x}_{\mathrm{i}-1}, \mathrm{x}_{\mathrm{i}}\right]$, then

$$
\sum_{i=1}^{n}\left|f\left(s_{i}\right)-f\left(t_{i}\right)\right| \Delta \alpha_{i}<\varepsilon
$$

(c) If $\mathrm{f} \in \mathscr{R}(\alpha)$ and the hypotheses of (b) hold, then

$$
\left|\sum_{i=1}^{n} f\left(t_{i}\right) \Delta \alpha_{i}-\int_{a}^{b} f d \alpha\right|<\varepsilon
$$

Proof. Theorem 6.4 implies (a). Under the assumptions made in (b), both $f\left(s_{i}\right)$ and $f\left(t_{i}\right)$ lie in $\left[m_{i}, M_{i}\right]$ so that $\left|f\left(s_{i}\right)-f\left(t_{i}\right)\right| \leq M_{i}-m_{i}$. Thus

$$
\sum_{i=1}^{n}\left|f\left(s_{i}\right)-f\left(t_{i}\right)\right| \Delta \alpha_{i} \leq U(P, f, \alpha)-L(P, f, \alpha)
$$

which proves (b). The obvious inequalities

$$
L(P, f, \alpha) \leq \sum f\left(t_{i}\right) \Delta \alpha_{i} \leq U(P, f, \alpha)
$$

and

$$
L(P, f, \alpha) \leq \int f d \alpha \leq U(P, f, \alpha)
$$

prove $(c)$.
6.8 Theorem. If f is continuous on $[a, b]$, then $\mathrm{f} \in \mathscr{R}(\alpha)$ on $[a, b]$.

Proof. If f is continuous on $[a, b]$ (Theorem 4.19), there exists a $\delta>0$ such that

$$
|f(x)-f(t)|<\eta
$$

if $x \in[a, b], t \in[a, b]$, and $|x-t|<\delta$.

If $P$ is any partition of $[a, b]$ such that $\Delta x_{i}<\delta$ for all $i$, then (6.16) implies that

$$
M_{i}-m_{i} \leq \eta \quad(i=1, \ldots, n)
$$

and therefore

$$
\begin{aligned}
U(P, f, \alpha)-L(P, f, \alpha) & =\sum_{i=1}^{n}\left(M_{i}-m_{i}\right) \Delta \alpha_{i} \\
& \leq \eta \sum_{i=1}^{n} \Delta \alpha_{i}=\eta[\alpha(b)-\alpha(a)]<\varepsilon
\end{aligned}
$$

By Theorem 6.6, $\mathrm{f} \in \mathscr{R}(\alpha)$.
6.9 Theorem. If f is monotonic on [a, b], and if $\alpha$ is continuous on [a, b], then $\mathrm{f} \in \mathscr{R}(\alpha)$. (We still assume, of course, that $\alpha$ is monotonic.)

Proof. Let $\varepsilon>0$ be given. For any positive integer $n$, choose a partition such that

$$
\Delta \alpha_{i}=\frac{\alpha(b)-\alpha(a)}{n} \quad(i=1, \ldots, n)
$$

This is possible since $\alpha$ is continuous (Theorem 4.23).
We suppose that $f$ is monotonically increasing (the proof is analogous in the other case). Then

$$
M_{i}=f\left(x_{i}\right), \quad m_{i}=f\left(x_{i-1}\right) \quad(i=1, \ldots, n)
$$

so that

$$
\begin{aligned}
U(P, f, \alpha)-L(P, f, \alpha) & =\frac{\alpha(b)-\alpha(a)}{n} \sum_{i=1}^{n}\left[f\left(x_{i}\right)-f\left(x_{i-1}\right)\right] \\
& =\frac{\alpha(b)-\alpha(a)}{n} \cdot[f(b)-f(a)]<\varepsilon
\end{aligned}
$$

if $n$ is taken large enough. By Theorem 6.6, $f \in \mathscr{R}(\alpha)$.
6.10 Theorem. Suppose f is bounded on [a, b], f has only finitely many points of discontinuity on $[a, b]$, and $\alpha$ is continuous at every point at which $f$ is discontinuous. Then $\mathrm{f} \in \mathscr{R}(\alpha)$.

Proof. Let $\varepsilon>0$ be given. Put $M=\sup |f(x)|$, let $E$ be the set of points at which $f$ is discontinuous. Since $E$ is finite and $\alpha$ is continuous at every point of $E$, we can cover $E$ by finitely many disjoint intervals $\left[u_{j}, v_{j}\right] \subset[a, b]$ such that the sum of the corresponding differences $\alpha\left(v_{j}\right)-\alpha\left(u_{j}\right)$ is less than $\varepsilon$. Furthermore, we can place these intervals in such a way that every point of $E \cap(a, b)$ lies in the interior of some $\left[u_{j}, v_{j}\right]$.

Remove the segments $\left(u_{j}, v_{j}\right)$ from $[a, b]$. The remaining set $K$ is compact. Hence $f$ is uniformly continuous on $K$, and there exists $\delta>0$ such that $|f(s)-f(t)|<$ $\varepsilon$ if $s \in K, t \in K,|s-t|<\delta$.

Now form a partition $P=\left\{x_{0}, x_{1}, \ldots, x_{n}\right\}$ of $[a, b]$ as follows: Each $u_{j}$ occurs in P. Each $v_{j}$ occurs in P. No point of any segment $\left(u_{j}, v_{j}\right)$ occurs in P. If $x_{i-1}$ is not one of the $u_{j}$, then $\Delta x_{i}<\delta$.

Note that $M_{i}-m_{i} \leq 2 M$ for every $i$, and that $M_{i}-m_{i} \leq \varepsilon$ unless $x_{i-1}$ is one of the $u_{j}$. Hence, as in the proof of Theorem 6.8,

$$
U(P, f, \alpha)-L(P, f, \alpha) \leq[\alpha(b)-\alpha(a)] \varepsilon+2 M \varepsilon
$$

Since $\varepsilon$ is arbitrary, Theorem 6.6 shows that $f \in \mathscr{R}(\alpha)$.
Note: If $f$ and $\alpha$ have a common point of discontinuity, then $f$ need not be in $\mathscr{R}(\alpha)$. Exercise 6.3 shows this.
6.11 Theorem. Suppose $f \in \mathscr{R}(\alpha)$ on $[a, b], m \leq f \leq M, \phi$ is continuous on $[m, M]$, and $h(x)=\phi(f(x))$ on $[a, b]$. Then $h \in \mathscr{R}(\alpha)$ on $[a, b]$.

Proof. Choose $\varepsilon>0$. Since $\phi$ is uniformly continuous on $[m, M]$, there exists $\delta>0$ such that $\delta<\varepsilon$ and $|\phi(s)-\phi(t)|<\varepsilon$ if $|s-t| \leq \delta$ and $s, t \in[m, M]$.

Since $f \in \mathscr{R}(\alpha)$, there is a partition $P=\left\{x_{0}, x_{1}, \ldots, x_{n}\right\}$ of $[a, b]$ such that

$$
U(P, f, \alpha)-L(P, f, \alpha)<\delta^{2}
$$

Let $M_{i}, m_{i}$ have the same meaning as in Definition 6.1, and let $M_{i}^{*}, m_{i}^{*}$ be the analogous numbers for $h$. Divide the numbers $1, \ldots, n$ into two classes: $i \in A$ if $M_{i}-m_{i}<\delta, i \in B$ if $M_{i}-m_{i} \geq \delta$.

For $i \in A$, our choice of $\delta$ shows that $M_{i}^{*}-m_{i}^{*} \leq \varepsilon$.
For $i \in B, M_{i}^{*}-m_{i}^{*} \leq 2 K$, where $K=\sup |\phi(t)|, m \leq t \leq M$. By (6.18), we have

$$
\delta \sum_{i \in B} \Delta \alpha_{i} \leq \sum_{i \in B}\left(M_{i}-m_{i}\right) \Delta \alpha_{i}<\delta^{2}
$$

so that $\sum_{i \in B} \Delta \alpha_{i}<\delta$. It follows that

$$
\begin{aligned}
U(P, h, \alpha)-L(P, h, \alpha) & =\sum_{i \in A}\left(M_{i}^{*}-m_{i}^{*}\right) \Delta \alpha_{i}+\sum_{i \in B}\left(M_{i}^{*}-m_{i}^{*}\right) \Delta \alpha_{i} \\
& \leq \varepsilon[\alpha(b)-\alpha(a)]+2 K \delta<\varepsilon[\alpha(b)-\alpha(a)+2 K]
\end{aligned}
$$

Since $\varepsilon$ was arbitrary, Theorem 6.6 implies that $h \in \mathscr{R}(\alpha)$.
Remark: This theorem suggests the question: Just what functions are Riemannintegrable? The answer is given by Theorem 11.33(b).

# PROPERTIES OF THE INTEGRAL 

### 6.12 Theorem.

(a) If $\mathrm{f}_{1} \in \mathscr{R}(\alpha)$ and $\mathrm{f}_{2} \in \mathscr{R}(\alpha)$ on $[\mathrm{a}, \mathrm{b}]$, then

$$
\mathrm{f}_{1}+\mathrm{f}_{2} \in \mathscr{R}(\alpha)
$$

$\mathrm{cf} \in \mathscr{R}(\alpha)$ for every constant c , and

$$
\begin{aligned}
\int_{a}^{b}\left(f_{1}+f_{2}\right) d \alpha & =\int_{a}^{b} f_{1} d \alpha+\int_{a}^{b} f_{2} d \alpha \\
\int_{a}^{b} c f d \alpha & =c \int_{a}^{b} f d \alpha
\end{aligned}
$$

(b) If $\mathrm{f}_{1}(\mathrm{x}) \leq \mathrm{f}_{2}(\mathrm{x})$ on $[\mathrm{a}, \mathrm{b}]$, then

$$
\int_{a}^{b} f_{1} d \alpha \leq \int_{a}^{b} f_{2} d \alpha
$$

(c) If $\mathrm{f} \in \mathscr{R}(\alpha)$ on $[\mathrm{a}, \mathrm{b}]$ and if $\mathrm{a}<\mathrm{c}<\mathrm{b}$, then $\mathrm{f} \in \mathscr{R}(\alpha)$ on $[\mathrm{a}, \mathrm{c}]$ and on $[\mathrm{c}, \mathrm{b}]$ and

$$
\int_{a}^{c} f d \alpha+\int_{c}^{b} f d \alpha=\int_{a}^{b} f d \alpha
$$

(d) If $\mathrm{f} \in \mathscr{R}(\alpha)$ on $[\mathrm{a}, \mathrm{b}]$ and if $|\mathrm{f}(\mathrm{x})| \leq \mathrm{M}$ on $[\mathrm{a}, \mathrm{b}]$, then

$$
\left|\int_{a}^{b} f d \alpha\right| \leq M[\alpha(b)-\alpha(a)]
$$

(e) If $\mathrm{f} \in \mathscr{R}\left(\alpha_{1}\right)$ and $\mathrm{f} \in \mathscr{R}\left(\alpha_{2}\right)$, then $\mathrm{f} \in \mathscr{R}\left(\alpha_{1}+\alpha_{2}\right)$ and

$$
\int_{a}^{b} f d\left(\alpha_{1}+\alpha_{2}\right)=\int_{a}^{b} f d \alpha_{1}+\int_{a}^{b} f d \alpha_{2}
$$

if $\mathrm{f} \in \mathscr{R}(\alpha)$ and c is a positive constant, then $\mathrm{f} \in \mathscr{R}(\mathrm{c} \alpha)$ and

$$
\int_{a}^{b} f d(c \alpha)=c \int_{a}^{b} f d \alpha
$$

Proof. If $\mathrm{f}=\mathrm{f}_{1}+\mathrm{f}_{2}$ and P is any partition of $[\mathrm{a}, \mathrm{b}]$, we have

$$
\begin{aligned}
\mathrm{L}\left(\mathrm{P}, \mathrm{f}_{1}, \alpha\right)+\mathrm{L}\left(\mathrm{P}, \mathrm{f}_{2}, \alpha\right) & \leq \mathrm{L}(\mathrm{P}, \mathrm{f}, \alpha) \\
& \leq \mathrm{U}(\mathrm{P}, \mathrm{f}, \alpha) \leq \mathrm{U}\left(\mathrm{P}, \mathrm{f}_{1}, \alpha\right)+\mathrm{U}\left(\mathrm{P}, \mathrm{f}_{2}, \alpha\right)
\end{aligned}
$$

If $f_{1} \in \mathscr{R}(\alpha)$ and $f_{2} \in \mathscr{R}(\alpha)$, let $\varepsilon>0$ be given. There are partitions $P_{j}(j=1,2)$ such that

$$
\mathrm{U}\left(\mathrm{P}_{\mathrm{j}}, \mathrm{f}_{\mathrm{j}}, \alpha\right)-\mathrm{L}\left(\mathrm{P}_{\mathrm{j}}, \mathrm{f}_{\mathrm{j}}, \alpha\right)<\varepsilon
$$

These inequalities persist if $P_{1}$ and $P_{2}$ are replaced by their common refinement $P$. Then (6.20) implies

$$
U(P, f, \alpha)-L(P, f, \alpha)<2 \varepsilon
$$

which proves that $f \in \mathscr{R}(\alpha)$.
With this same $P$, we have

$$
U\left(P, f_{j}, \alpha\right)<\int f_{j} d \alpha+\varepsilon \quad(j=1,2)
$$

hence (6.20) implies

$$
\int f d \alpha \leq U(P, f, \alpha)<\int f_{1} d \alpha+\int f_{2} d \alpha+2 \varepsilon
$$

Since $\varepsilon$ was arbitrary, we conclude that

$$
\int f d \alpha \leq \int f_{1} d \alpha+\int f_{2} d \alpha
$$

If we replace $f_{1}$ and $f_{2}$ in (6.21) by $-f_{1}$ and $-f_{2}$, the inequality is reversed, and the equality is proved.

The proof of the other assertions of Theorem 6.12 are so similar that we omit the details. In part (c), the point is that (by passing to refinements) we may restrict ourselves to partitions which contain the point $c$, in approximating $\int f d \alpha$.
6.13 Theorem. If $f \in \mathscr{R}(\alpha)$ and $g \in \mathscr{R}(\alpha)$ on $[a, b]$, then
(a) $\mathrm{fg} \in \mathscr{R}(\alpha)$;
(b) $|f| \in \mathscr{R}(\alpha)$ and $\left|\int_{a}^{b} f d \alpha\right| \leq \int_{a}^{b}|f| d \alpha$.

Proof. If we take $\phi(t)=t^{2}$, Theorem 6.11 shows that $f^{2} \in \mathscr{R}(\alpha)$ if $f \in \mathscr{R}(\alpha)$. The identity

$$
4 \mathrm{fg}=(\mathrm{f}+\mathrm{g})^{2}-(\mathrm{f}-\mathrm{g})^{2}
$$

completes the proof of (a).
If we take $\phi(\mathrm{t})=|\mathrm{t}|$, Theorem 6.11 shows similarly that $|f| \in \mathscr{R}(\alpha)$. Choose $\mathrm{c}= \pm 1$, so that

$$
c \int f d \alpha \geq 0
$$

Then

$$
|\int f d \alpha|=c \int f d \alpha=\int c f d \alpha \leq \int|f| d \alpha
$$

since $c f \leq|f|$.

6.14 Definition. The unit step function I is defined by

$$
I(x)= \begin{cases}0 & (x \leq 0) \\ 1 & (x>0)\end{cases}
$$

6.15 Theorem. If $\mathrm{a}<\mathrm{s}<\mathrm{b}, \mathrm{f}$ is bounded on $[\mathrm{a}, \mathrm{b}], \mathrm{f}$ is continuous at s , and $\alpha(\mathrm{x})=$ $\mathrm{I}(\mathrm{x}-\mathrm{s})$, then

$$
\int_{a}^{b} f d \alpha=f(s)
$$

Proof. Consider partitions $P=\left\{x_{0}, x_{1}, x_{2}, x_{3}\right\}$, where $x_{0}=a$, and $x_{1}=s<x_{2}<$ $x_{3}=b$. Then

$$
U(P, f, \alpha)=M_{2}, \quad L(P, f, \alpha)=m_{2}
$$

Since $f$ is continuous at $s$, we see that $M_{2}$ and $m_{2}$ converge to $f(s)$ as $x_{2} \rightarrow s$.
6.16 Theorem. Suppose $\mathrm{c}_{n} \geq 0$ for $1,2,3, \ldots, \Sigma \mathrm{c}_{n}$ converges, $\left(\mathrm{s}_{\mathrm{n}}\right)$ is a sequence of distinct points in ( $\mathrm{a}, \mathrm{b}$ ), and

$$
\alpha(x)=\sum_{n=1}^{\infty} c_{n} I\left(x-s_{n}\right)
$$

Let f be continuous on $[\mathrm{a}, \mathrm{b}]$. Then

$$
\int_{a}^{b} f d \alpha=\sum_{n=1}^{\infty} f\left(s_{n}\right)
$$

Proof. The comparison test shows that the series (6.22) converges for every x . Its sum $\alpha(x)$ is evidently monotonic, and $\alpha(a)=0, \alpha(b)=\Sigma c_{n}$. (This is the type of function that occurred in Remark 4.31.)

Let $\varepsilon>0$ be given, and choose N so that

$$
\sum_{n=N+1}^{\infty} c_{n}<\varepsilon
$$

Put

$$
\alpha_{1}(x)=\sum_{n=1}^{N} c_{n} I\left(x-s_{n}\right), \quad \alpha_{2}(x)=\sum_{n=N+1}^{\infty} c_{n} I\left(x-s_{n}\right)
$$

By Theorems 6.12 and 6.15 ,

$$
\int_{a}^{b} f d \alpha_{1}=\sum_{i=1}^{N} c_{n} f\left(s_{n}\right)
$$

Since $\alpha_{2}(b)-\alpha_{2}(a)<\varepsilon$,

$$
\left|\int_{a}^{b} f d \alpha_{2}\right| \leq M \varepsilon
$$

where $M=\sup |f(x)|$. Since $\alpha=\alpha_{1}+\alpha_{2}$, it follows from (6.24) and (6.25) that

$$
\left|\int_{a}^{b} f d \alpha-\sum_{i=1}^{N} c_{n} f\left(s_{n}\right)\right| \leq M \varepsilon
$$

If we let $\mathrm{N} \rightarrow \infty$, we obtain (6.23).
6.17 Theorem. Assume $\alpha$ increases monotonically and $\alpha^{\prime} \in \mathscr{R}$ on [a,b]. Let f be a bounded real function on $[\mathrm{a}, \mathrm{b}]$. Then $\mathrm{f} \in \mathscr{R}(\alpha)$ if and only if $\mathrm{f} \alpha^{\prime} \in \mathscr{R}$. In that case

$$
\int_{a}^{b} f d \alpha=\int_{a}^{b} f(x) \alpha^{\prime}(x) d x
$$

Proof. Let $\varepsilon>0$ be given and apply Theorem 6.6 to $\alpha^{\prime}$ : There is a partition $\mathrm{P}=$ $\left\{\mathrm{x}_{0}, \ldots, \mathrm{x}_{\mathrm{n}}\right\}$ of $[\mathrm{a}, \mathrm{b}]$ such that

$$
U\left(P, \alpha^{\prime}\right)-L\left(P, \alpha^{\prime}\right)<\varepsilon
$$

The mean value theorem furnishes points $t_{i} \in\left\{x_{i-1}, x_{i}\right\}$ such that

$$
\Delta \alpha_{i}=\alpha^{\prime}\left(t_{i}\right) \Delta x_{i}
$$

for $i=1, \ldots, n$. If $s_{i} \in\left\{x_{i-1}, x_{i}\right\}$, then

$$
\sum_{i=1}^{n}\left|\alpha^{\prime}\left(s_{i}\right)-\alpha^{\prime}\left(t_{i}\right)\right| \Delta x_{i}<\varepsilon
$$

by (6.28) and Theorem 6.7(b). Put $M=\sup |f(x)|$. Since

$$
\sum_{i=1}^{n} f\left(s_{i}\right) \Delta \alpha_{i}=\sum_{i=1}^{n} f\left(s_{i}\right) \alpha^{\prime}\left(t_{i}\right) \Delta x_{i}
$$

it follows from (6.29) that

$$
\left|\sum_{i=1}^{n} f\left(s_{i}\right) \Delta \alpha_{i}-\sum_{i=1}^{n} f\left(s_{i}\right) \alpha^{\prime}\left(s_{i}\right) \Delta x_{i}\right| \leq M \varepsilon
$$

In particular,

$$
\sum_{i=1}^{n} f\left(s_{i}\right) \Delta \alpha_{i} \leq U\left(P, f \alpha^{\prime}\right)+M \varepsilon
$$

for all choices of $s_{i} \in\left[x_{i-1}, x_{i}\right]$, so that

$$
U(P, f, \alpha) \leq U\left(P, f \alpha^{\prime}\right)+M \varepsilon
$$

The same argument leads from (6.30) to

$$
U\left(P, f \alpha^{\prime}\right) \leq U(P, f, \alpha)+M \varepsilon
$$

Thus

$$
|U(P, f, \alpha)-U\left(P, f \alpha^{\prime}\right)| \leq M \varepsilon
$$

Now note that (6.28) remains true if P is replaced by any refinement. Hence (6.31) remains true. We conclude that

$$
\left|\int_{a}^{b} f d \alpha-\int_{a}^{b} f(x) \alpha^{\prime}(x) d x\right| \leq M \varepsilon
$$

But $\varepsilon$ is arbitrary. Hence

$$
\int_{a}^{b} f d \alpha=\int_{a}^{b} f(x) \alpha^{\prime}(x) d x
$$

for any bounded $f$. The equality of the lower integrals follows from (6.30) in exactly the same way. The theorem follows.
6.18 Remark. The two preceding theorems illustrate the generality and flexibility which are inherent in the Stieltjes process of integration. If $\alpha$ is a pure step function [this is the name often given to functions of the form (6.22)], the integral reduces to a finite or infinite series. If $\alpha$ has an integrable derivative, the integral reduces to an ordinary Riemann integral. This makes it possible in many cases to study series and integrals simultaneously, rather than separately.

To illustrate this point, consider a physical example. The moment of inertia of a straight wire of unit length, about an axis through an endpoint, at right angles to the wire, is

$$
\int_{0}^{1} x^{2} d m
$$

where $m(x)$ is the mass contained in the interval $[0, x]$. If the wire is regarded as having continuous density $\rho$, that is, if $m^{\prime}(x)=\rho(x)$, then (6.33) turns into

$$
\int_{0}^{1} x^{2} \rho(x) d x
$$

On the other hand, if the wire is composed of masses $m_{i}$ concentrated at points

$\mathrm{x}_{\mathrm{L}},(6.33)$ becomes

$$
\sum_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^{2} \mathrm{~m}_{\mathrm{i}}
$$

Thus (6.33) contains (6.34) and (6.35) as special cases, but it contains much more; for instance, the case in which $m$ is continuous but not everywhere differentiable.
6.19 Theorem (Change of Variable). Suppose $\phi$ is a strictly increasing continuous function that maps an interval $[A, B]$ onto $[a, b]$. Suppose $\alpha$ is monotonically increasing on $[a, b]$ and $f \in \mathscr{R}(\alpha)$ on $[a, b]$. Define $\beta$ and $g$ on $[A, B]$ by

$$
\beta(\mathrm{y})=\alpha(\phi(\mathrm{y})), \quad \mathrm{g}(\mathrm{y})=\mathrm{f}(\phi(\mathrm{y}))
$$

Then $\mathrm{g} \in \mathscr{R}(\beta)$ and

$$
\int_{A}^{B} g d \beta=\int_{a}^{b} f d \alpha
$$

Proof. To each partition $\mathrm{P}=\left\{\mathrm{x}_{0}, \ldots, \mathrm{x}_{\mathrm{n}}\right\}$ of $[a, b]$ corresponds a partition $\mathrm{Q}=$ $\left\{y_{0}, \ldots, y_{n}\right\}$ of $[A, B]$, so that $x_{i}=\phi\left(y_{i}\right)$. All partitions of $[A, B]$ are obtained in this way. Since the values taken by $f$ on $\left\{x_{i-1}, x_{i}\right\}$ are exactly the same as those taken by $g$ on $\left[y_{i-1}, y_{i}\right]$, we see that

$$
U(Q, g, \beta)=U(P, f, \alpha), \quad L(Q, g, \beta)=L(P, f, \alpha)
$$

Since $f \in \mathscr{R}(\alpha), P$ can be chosen so that both $U(P, f, \alpha)$ and $L(P, f, \alpha)$ are close to $\int f d \alpha$. Hence (6.38) combined with Theorem 6.6, shows that $g \in \mathscr{R}(\beta)$ and that (6.37) holds. This completes the proof.

Let us note the following special case: Take $\alpha(x)=x$. Then $\beta=\phi$. Assume $\phi^{\prime} \in \mathscr{R}$ on $[A, B]$. If Theorem 6.17 is applied to the left side of (6.37), we obtain

$$
\int_{a}^{b} f(x) d x=\int_{A}^{B} f(\phi(y)) \phi^{\prime}(y) d y
$$

# INTEGRATION AND DIFFERENTIATION 

We still confine ourselves to real functions in this section. We shall show that integration and differentiation are, in a certain sense, inverse operations.
6.20 Theorem. Let $\mathrm{f} \in \mathscr{R}$ on $[\mathrm{a}, \mathrm{b}]$. For $\mathrm{a} \leq \mathrm{x} \leq \mathrm{b}$, put

$$
\mathrm{F}(\mathrm{x})=\int_{\mathrm{a}}^{\mathrm{x}} \mathrm{f}(\mathrm{t}) \mathrm{dt}
$$

Then F is continuous on [a, b]; furthermore, if f is continuous at a point $\mathrm{x}_{0}$ of $[\mathrm{a}, \mathrm{b}]$, then F is differentiable at $\mathrm{x}_{0}$, and

$$
\mathrm{F}^{\prime}\left(\mathrm{x}_{0}\right)=\mathrm{f}\left(\mathrm{x}_{0}\right)
$$

Proof. Since $f \in \mathscr{R}, f$ is bounded. Suppose $|f(t)| \leq M$ for $a \leq t \leq b$. If $a \leq x<$ $y \leq b$, then

$$
|F(y)-F(x)|=\left|\int_{x}^{y} f(t) d t\right| \leq M(y-x)
$$

by Theorem 6.12(c) and (d). Given $\varepsilon>0$, we see that

$$
|F(y)-F(x)|<\varepsilon
$$

provided that $|y-x|<\varepsilon / M$. This proves continuity (and, in fact, uniform continuity) of $F$.

Now suppose $f$ is continuous at $x_{0}$. Given $\varepsilon>0$, choose $\delta>0$ such that

$$
\left|f(t)-f\left(x_{0}\right)\right|<\varepsilon
$$

if $\left|t-x_{0}\right|$, and $a \leq t \leq b$. Hence, if

$$
x_{0}-\delta<s \leq x_{0} \leq t<x_{0}+\delta \quad \text { and } \quad a \leq s<t \leq b
$$

we have, by Theorem 6.12(d),

$$
\left|\frac{F(t)-F(s)}{t-s}-f\left(x_{0}\right)\right|=\left|\frac{1}{t-s} \int_{s}^{t}\left[f(u)-f\left(x_{0}\right)\right] d u\right|<\varepsilon
$$

It follows that $F^{\prime}\left(x_{0}\right)=f\left(x_{0}\right)$.
6.21 Theorem (The Fundamental Theorem of Calculus). If $\mathrm{f} \in \mathscr{R}$ on $[\mathrm{a}, \mathrm{b}]$ and if there is a differentiable function F on $[\mathrm{a}, \mathrm{b}]$ such that $\mathrm{F}^{\prime}=\mathrm{f}$, then

$$
\int_{a}^{b} f(x) d x=F(b)-F(a)
$$

Proof. Let $\varepsilon>0$ be given. Choose a partition $P=\left\{x_{0}, \ldots, x_{n}\right\}$ of $[a, b]$ so that $U(P, f)-L(P, f)<\varepsilon$. The mean value theorem furnishes points $t_{i} \in\left\{x_{i-1}, x_{i}\right\}$ such that

$$
F\left(x_{i}\right)-F\left(x_{i-1}\right)=f\left(t_{i}\right) \Delta x_{i}
$$

for $\mathrm{i}=1, \ldots, \mathrm{n}$. Thus

$$
\sum_{i=1}^{n} f\left(t_{i}\right) \Delta x_{i}=F(b)-F(a)
$$

It now follows from Theorem 6.7(c) that

$$
\left|F(b)-F(a)-\int_{a}^{b} f(x) d x\right|<\varepsilon
$$

Since this holds for every $\varepsilon>0$, the proof is complete.

6.22 Theorem (Integration by Parts). Suppose F and G are differentiable functions on $[\mathrm{a}, \mathrm{b}], \mathrm{F}^{\prime}=\mathrm{f} \in \mathscr{R}$, and $\mathrm{G}^{\prime}=\mathrm{g} \in \mathscr{R}$. Then

$$
\int_{a}^{b} F(x) g(x) d x=F(b) G(b)-F(a) G(a)-\int_{a}^{b} f(x) G(x) d x
$$

Proof. Put $H(x)=F(x) G(x)$ and apply Theorem 6.21 to $H$ and its derivative. Note that $\mathrm{H}^{\prime} \in \mathscr{R}$ by Theorem 6.13 .
6.23 Definition. Let $f_{1}, \ldots, f_{k}$ be real functions on $[a, b]$, and let $f=\left(f_{1}, \ldots, f_{k}\right)$ be the corresponding mapping of $[a, b]$ into $\mathbb{R}^{k}$. If $\alpha$ increases monotonically on $[a, b]$, to say that $f \in \mathscr{R}(\alpha)$ means that $f_{j} \in \mathscr{R}(\alpha)$ for $j=1, \ldots, k$. If this is the case, we define

$$
\int_{a}^{b} f d \alpha=\left(\int_{a}^{b} f_{1} d \alpha, \ldots, \int_{a}^{b} f_{k} d \alpha\right)
$$

In other words, $\int \mathbf{f} \mathrm{d} \alpha$ is the point in $\mathbb{R}^{\mathrm{k}}$ whose jth coordinate is $\int \mathrm{f}_{\mathrm{j}} \mathrm{d} \alpha$.
It is clear that parts (a), (c), and (e) of Theorem 6.12 are valid for these vectorvalued integrals; we simply apply the earlier results to each coordinate. The same is true of Theorems $6.17,6.20$, and 6.21 . To illustrate, we state the analogue of Theorem 6.21 .
6.24 Theorem. If $\mathbf{f}$ and $\mathbf{F}$ map $[a, b]$ into $\mathbb{R}^{k}$, if $\mathbf{f} \in \mathscr{R}$ on $[a, b]$, and if $\mathbf{F}^{\prime}=\mathbf{f}$, then

$$
\int_{a}^{b} f(t) d t=F(b)-F(a)
$$

The analogue of Theorem 6.13(b) offers some new features, however, at least in its proof.
6.25 Theorem. If $\mathbf{f}$ maps $[a, b]$ into $\mathbb{R}^{k}$ and if $\mathbf{f} \in \mathscr{R}(\alpha)$ for some monotonically increasing function $\alpha$ on $[a, b]$, then $|\mathbf{f}| \in \mathscr{R}(\alpha)$, and

$$
\left|\int_{a}^{b} f d \alpha\right| \leq \int_{a}^{b}|f| d \alpha
$$

Proof. If $f_{1}, \ldots, f_{k}$ are the components of $f$, then

$$
|\mathbf{f}|=\left(\mathrm{f}_{1}^{2}+\cdots+\mathrm{f}_{\mathrm{k}}^{2}\right)^{1 / 2}
$$

By Theorem 6.11, each of the functions $f_{i}^{2}$ belongs to $\mathscr{R}(\alpha)$; hence so does their sum. Since $x^{2}$ is a continuous function of $x$, Theorem 4.17 shows that the squareroot function is continuous on $[0, M]$, for every real $M$. If we apply Theorem 6.11 once more, (6.41) shows that $|\mathbf{f}| \in \mathscr{R}(\alpha)$.

To prove (6.40), put $\mathbf{y}=\left(y_{1}, \ldots, y_{k}\right)$, where $y_{j}=\int f_{j} d \alpha$. Then we have $\mathbf{y}=$

$\int \mathbf{f} \mathrm{d} \alpha$, and

$$
|\mathbf{y}|^{2}=\sum y_{j}^{2}=\sum y_{j} \int f_{j} d \alpha=\int\left(\sum y_{j} f_{j}\right) d \alpha
$$

By the Schwarz inequality,

$$
\sum y_{j} f_{j}(t) \leq|\mathbf{y}||\mathbf{f}(t)| \quad(\mathfrak{a} \leq \mathrm{t} \leq \mathrm{b})
$$

hence Theorem 6.12(b) implies

$$
|\mathbf{y}|^{2} \leq|\mathbf{y}| \int|\mathbf{f}| \mathrm{d} \alpha
$$

If $\mathbf{y}=\mathbf{0}$, (6.40) is trivial. If $\mathbf{y} \neq \mathbf{0}$, division of (6.43) by $|\mathbf{y}|$ gives (6.40).

# RECTIFIABLE CURVES 

We conclude this chapter with a topic of geometric interest which provides us an application of some of the preceding theory. The case $\mathrm{k}=2$ (i.e., the case of plane curves) is of considerable importance in the study of analytic functions of a complex variable.
6.26 Definition. A continuous mapping $\gamma$ of an interval $[\mathfrak{a}, \mathrm{b}]$ into $\mathbb{R}^{\mathrm{k}}$ is called a curve in $\mathbb{R}^{\mathrm{k}}$. To emphasize the parameter interval $[\mathfrak{a}, \mathrm{b}]$, we may also say that $\gamma$ is a curve on $[\mathfrak{a}, \mathrm{b}]$.

- If $\gamma$ is one-to-one, $\gamma$ is called an arc.
- If $\gamma(\mathfrak{a})=\gamma(\mathrm{b}), \gamma$ is said to be a closed curve.

It should be noted that we define a curve to be a mapping, not a point set. Of course, with each curve $\gamma$ in $\mathbb{R}^{\mathrm{k}}$, there is an associated subset of $\mathbb{R}^{\mathrm{k}}$, namely the range of $\gamma$, but different curves may have the same range.

We associate to each partition $\mathrm{P}=\left\{\mathrm{x}_{0}, \ldots, \mathrm{x}_{\mathrm{n}}\right\}$ of $[\mathfrak{a}, \mathrm{b}]$ and to each curve $\gamma$ on $[\mathfrak{a}, \mathrm{b}]$ the number

$$
\Lambda(\mathrm{P}, \gamma)=\sum_{\mathrm{i}=1}^{\mathrm{n}}\left|\gamma\left(\mathrm{x}_{\mathrm{i}}\right)-\gamma\left(\mathrm{x}_{\mathrm{i}-1}\right)\right|
$$

The ith term in this sum is the distance (in $\mathbb{R}^{\mathrm{k}}$ ) between the points $\gamma\left(\mathrm{x}_{\mathrm{i}-1}\right)$ and $\gamma\left(\mathrm{x}_{\mathrm{i}}\right)$. Hence $\Lambda(\mathrm{P}, \gamma)$ is the length of the polygonal path with vertices at $\gamma\left(\mathrm{x}_{0}\right)$, $\gamma\left(\mathrm{x}_{1}\right), \ldots, \gamma\left(\mathrm{x}_{\mathrm{n}}\right)$, in this order. As our partition becomes finer and finer, this polygon approaches the range of $\gamma$ more and more closely. This makes it seem reasonable to define the length of $\gamma$ as

$$
\Lambda(\gamma)=\sup \Lambda(\mathrm{P}, \gamma)
$$

where the supremum is taken over all partitions of $[\mathfrak{a}, \mathrm{b}]$.
If $\Lambda(\gamma)<\infty$, we say that $\gamma$ is rectifiable.

In certain cases, $\Lambda(\gamma)$ is given by a Riemann integral. We shall prove this for continuously differentiable curves, i.e., for curves $\gamma$ whose derivative $\gamma^{\prime}$ is continuous.
6.27 Theorem. If $\gamma^{\prime}$ is continuous on $[a, b]$, then $\gamma$ is rectifiable, and

$$
\Lambda(\gamma)=\int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t
$$

Proof. If $a \leq x_{i-1}<x_{i} \leq b$, then

$$
\left|\gamma\left(x_{i}\right)-\gamma\left(x_{i-1}\right)\right|=\left|\int_{x_{i-1}}^{x_{i}} \gamma^{\prime}(t) d t\right| \leq \int_{x_{i-1}}^{x_{i}}\left|\gamma^{\prime}(t)\right| d t
$$

Hence

$$
\Lambda(P, \gamma) \leq \int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t
$$

for every partition $P$ of $[a, b]$. Consequently,

$$
\Lambda(\gamma) \leq \int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t
$$

To prove the opposite inequality, let $\varepsilon>0$ be given. Since $\gamma^{\prime}$ is uniformly continuous on $[a, b]$, there exists $\delta>0$ such that

$$
\left|\gamma^{\prime}(s)-\gamma^{\prime}(t)\right|<\varepsilon \quad \text { if }|s-t|<\delta
$$

Let $P=\left\{x_{0}, \ldots, x_{n}\right\}$ be a partition of $[a, b]$, with $\Delta x_{i}<\delta$ for all $i$. If $x_{i-1} \leq t \leq x_{i}$, it follows that

$$
\left|\gamma^{\prime}(t)\right| \leq\left|\gamma^{\prime}\left(x_{i}\right)\right|+\varepsilon
$$

Hence

$$
\begin{aligned}
\int_{x_{i-1}}^{x_{i}}\left|\gamma^{\prime}(t)\right| d t & \leq\left|\gamma^{\prime}\left(x_{i}\right)\right| \Delta x_{i}+\varepsilon \Delta x_{i} \\
& =\left|\int_{x_{i-1}}^{x_{i}}\left|\gamma^{\prime}(t)+\gamma^{\prime}\left(x_{i}\right)-\gamma^{\prime}(t)\right| d t\right|+\varepsilon \Delta x_{i} \\
& \leq\left|\int_{x_{i-1}}^{x_{i}} \gamma^{\prime}(t) d t\right|+\left|\int_{x_{i-1}}^{x_{i}}\left|\gamma^{\prime}\left(x_{i}\right)-\gamma^{\prime}(t)\right| d t\right|+\varepsilon \Delta x_{i} \\
& \leq\left|\gamma\left(x_{i}\right)-\gamma\left(x_{i-1}\right)\right|+2 \varepsilon \Delta x_{i}
\end{aligned}
$$

If we add these inequalities, we obtain

$$
\int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t \leq \Lambda(P, \gamma)+2 \varepsilon(b-a) \leq \Lambda(y)+2 \varepsilon(b-a)
$$

Since $\varepsilon$ was arbitrary,

$$
\int_{a}^{b}\left|y^{\prime}(t)\right| d t \leq \Lambda(y)
$$

This completes the proof.

# EXERCISES 

6.1. Suppose $\alpha$ increases on $[a, b], a \leq x_{0} \leq b, \alpha$ is continuous at $x_{0}, f\left(x_{0}\right)=1$, and $f(x)=0$ if $x \neq x_{0}$. Prove that $f \in \mathscr{R}(\alpha)$ and that $\int f d \alpha=0$.
6.2. Suppose $f \geq 0, f$ is continuous on $[a, b]$, and $\int_{a}^{b} f(x) d x=0$. Prove that $f(x)=0$ for all $x \in[a, b]$. (Compare this with Exercise 6.1.)
6.3. Define three functions $\beta_{1}, \beta_{2}, \beta_{3}$ as follows: $\beta_{j}(x)=0$ if $x<0, \beta_{j}(x)=1$ if $x>0$ for $j=1,2,3$; and $\beta_{1}(0)=0, \beta_{2}(0)=1, \beta_{3}(0)=1 / 2$. Let $f$ be a bounded function on $[-1,1]$.
(a) Prove that $f \in \mathscr{R}\left(\beta_{1}\right)$ if and only if $f(0+)=f(0)$ and that then

$$
\int f d \beta_{1}=f(0)
$$

(b) State and prove a similar result for $\beta_{2}$.
(c) Prove that $f \in \mathscr{R}\left(\beta_{3}\right)$ if and only if $f$ is continuous at 0 .
(d) If $f$ is continuous at 0 prove that

$$
\int f d \beta_{1}=\int f d \beta_{2}=\int f d \beta_{3}=f(0)
$$

6.4. If $f(x)=0$ for all irrational $x, f(x)=1$ for all rational $x$, prove that $f \notin \mathscr{R}$ on $[a, b]$ for any $a<b$.
6.5. Suppose $f$ is a bounded real function on $[a, b]$ and $f^{2} \in \mathscr{R}$ on $[a, b]$. Does it follow that $f \in \mathscr{R}$ ? Does the answer chance if we assume that $f^{3} \in \mathscr{R}$ ?
6.6. Let $P$ be the Cantor set constructed in Theorem 2.44. Let $f$ be a bounded real function on $[0,1]$ which is continuous at every point outside $P$. Prove that $f \in \mathscr{R}$ on $[0,1]$. Hint: $P$ can be covered by finitely many segments whose total length can be made as small as desired. Proceed as in Theorem 6.10.
6.7. Suppose $f$ is a real function on $[0,1]$ and $f \in \mathscr{R}$ on $[c, 1]$ for every $c>0$. Define

$$
\int_{0}^{1} f(x) d x=\lim _{c \rightarrow 0} \int_{c}^{1} f(x) d x
$$

if this limit exists (and is finite).
(a) If $f \in \mathscr{R}$ on $[0,1]$, show that this definition of the integral agrees with the old one.
(b) Construct a function $f$ such that the above limit exists, although it fails to exist with $|f|$ in place of $f$.
6.8. Suppose $f \in \mathscr{R}$ on $[a, b]$ for every $b>a$ where $a$ is fixed. Define

$$
\int_{a}^{\infty} f(x) d x=\lim _{b \rightarrow \infty} \int_{a}^{b} f(x) d x
$$

if this limit exists (and is finite). In that case, we say that the integral on the left converges. If it also converges after $f$ has been replaced by $|f|$, it is said to converge absolutely.

Assume that $f(x) \geq 0$ and that $f$ decreases monotonically on $[1, \infty)$. Prove that

$$
\int_{1}^{\infty} f(x) d x
$$

converges if and only if

$$
\sum_{n=1}^{\infty} f(n)
$$

converges. (This is the so-called "integral test" for convergence of series.)
6.9. Show that integration by parts can sometimes be applied to the "improper" integrals defined in Exercises 6.7 and 6.8. (State the appropriate hypotheses, formulate a theorem, and prove it.) For instance show that

$$
\int_{0}^{\infty} \frac{\cos x}{1+x} d x=\int_{0}^{\infty} \frac{\sin x}{(1+x)^{2}} d x
$$

Show that one of these integrals converges absolutely, but that the other does not.
6.10. Let $p$ and $q$ be positive real numbers such that

$$
\frac{1}{p}+\frac{1}{q}=1
$$

Prove the following statements.
(a) If $u \geq 0$ and $v \geq 0$, then

$$
u v \leq \frac{u^{p}}{p}+\frac{v^{q}}{q}
$$

Equality holds if and only if $u^{p}=v^{q}$.
(b) If $f \in \mathscr{R}(\alpha), g \in \mathscr{R}(\alpha), f \geq 0, g \geq 0$, and

$$
\int_{a}^{b} f^{p} d \alpha=1=\int_{a}^{b} g^{q} d \alpha
$$

then

$$
\int_{a}^{b} f g d \alpha \leq 1
$$

(c) If $f$ and $g$ are complex functions in $\mathscr{R}(\alpha)$, then

$$
\left|\int f g d \alpha\right| \leq\left\{\int_{a}^{b}|f|^{p} d \alpha\right\}^{1 / p}\left\{\int_{a}^{b}|g|^{q} d \alpha\right\}^{1 / q}
$$

This is Hölder's inequality. When $p=q=2$, it is usually called the Schwarz inequality. (Note that Theorem 1.35 is a very special case of this.)
(d) Show that Hölder's inequality is also true for the "improper" integrals described in Exercises 6.7 and 6.8.
6.11. Let $\alpha$ be a fixed increasing function on $[a, b]$. For $u \in \mathscr{R}(\alpha)$, define

$$
\|u\|_{2}=\left\{\int_{a}^{b}|u|^{2}\right\}^{1 / 2}
$$

Suppose $f, g, h \in \mathscr{R}(\alpha)$, and prove the triangle inequality

$$
\|f-h\|_{2} \leq\|f-g\|_{2}+\|g-h\|_{2}
$$

as a consequence of the Schwarz inequality, as in the proof of Theorem 1.37.

6.12. With the notations of Exercise 6.11, suppose $f \in \mathscr{R}(\alpha)$ and $\varepsilon>0$. Prove that there exists a continuous function $g$ on $[a, b]$ such that $\|f-g\|_{2}<\varepsilon$.

Hint: Let $P=\left\{x_{0}, \ldots, x_{n}\right\}$ be a suitable partition on $[a, b]$, define

$$
g(t)=\frac{x_{i}-t}{\Delta x_{i}} f\left(x_{i-1}\right)+\frac{t-x_{i-1}}{\Delta x_{i}} f\left(x_{i}\right)
$$

if $x_{i-1} \leq t \leq x_{i}$.
6.13. Define

$$
f(x)=\int_{x}^{x+1} \sin \left(t^{2}\right) d t
$$

(a) Prove that $|f(x)|<1 / x$ if $x>0$.

Hint: Put $t^{2}=u$ and integrate by parts, to show that $f(x)$ is equal to

$$
\frac{\cos \left(x^{2}\right)}{2 x}-\frac{\cos \left[(x+1)^{2}\right]}{2(x+1)}-\int_{x^{2}}^{(x+1)^{2}} \frac{\cos u}{4 u^{3 / 2}} d u
$$

Replace $\cos u$ by -1 .
(b) Prove that

$$
2 x f(x)=\cos \left(x^{2}\right)-\cos \left[(x+1)^{2}\right]+r(x)
$$

where $|r(x)|<c / x$ and $c$ is a constant.
(c) Find the upper and lower limits of $x f(x)$ as $x \rightarrow \infty$.
(d) Does $\int_{0}^{\infty} \sin \left(t^{2}\right) d t$ converge?
6.14. Deal similarly with

$$
f(x)=\int_{x}^{x+1} \sin \left(e^{t}\right) d t
$$

Show that

$$
e^{x}|f(x)|<2
$$

and that

$$
e^{x} f(x)=\cos \left(e^{x}\right)-e^{-1} \cos \left(e^{x+1}\right)+r(x)
$$

where $|r(x)|<C e^{-x}$ for some constant $C$.
6.15. Suppose $f$ is a real, continuously differentiable function on $[a, b], f(a)=f(b)=0$, and

$$
\int_{a}^{b} f^{2}(x) d x=1
$$

Prove that

$$
\int_{a}^{b} x f(x) f^{\prime}(x) d x=-\frac{1}{2}
$$

and that

$$
\int_{a}^{b}\left[f^{\prime}(x)\right]^{2} d x \cdot \int_{a}^{b} x^{2} f^{2}(x) d x>\frac{1}{4}
$$

6.16. For $1<s<\infty$, define

$$
\zeta(s)=\sum_{n=1}^{\infty} \frac{1}{n^{s}}
$$

(This is Riemann's zeta function, of great importance in the study of the distribution of prime numbers.) Prove that
(a) $\zeta(s)=s \int_{1}^{\infty} \frac{[x]}{x^{s+1}} d x$,

(b) $\zeta(s)=\frac{s}{s-1}-s \int_{1}^{\infty} \frac{x-[x]}{x^{s+1}} d x$,
where $[x]$ denotes the greatest integer $\leq x$.
Prove that the integral in (b) converges for all $s>0$.
Hint: To prove (a), compute the difference between the integral over $[1, \mathrm{~N}]$ and the Nth partial sum of the series that defines $\zeta(s)$.
6.17. Suppose $\alpha$ increases monotonically on $[a, b], g$ is continuous, and $g(x)=G^{\prime}(x)$ for $a \leq x \leq b$. Prove that

$$
\int_{a}^{b} \alpha(x) g(x) d x=G(b) \alpha(b)-G(a) \alpha(a)-\int_{a}^{b} G d \alpha
$$

Hint: Take $g$ real, without loss of generality. Given $P=\left\{x_{0}, x_{1}, \ldots, x_{n}\right\}$, choose $t_{i} \in$ $\left(x_{i-1}, x_{i}\right)$ so that $g\left(t_{i}\right) \Delta x_{i}=G\left(x_{i}\right)-G\left(x_{i-1}\right)$. Show that

$$
\sum_{i=1}^{n} \alpha\left(x_{i}\right) g\left(t_{i}\right) \Delta x_{i}=G(b) \alpha(b)-G(a) \alpha(a)-\sum_{i=1}^{n} G\left(x_{i-1}\right) \Delta \alpha_{i}
$$

6.18. Let $\gamma_{1}, \gamma_{2}, \gamma_{3}$ be curves in the complex plane defined on $[0,2 \pi]$ by

$$
\gamma_{1}(t)=e^{i t}, \quad \gamma_{2}(t)=e^{2 i t}, \quad \gamma_{3}(t)=e^{2 \pi i t \sin (1 / t)}
$$

Show that these curves have the same range, that $\gamma_{1}$ and $\gamma_{2}$ are rectifiable, that the length of $\gamma_{1}$ is $2 \pi$, that the length of $\gamma_{2}$ is $4 \pi$, and that $\gamma_{3}$ is not rectifiable.
6.19. Let $\gamma_{1}$ be a curve in $\mathbb{R}^{\mathrm{k}}$ defined on $[a, b]$; let $\phi$ be a continuous 1-1 mapping of $[c, d]$ into $[a, b]$ such that $\phi(c)=a$; and define $\gamma_{2}(s)=\gamma_{1}(\phi(s))$. Prove that $\gamma_{2}$ is an arc, a closed curve, or a rectifiable curve if and only if the same is true of $\gamma_{1}$. Prove that $\gamma_{2}$ and $\gamma_{1}$ have the same length.

# Chapter 7 

## SEQUENCES AND SERIES OF FUNCTIONS

In the present chapter we confine our attention to complex-valued functions (including the real-valued ones, of course), although many of the theorems and proofs which follow extend without difficulty to vector-valued functions, and even to mappings into general metric spaces. We choose to stay within this simple framework in order to focus attention on the most important aspects of the problems that arise when limit processes are interchanged.

## DISCUSSION OF THE MAIN PROBLEM

7.1 Definition. Suppose $\left(f_{n}\right)_{n=1}^{\infty}$ is a sequence of functions defined on a set $E$, and suppose that the sequence of numbers $\left(f_{n}(x)\right)$ converges for every $x \in E$. We can then define a function $f$ by

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x) \quad(x \in E)
$$

Under these circumstances we say that $\left(f_{n}\right)$ converges on $E$ and that $f$ is the limit, or the limit function, of $\left(f_{n}\right)$. Sometimes we shall use a more descriptive terminology and shall say that " $\left(f_{n}\right)$ converges to $f$ pointwise on $E$ " if (7.1) holds. Similarly, if $\Sigma f_{n}(x)$ converges for every $x \in E$, and if we define

$$
f(x)=\sum_{n=1}^{\infty} f_{n}(x) \quad(x \in E)
$$

the function $f$ is called the sum of the series $\Sigma f_{n}$.
The main problem which arises is to determine whether important properties of functions are preserved under the limit operations (7.1) and (7.2). For instance, if the functions $f_{n}$ are continuous, or differentiable, or integrable, is the same true

of the limit function? What are the relations between $f_{n}^{\prime}$ and $f^{\prime}$, say, or between the integrals of $f_{n}$ and that of $f$ ?

To say that $f$ is continuous at a limit point $x$ means

$$
\lim _{t \rightarrow x} f(t)=f(x)
$$

Hence, to ask whether the limit of a sequence of continuous functions is continuous is the same as to ask whether

$$
\lim _{t \rightarrow x} \lim _{n \rightarrow \infty} f_{n}(t)=\lim _{n \rightarrow \infty} \lim _{t \rightarrow x} f_{n}(t)
$$

i.e., whether the order in which limit processes are carried out is immaterial. On the left side of (7.3), we first set $n \rightarrow \infty$, then $t \rightarrow x$; on the right side, $t \rightarrow x$ first, then $n \rightarrow \infty$.

We shall now show by means of several examples that limit processes cannot in general be interchanged without affecting the result. Afterward, we shall prove that under certain conditions the order in which limit operations are carried out is immaterial.

Our first example, and the simplest one, concerns a "double sequence."
7.2 Example. For $m=1,2,3, \ldots, n=1,2,3, \ldots$, let

$$
s_{m, n}=\frac{m}{m+n}
$$

Then, for every fixed $n$,

$$
\lim _{m \rightarrow \infty} s_{m, n}=1
$$

so that

$$
\lim _{n \rightarrow \infty} \lim _{m \rightarrow \infty} s_{m, n}=1
$$

On the other hand, for every fixed $m$,

$$
\lim _{n \rightarrow \infty} s_{m, n}=0
$$

so that

$$
\lim _{m \rightarrow \infty} \lim _{n \rightarrow \infty} s_{m, n}=0
$$

7.3 Example. Let

$$
f_{n}(x)=\frac{x^{2}}{\left(1+x^{2}\right)^{n}} \quad(x \text { real } ; n=0,1,2, \ldots)
$$

and consider

$$
f(x)=\sum_{n=0}^{\infty} f_{n}(x)=\sum_{n=0}^{\infty} \frac{x^{2}}{\left(1+x^{2}\right)^{n}}
$$

Since $f_{n}(0)=0$, we have $f(0)=0$. For $x \neq 0$, the last series in (7.6) is a convergent geometric series with sum $1+x^{2}$ (Theorem 3.26). Hence

$$
f(x)= \begin{cases}0 & (x=0) \\ 1+x^{2} & (x \neq 0)\end{cases}
$$

so that a convergent series of continuous functions may have a discontinuous sum.
7.4 Example. For $m=1,2,3, \ldots$, put

$$
f_{m}(x)=\lim _{n \rightarrow \infty}(\cos m!\pi x)^{2 n}
$$

When $m!x$ is an integer, $f_{m}(x)=1$. For all other values of $x, f_{m}(x)=0$. Now let

$$
f(x)=\lim _{m \rightarrow \infty} f_{m}(x)
$$

For irrational $x, f_{m}(x)=0$ for every $m$; hence $f(x)=0$. For rational $x$, say $x=p / q$, where $p$ and $q$ are integers, we see that $m!x$ is an integer if $m \geq q$, so that $f(x)=1$. Hence

$$
\lim _{m \rightarrow \infty} \lim _{n \rightarrow \infty}(\cos m!\pi x)^{2 n}= \begin{cases}0 & (x \text { irrational }) \\ 1 & (x \text { rational })\end{cases}
$$

We have thus obtained an everywhere discontinuous limit function, which is not Riemann-integrable (Exercise 6.4).

# 7.5 Example. Let 

$$
f_{n}(x)=\frac{\sin n x}{\sqrt{n}} \quad(x \text { real, } n=1,2,3, \ldots)
$$

and

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x)=0
$$

Then $f^{\prime}(x)=0$, and

$$
f_{n}^{\prime}(x)=\sqrt{n} \cos n x
$$

so that $\left(f_{n}^{\prime}\right)$ does not converge to $f^{\prime}$. For instance,

$$
f_{n}^{\prime}(0)=\sqrt{n} \rightarrow+\infty
$$

as $n \rightarrow \infty$, whereas $f^{\prime}(0)=0$.

# 7.6 Example. Let 

$$
f_{n}(x)=n^{2} x\left(1-x^{2}\right)^{n} \quad(0 \leq x \leq 1, n=1,2,3, \ldots)
$$

For $0<x \leq 1$, we have

$$
\lim _{n \rightarrow \infty} f_{n}(x)=0
$$

by Theorem 3.20(d). Since $f_{n}(0)=0$, we see that

$$
\lim _{n \rightarrow \infty} f_{n}(x)=0 \quad(0 \leq x \leq 1)
$$

A simple calculation show that

$$
\int_{0}^{1} x\left(1-x^{2}\right)^{n} d x=\frac{1}{2 n+2}
$$

Thus, in spite of (7.11),

$$
\int_{0}^{1} f_{n}(x) d x=\frac{n^{2}}{2 n+2} \rightarrow+\infty
$$

as $n \rightarrow \infty$.
If, in (7.10), we replace $n^{2}$ by $n$, (7.11) still holds, but we now have

$$
\lim _{n \rightarrow \infty} \int_{0}^{1} f_{n}(x) d x=\lim _{n \rightarrow \infty} \frac{n}{2 n+2}=\frac{1}{2}
$$

whereas

$$
\int_{0}^{1}\left[\lim _{n \rightarrow \infty} f_{n}(x)\right] d x=0
$$

Thus the limit of the integral need not be equal to the integral of the limit, even if both are finite.

After these examples, which show what can go wrong if limit processes are interchanged carelessly, we now define a new mode of convergence, stronger than pointwise convergence as defined in Definition 7.1, which will enable us to arrive at positive results.

## UNIFORM CONVERGENCE

7.7 Definition. We say that a sequence of functions $\left\{f_{n}\right\}, n=1,2,3, \ldots$, converges uniformly on E to a function f if for every $\varepsilon>0$ there is an integer N such that $\mathrm{n} \geq \mathrm{N}$ implies

$$
\left|f_{n}(x)-f(x)\right| \leq \varepsilon
$$

for all $x \in E$.

It is clear that every uniformly convergent sequence is pointwise convergent. Quite explicitly, the difference between the two concepts is this: If $\left(f_{n}\right)$ converges pointwise on $E$, then there exists a function $f$ such that, for every $\varepsilon>0$, and for every $x \in E$, there is an integer $N$, depending on $\varepsilon$ and on $x$, such that (7.12) holds if $n \geq N$; if $\left(f_{n}\right)$ converges uniformly on $E$, it is possible, fr each $\varepsilon>0$ to find one integer $N$ which will do for all $x \in E$.

We say that the series $\Sigma f_{n}(x)$ converges uniformly on $E$ if the sequence $\left(s_{n}\right)$ of partial sums defined by

$$
\sum_{i=1}^{n} f_{i}(x)=s_{n}(x)
$$

converges uniformly on $E$.
The Cauchy criterion for uniform convergence is as follows.
7.8 Theorem. The sequence of functions $\left(f_{n}\right)$, defined on E, converges uniformly on E if and only if for every $\varepsilon>0$ there exists an integer N such that $\mathrm{m} \geq \mathrm{N}, \mathrm{n} \geq \mathrm{N}, \mathrm{x} \in \mathrm{E}$ implies

$$
\left|f_{n}(x)-f_{m}(x)\right| \leq \varepsilon
$$

Proof. Suppose $\left(f_{n}\right)$ converges uniformly on $E$, and let $f$ be the limit function. Then there is an integer $N$ such that $n \geq N, x \in E$ implies

$$
\left|f_{n}(x)-f(x)\right| \leq \frac{\varepsilon}{2}
$$

so that

$$
\left|f_{n}(x)-f_{m}(x)\right| \leq\left|f_{n}(x)-f(x)\right|+\left|f(x)-f_{m}(x)\right| \leq \varepsilon
$$

if $n \geq N, m \geq N, x \in E$.
Conversely, suppose the Cauchy condition holds. By Theorem 3.11, the sequence $\left(f_{n}(x)\right)$ converges, for every $x$, to a limit which we may call $f(x)$. Thus the sequence $\left(f_{n}\right)$ converges on $E$, to $f$. We have to prove that the convergence is uniform.

Let $\varepsilon>0$ be given, and choose $N$ such that (7.13) holds. Fix $n$, and let $m \rightarrow \infty$ in (7.13). Since $f_{m}(x) \rightarrow f(x)$ as $m \rightarrow \infty$, this gives

$$
\left|f_{n}(x)-f(x)\right| \leq \varepsilon
$$

for every $n \geq N$ and every $x \in E$, which completes the proof.
The following criterion is sometimes useful.
7.9 Theorem. Suppose

$$
\lim _{n \rightarrow \infty} f_{n}(x)=f(x) \quad(x \in E)
$$

Put

$$
M_{n}=\sup _{x \in E}\left|f_{n}(x)-f(x)\right|
$$

Then $f_{n} \rightarrow f$ uniformly on $E$ if and only if $M_{n} \rightarrow 0$ as $n \rightarrow \infty$.
Since this is an immediate consequence of Definition 7.7, we omit the details of the proof.

For series, there is a very convenient test for uniform convergence, due to Weierstrass.
7.10 Theorem. Suppose $\left(f_{n}\right)$ is a sequence of functions defined on $E$, and suppose

$$
\left|f_{n}(x)\right| \leq M_{n} \quad(x \in E, n=1,2,3, \ldots)
$$

Then $\Sigma f_{n}$ converges uniformly on $E$ if $\Sigma M_{n}$ converges.
Note that the converse is not asserted (and is, in fact, not true).
Proof. If $\Sigma M_{n}$ converges, then, for arbitrary $\varepsilon>0$,

$$
\left|\sum_{i=1}^{m} f_{i}(x)\right| \leq \sum_{i=n}^{m} M_{i} \leq \varepsilon \quad(x \in E)
$$

provided $m$ and $n$ are large enough. Uniform convergence now follows from Theorem 7.8 .

# UNIFORM CONVERGENCE AND CONTINUITY 

7.11 Theorem. Suppose $f_{n} \rightarrow f$ uniformly on a set $E$ in a metric space. Let $x$ be a limit point of E , and suppose that

$$
\lim _{t \rightarrow x} f_{n}(t)=A_{n} \quad(n=1,2,3, \ldots)
$$

Then $\left(A_{n}\right)$ converges, and

$$
\lim _{t \rightarrow x} f(t)=\lim _{n \rightarrow \infty} A_{n}
$$

In other words, the conclusion is that

$$
\lim _{t \rightarrow x} \lim _{n \rightarrow \infty} f_{n}(t)=\lim _{n \rightarrow \infty} \lim _{t \rightarrow x} f_{n}(t)
$$

Proof. Let $\varepsilon>0$ be given. By the uniform convergence of $\left(f_{n}\right)$, there exists $N$ such that $n \geq N, m \geq N, t \in E$ imply

$$
\left|f_{n}(t)-f_{m}(t)\right| \leq \varepsilon
$$

Letting $t \rightarrow x$ in (7.18), we obtain

$$
\left|A_{n}-A_{m}\right| \leq \varepsilon
$$

for $n \geq N, m \geq N$, so that $\left(A_{n}\right)$ is a Cauchy sequence and therefore converges, say to A.

Next,

$$
|f(t)-A| \leq\left|f(t)-f_{n}(t)\right|+\left|f_{n}(t)-A_{n}\right|+\left|A_{n}-A\right|
$$

We first choose $n$ such that

$$
\left|f(t)-f_{n}(t)\right| \leq \frac{\varepsilon}{3}
$$

for all $t \in E$ (this is possible by uniform convergence), and such that

$$
\left|A_{n}-A\right| \leq \frac{\varepsilon}{3}
$$

Then, for this $n$, we choose a neighborhood $V$ of $x$ such that

$$
\left|f_{n}(t)-A_{n}\right| \leq \frac{\varepsilon}{3}
$$

if $t \in V \cap E, t \neq x$.
Substituting the inequalities (7.20) to (7.22) into (7.19), we see that

$$
|f(t)-A| \leq \varepsilon
$$

provided $t \in V \cap E, t \neq x$. This is equivalent to (7.16).
7.12 Theorem. If $\left(f_{n}\right)$ is a sequence of continuous functions on $E$, and if $f_{n} \rightarrow f$ uniformly on E , then f is is continuous on E .

This very important result is an immediate corollary of Theorem 7.11.
The converse is not true; that is, a sequence of continuous functions may converge to a continuous function, although the convergence is not uniform. Example 7.6 is of this kind (to see this, apply Theorem 7.9). But there is a case in which we can assert the converse.
7.13 Theorem. Suppose K is compact, and
(a) $\left(f_{n}\right)$ is a sequence of continuous functions on $K$,
(b) $\left(f_{n}\right)$ converges pointwise to a continuous function $f$ on $K$,
(c) $f_{n}(x) \geq f_{n+1}(x)$ for all $x \in K, n=1,2,3, \ldots$

Then $f_{n} \rightarrow f$ uniformly on K .

Proof. Put $g_{n}=f_{n}-f$. Then $g_{n}$ is continuous, $g_{n} \rightarrow 0$ pointwise, and $g_{n} \geq g_{n+1}$. We have to prove that $g_{n} \rightarrow 0$ uniformly on $K$.

Let $\varepsilon>0$ be given. Let $K_{n}$ be the set of all $x \in K$ with $g_{n}(x) \geq \varepsilon$. Since $g_{n}$ is continuous, $\mathrm{K}_{n}$ is closed (Theorem 4.8), hence compact (Theorem 2.35). Since $g_{n} \geq g_{n+1}$, we have $K_{n} \supset K_{n+1}$. Fix $x \in K$. Since $g_{n}(x) \rightarrow 0$, we see that $x \notin K_{n}$ if $n$ is sufficiently large. Thus $x \notin \cap K_{n}$. In other words, $\cap K_{n}$ is empty. Hence $K_{N}$ is empty for some N (Theorem 2.36). It follows that $0 \leq g_{n}(x)<\varepsilon$ for all $x \in K$ and for all $n \geq N$. This proves the theorem.

Let us note that compactness is really needed here. For instance if

$$
f_{n}(x)=\frac{1}{n x+1} \quad(0<x<1 ; n=1,2,3, \ldots)
$$

then $f_{n}(x) \rightarrow 0$ monotonically in $(0,1)$, but the convergence is not uniform.
7.14 Definition. If $X$ is a metric space $\mathscr{C}(X)$ will denote the set of all complexvalued, continuous, bounded functions with domain $X$.
[Note that boundedness is redundant if X is compact (Theorem 4.15). Thus $\mathscr{C}(\mathrm{X})$ consists of all complex continuous functions on X if X is compact.]

We associate with each $f \in \mathscr{C}(X)$ its supremum norm

$$
\|f\|=\sup _{x \in X}|f(x)|
$$

Since $f$ is assumed to be bounded, $\|f\|<\infty$. It is obvious that $\|f\|=0$ only if $f(x)=0$ for every $x \in X$, that is, only if $f=0$. If $h=f+g$, then

$$
|h(x)| \leq|f(x)|+|g(x)| \leq\|f\|+\|g\|
$$

for all $x \in X$; hence

$$
\|f+g\| \leq\|f\|+\|g\|
$$

If we define the distance between $f \in \mathscr{C}(X)$ and $g \in \mathscr{C}(X)$ to be $\|f-g\|$, it follows that Axioms 2.15 for a metric are satisfied.

We have thus made $\mathscr{C}(\mathrm{X})$ into a metric space.
Theorem 7.9 can be rephrased as follows:
$A$ sequence $\left(f_{n}\right)$ converges to $f$ with respect to the metric of $\mathscr{C}(X)$ if and only if $f_{n} \rightarrow f$ uniformly on $X$.

Accordingly, closed subsets of $\mathscr{C}(X)$ are sometimes called uniformly closed, the closure of a set $\mathscr{A} \subset \mathscr{C}(\mathrm{X})$ is called its uniform closure, and so on.
7.15 Theorem. The above metric makes $\mathscr{C}(\mathrm{X})$ into a complete metric space.

Proof. Let $\left(f_{n}\right)$ be a Cauchy sequence $\mathscr{C}(X)$. This means that to each $\varepsilon>0$ corresponds an N such that $\left\|f_{n}-f_{m}\right\|<\varepsilon$ if $n \geq N$ and $m \geq N$. It follows (by

Theorem 7.8) that there is a function $f$ with domain $X$ to which $\left(f_{n}\right)$ converges uniformly. By Theorem 7.12, $f$ is continuous. Moreover, $f$ is bounded, since there is an $n$ such that $\left|f(x)-f_{n}(x)\right|<1$ for all $x \in X$, and $f_{n}$ is bounded.

Thus $f \in \mathscr{C}(X)$, and since $f_{n} \rightarrow f$ uniformly on $X$, we have $\left\|f-f_{n}\right\| \rightarrow 0$ as $n \rightarrow \infty$.

# UNIFORM CONVERGENCE AND INTEGRATION 

7.16 Theorem. Let $\alpha$ be monotonically increasing on [a,b]. Suppose $f_{n} \in \mathscr{R}(\alpha)$ on $[a, b]$, for $n=1,2,3, \ldots$, and suppose $f_{n} \rightarrow f$ uniformly on $[a, b]$. Then $f \in \mathscr{R}(\alpha)$ on $[a, b]$, and

$$
\int_{a}^{b} f d \alpha=\lim _{n \rightarrow \infty} \int_{a}^{b} f_{n} d \alpha
$$

(The existence of the limit is part of the conclusion.)
Proof. It suffices to prove this for real $f_{n}$. Put

$$
\varepsilon_{n}=\sup \left|f_{n}(x)-f(x)\right|
$$

the supremum being taken over $a \leq x \leq b$. Then

$$
f_{n}-\varepsilon_{n} \leq f \leq f_{n}+\varepsilon_{n}
$$

so that the upper and lower integrals of $f$ (see Definition 6.2) satisfy

$$
\int_{a}^{b}\left(f_{n}-\varepsilon_{n}\right) d \alpha \leq \int f d \alpha \leq \int f d \alpha \leq \int_{a}^{b}\left(f_{n}+\varepsilon_{n}\right) d \alpha
$$

Hence

$$
0 \leq \int f d \alpha-\int f d \alpha \leq 2 \varepsilon_{n}[\alpha(b)-\alpha(a)]
$$

Since $\varepsilon_{n} \rightarrow 0$ as $n \rightarrow \infty$ (Theorem 7.9), the upper and lower integrals of $f$ are equal.

Thus $f \in \mathscr{R}(\alpha)$. Another application of (7.25) now yields

$$
\left|\int_{a}^{b} f d \alpha-\int_{a}^{b} f_{n} d \alpha\right| \leq \varepsilon_{n}[\alpha(b)-\alpha(a)]
$$

Thus implies (7.23).
Corollary. If $f_{n} \in \mathscr{R}(\alpha)$ on $[a, b]$ and if

$$
f(x)=\sum_{n=1}^{\infty} f_{n}(x) \quad(a \leq x \leq b)
$$

the series converging uniformly on $[a, b]$, then

$$
\int_{a}^{b} f d \alpha=\sum_{n=1}^{\infty} \int_{a}^{b} f_{n} d \alpha
$$

In other words the series may be integrated term by term.

# UNIFORM CONVERGENCE AND DIFFERENTIATION 

We have already seen, in Example 7.5, that uniform convergence of $\left(f_{n}\right)$ implies nothing about the sequence $\left(f_{n}^{\prime}\right)$. Thus stronger hypotheses are required for the assertion that $f_{n}^{\prime} \rightarrow f^{\prime}$ if $f_{n} \rightarrow f$.
7.17 Theorem. Suppose $\left(f_{n}\right)$ is a sequence of functions, differentiable on $[a, b]$ and such that $\left(f_{n}\left(x_{0}\right)\right)$ converges for some point $x_{0}$ on $[a, b]$. If $\left(f_{n}^{\prime}\right)$ converges uniformly on $[a, b]$, then $\left(f_{n}\right)$ converges uniformly on $[a, b]$, to a function $f$, and

$$
f^{\prime}(x)=\lim _{n \rightarrow \infty} f_{n}^{\prime}(x) \quad(a \leq x \leq b)
$$

Proof. Let $\varepsilon>0$ be given. Choose N such that $\mathrm{n} \geq \mathrm{N}, \mathrm{m} \leq \mathrm{N}$, implies

$$
\left|f_{n}\left(x_{0}\right)-f_{m}\left(x_{0}\right)\right|<\frac{\varepsilon}{2}
$$

and

$$
\left|f_{n}^{\prime}(t)-f_{m}^{\prime}(t)\right|<\frac{\varepsilon}{2(b-a)} \quad(a \leq t \leq b)
$$

If we apply the mean value theorem 5.19 to the function $f_{n}-f_{m}$, (7.29) shows that

$$
\left|f_{n}(x)-f_{m}(x)-f_{n}(t)+f_{m}(t)\right| \leq \frac{|x-t| \varepsilon}{2(b-a)} \leq \frac{\varepsilon}{2}
$$

for any $x$ and $t$ on $[a, b]$, if $n \geq N, m \geq N$. The inequality

$$
\left|f_{n}(x)-f_{m}(x)\right| \leq\left|f_{n}(x)-f_{m}(x)-f_{n}\left(x_{0}\right)+f_{m}\left(x_{0}\right)\right|+\left|f_{n}\left(x_{0}\right)-f_{m}\left(x_{0}\right)\right|
$$

implies, by (7.28) and (7.30), that

$$
\left|f_{n}(x)-f_{m}(x)\right|<\varepsilon \quad(a \leq x \leq b, n \geq N, m \geq N)
$$

so that $\left(f_{n}\right)$ converges uniformly on $[a, b]$. Let

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x) \quad(a \leq x \leq b)
$$

Let us now fix a point $x$ on $[a, b]$ and define

$$
\phi_{n}(t)=\frac{f_{n}(t)-f_{n}(x)}{t-x}, \quad \phi(t)=\frac{f(t)-f(x)}{t-x}
$$

for $a \leq t \leq b, t \neq x$. Then

$$
\lim _{t \rightarrow x} \phi_{n}(t)=f_{n}^{\prime}(x) \quad(n=1,2,3, \ldots)
$$

The first inequality in (7.30) shows that

$$
\left|\phi_{n}(t)-\phi_{m}(t)\right| \leq \frac{\varepsilon}{2(b-a)} \quad(n \geq N, m \geq N)
$$

so that $\left(\phi_{n}\right)$ converges uniformly, for $t \neq x$. Since $\left(f_{n}\right)$ converges to $f$, we conclude from (7.31) that

$$
\lim _{n \rightarrow \infty} \phi_{n}(t)=\phi(t)
$$

uniformly for $a \leq t \leq b, t \neq x$.
If we now apply Theorem 7.11 to $\left(\phi_{n}\right)$, (7.32) and (7.33) show that

$$
\lim _{t \rightarrow x} \phi(t)=\lim _{n \rightarrow \infty} f_{n}^{\prime}(x)
$$

and this is (7.27), by definition of $\phi(t)$.
Remark: If the continuity of the functions $f_{n}^{\prime}$ is assumed in addition to the above hypotheses, then a much shorter proof of (7.27) can be based on Theorem 7.16 and the fundamental theorem of calculus.
7.18 Theorem. There exists a real continuous function on the real line which is nowhere differentiable.

Proof. Define

$$
\varphi(x)=|x| \quad(-1 \leq x \leq 1)
$$

and extend the definition of $\varphi(x)$ to all real $x$ by requiring that

$$
\varphi(x+2)=\varphi(x)
$$

Then, for all $s$ and $t$,

$$
|\varphi(s)-\varphi(t)| \leq|s-t|
$$

In particular, $\varphi$ is continuous on $\mathbb{R}^{1}$. Define

$$
f(x)=\sum_{n=0}^{\infty}\left(\frac{3}{4}\right)^{n} \varphi\left(4^{n} x\right)
$$

Since $0 \leq \varphi \leq 1$, Theorem 7.10 shows that the series (7.37) converges uniformly on $\mathbb{R}^{1}$. By Theorem $7.12, \mathrm{f}$ is continuous on $\mathbb{R}^{1}$.

Now fix a real number $x$ and a positive integer $m$. Put

$$
\delta_{m}= \pm \frac{1}{2} \cdot 4^{-m}
$$

where the sign is so chosen that no integer lies between $4^{m} x$ and $4^{m}\left(x+\delta_{m}\right)$. This can be done, since $4^{m}\left|\delta_{m}\right|=1 / 2$. Define

$$
\gamma_{n}=\frac{\varphi\left(4^{n}\left(x+\delta_{m}\right)\right)-\varphi\left(4^{n} x\right)}{\delta_{m}}
$$

When $n>m$, then $4^{n} \delta_{m}$ is an even integer, so that $\gamma_{n}=0$. When $0 \leq n \leq m$, (7.36) implies that $\left|\gamma_{n}\right| \leq 4^{n}$.

Since $\left|\gamma_{m}\right|=4^{m}$, we conclude that

$$
\begin{aligned}
\left|\frac{f\left(x+\delta_{m}\right)-f(x)}{\delta_{m}}\right| & =\left|\sum_{n=0}^{m}\left(\frac{3}{4}\right)^{n} \gamma_{n}\right| \\
& \geq 3^{m}-\sum_{n=0}^{m-1} 3^{n} \\
& =\frac{1}{2}\left(3^{m}+1\right)
\end{aligned}
$$

As $m \rightarrow \infty, \delta_{m} \rightarrow 0$. It follows that $f$ is not differentiable at $x$.

# EQUICONTINUOUS FAMILIES OF FUNCTIONS 

In Theorem 3.6 we saw that every bounded sequence of complex numbers contains a convergent subsequence, and the question arises whether something similar is true for sequences of functions. To make the question more precise, we shall define two kinds of boundedness.
7.19 Definition. Let $\left(f_{n}\right)$ be a sequence of functions defined on a set $E$.

We say that $\left(f_{n}\right)$ is pointwise bounded on $E$ if the sequence $\left(f_{n}(x)\right)$ is bounded for every $x \in E$, that is, if there exists a finite-valued function $\phi$ defined on $E$ such that

$$
\left|f_{n}(x)\right|<\phi(x) \quad(x \in E, n=1,2,3, \ldots)
$$

We say that $\left(f_{n}\right)$ is uniformly bounded on $E$ if there exists a number $M$ such that

$$
\left|f_{n}(x)\right|<M \quad(x \in E, n=1,2,3, \ldots)
$$

Now if $\left(f_{n}\right)$ is pointwise bounded on $E$ and $E_{1}$ is a countable subset of $E$, it is always possible to find a subsequence $\left(f_{n_{k}}\right)$ such that $\left(f_{n_{k}}(x)\right)$ converges for

every $x \in E_{1}$. This can be done by the diagonal process which is used in the proof of Theorem 7.23.

However, even if $\left(f_{n}\right)$ is a uniformly bounded sequence of continuous functions on a compact set $E$, there need not exist a subsequence which converges pointwise on E. In the following example, this would be quite troublesome to prove with the equipment which we have at hand so far, but the proof is simple if we appeal to a theorem from Chap. 11.
7.20 Example. Let

$$
f_{n}(x)=\sin n x \quad(0 \leq x \leq 2 \pi, n=1,2,3, \ldots)
$$

Suppose there exists a sequence $\left(n_{k}\right)$ such that $\left(\sin n_{k} x\right)$ converges, for every $x \in$ $[0,2 \pi]$. In that case we must have

$$
\lim _{k \rightarrow \infty}\left(\sin n_{k} x-\sin n_{k+1} x\right)=0 \quad(0 \leq x \leq 2 \pi)
$$

hence

$$
\lim _{k \rightarrow \infty}\left(\sin n_{k} x-\sin n_{k+1} x\right)^{2}=0 \quad(0 \leq x \leq 2 \pi)
$$

By Lebesgue's theorem concerning integration of boundedly convergent sequences (Theorem 11.32), (7.40) implies

$$
\lim _{k \rightarrow \infty} \int_{0}^{2 \pi}\left(\sin n_{k} x-\sin n_{k+1} x\right)^{2} d x=0
$$

But a simple calculation shows that

$$
\int_{0}^{2 \pi}\left(\sin n_{k} x-\sin n_{k+1} x\right)^{2} d x=2 \pi
$$

which contradicts (7.41).
Another question is whether every convergent sequence contains a uniformly convergent subsequence. Our next example will show that this need not be so, even if the sequence is uniformly bounded on a compact set. (Example 7.6 shows that a sequence of bounded functions may converge without being uniformly bounded; but it is trivial to see that uniform convergence of a sequence of bounded functions implies uniform boundedness.)
7.21 Example. Let

$$
f_{n}(x)=\frac{x^{2}}{x^{2}+(1-n x)^{2}} \quad(0 \leq x \leq 1, n=1,2,3, \ldots)
$$

Then $\left|f_{n}(x)\right| \leq 1$, so that $\left(f_{n}\right)$ is uniformly bounded on $[0,1]$. Also

$$
\lim _{n \rightarrow \infty} f_{n}(x)=0 \quad(0 \leq x \leq 1)
$$

but

$$
f_{n}\left(\frac{1}{n}\right)=1 \quad(n=1,2,3, \ldots)
$$

so that no subsequence can converge uniformly on $[0,1]$.
The concept which is needed in this connection is that of equicontinuity; it is given in the following definition.
7.22 Definition. A family $\mathscr{F}$ of complex functions $f$ defined on a set $E$ in a metric space $X$ is said to be equicontinuous on $E$ if for every $\varepsilon>0$ there exists $\delta>0$ such that

$$
|f(x)-f(y)|<\varepsilon
$$

whenever $d(x, y)<\delta, x \in E, y \in E$, and $f \in \mathscr{F}$. Here $d$ denotes the metric of $X$.
It is clear that every member of an equicontinuous family is uniformly continuous.

The sequence of Example 7.21 is not equicontinuous.
Theorems 7.24 and 7.25 will show that there is a very close relation between equicontinuity, on the one hand, and uniform convergence of sequences of continuous functions, on the other. But first we describe a selection process which has nothing to do with continuity.
7.23 Theorem. If $\left(f_{n}\right)$ is a pointwise bounded sequence of complex functions on a countable set E , then $\left(f_{n}\right)$ has a subsequence $\left(f_{n_{k}}\right)$ such that $\left(f_{n_{k}}(x)\right)$ converges for every $x \in E$.

Proof. Let $\left(x_{i}\right), i=1,2,3, \ldots$, be the points of $E$, arranged in a sequence. Since $\left(f_{n}\left(x_{1}\right)\right)$ is bounded, there exists a subsequence, which we shall denote by $\left(f_{1, k}\right)$, such that $\left(f_{1, k}\left(x_{1}\right)\right)$ converges as $k \rightarrow \infty$.

Let us now consider sequences $S_{1}, S_{2}, S_{3}, \ldots$, which we represent by the array

| $S_{1}:$ | $f_{1,1}$ | $f_{1,2}$ | $f_{1,3}$ | $f_{1,4}$ | $\ldots$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $S_{2}:$ | $f_{2,1}$ | $f_{2,2}$ | $f_{2,3}$ | $f_{2,4}$ | $\ldots$ |
| $S_{3}:$ | $f_{3,1}$ | $f_{3,2}$ | $f_{3,3}$ | $f_{3,4}$ | $\ldots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

and which have the following properties:
(a) $S_{n}$ is a subsequence of $S_{n-1}$, for $n=2,3,4, \ldots$
(b) $\left(f_{n, k}\left(x_{n}\right)\right)$ converges, as $k \rightarrow \infty$ (the boundedness of $\left(f_{n}\left(x_{n}\right)\right)$ makes it possible to choose $S_{n}$ in this way);

(c) The order in which the functions appear is the same in each sequence; i.e., if one function precedes another in $S_{1}$, they are in the same relation in every $S_{n}$, until one or the other is deleted. Hence, when going from one row in the above array to the next below, functions may move to the left but never to the right.

We now go down the diagonal of the array; i.e., we consider the sequence

$$
S: \quad f_{1,1} \quad f_{2,2} \quad f_{3,3} \quad f_{4,4} \quad \cdots
$$

By (c), the sequence $S$ (except possible its first $n-1$ terms) is a subsequence of $S_{n}$, for $n=1,2,3, \ldots$ Hence (b) implies that $\left(f_{n, n}\left(x_{i}\right)\right)$ converges, as $n \rightarrow \infty$, for every $x_{i} \in E$.
7.24 Theorem. If K is a compact metric space, if $\mathrm{f}_{\mathrm{n}} \in \mathscr{C}(\mathrm{K})$ for $\mathrm{n}=1,2,3, \ldots$, and if $\left(f_{n}\right)$ converges uniformly on K , then $\left(f_{n}\right)$ is equicontinuous on K .

Proof. Let $\varepsilon>0$ be given. Since $\left(f_{n}\right)$ converges uniformly, there is an integer $N$ such that

$$
\left\|f_{n}-f_{N}\right\|<\varepsilon \quad(n>N)
$$

(See Definition 7.14.) Since continuous functions are uniformly continuous on compact sets, there is a $\delta>0$ such that

$$
\left|f_{i}(x)-f_{i}(y)\right|<\varepsilon
$$

if $1 \leq \mathrm{i} \leq \mathrm{N}$ and $\mathrm{d}(\mathrm{x}, \mathrm{y})<\delta$.
If $\mathrm{n}>\mathrm{N}$ and $\mathrm{d}(\mathrm{x}, \mathrm{y})<\delta$, it follows that

$$
\left|f_{n}(x)-f_{n}(y)\right| \leq\left|f_{n}(x)-f_{N}(x)\right|+\left|f_{N}(x)-f_{N}(y)\right|+\left|f_{N}(y)-f_{n}(y)\right|<3 \varepsilon
$$

In conjunction with (7.43), this proves the theorem.
7.25 Theorem. If K is compact, if $\mathrm{f}_{\mathrm{n}} \in \mathscr{C}(\mathrm{K})$ for $\mathrm{n}=1,2,3 \ldots$, and if $\left(\mathrm{f}_{\mathrm{n}}\right)$ is pointwise bounded and equicontinuous on K , then
(a) $\left(f_{n}\right)$ is uniformly bounded on $K$,
(b) $\left(f_{n}\right)$ contains a uniformly convergent subsequence.

Proof.
(a) Let $\varepsilon>0$ be given and choose $\delta>0$, in accordance with Definition 7.22, so that

$$
\left|f_{n}(x)-f_{n}(y)\right|<\varepsilon
$$

for all n , provided that $\mathrm{d}(\mathrm{x}, \mathrm{y})<\delta$.

Since K is compact, there are finitely many points $\mathrm{p}_{1}, \ldots, \mathrm{p}_{\mathrm{r}}$ in K such that to every $x \in K$ corresponds at least one $p_{i}$ with $d\left(x, p_{i}\right)<\delta$. Since $\left(f_{n}\right)$ is pointwise bounded, there exists $M_{i}<\infty$ such that $\left|f_{n}\left(p_{i}\right)\right|<M_{i}$ for all $n$. If $M=\max \left(M_{1}, \ldots, M_{r}\right)$, then $\left|f_{n}(x)\right|<M+\varepsilon$ for every $x \in K$. This proves (a).
(b) Let E be a countable dense subset of K. (For the existence of such a set E, see Exercise 2.25.) Theorem 7.23 shows that $\left(f_{n}\right)$ has a subsequence $\left(f_{n_{i}}\right)$ such that $\left(f_{n_{i}}(x)\right)$ converges for every $x \in E$.

Put $f_{n_{i}}=g_{i}$, to simplify the notation. We shall prove that $\left(g_{i}\right)$ converges uniformly on K .

Let $\varepsilon>0$, and pick $\delta>0$ as in the beginning of this proof. Let $V(x, \delta)$ be the set of all $y \in K$ with $d(x, y)<\delta$. Since $E$ is dense in $K$ and $K$ is compact, there are finitely many points $x_{1}, \ldots, x_{m}$ in $E$ such that

$$
K \subset V\left(x_{1}, \delta\right) \cup \cdots \cup V\left(x_{m}, \delta\right)
$$

Since $\left(g_{i}(x)\right)$ converges for every $x \in E$, there is an integer $N$ such that

$$
\left|g_{i}\left(x_{s}\right)-g_{j}\left(x_{s}\right)\right|<\varepsilon
$$

whenever $i \geq N, j \geq N, 1 \leq s \leq m$.
If $x \in K,(7.45)$ shows that $x \in V\left(x_{s}, \delta\right)$ for some $s$, so that

$$
\left|g_{i}(x)-g_{i}\left(x_{s}\right)\right|<\varepsilon
$$

for every $i$. If $i \geq N$ and $j \geq N$, it follows from (7.46) that

$$
\begin{aligned}
\left|g_{i}(x)-g_{j}(x)\right| & \leq\left|g_{i}(x)-g_{i}\left(x_{s}\right)\right|+\left|g_{i}\left(x_{s}\right)-g_{j}\left(x_{s}\right)\right|+\left|g_{j}\left(x_{s}\right)-g_{j}(x)\right| \\
& <3 \varepsilon
\end{aligned}
$$

This completes the proof.

# THE STONE-WEIERSTRASS THEOREM 

7.26 Theorem. If f is a continuous complex function on [a,b], there exists a sequence of polynomials $\mathrm{P}_{\mathrm{n}}$ such that

$$
\lim _{n \rightarrow \infty} P_{n}(x)=f(x)
$$

uniformly on $[a, b]$. If $f$ is real, then $P_{n}$ may be taken real.
This is the form in which the theorem was originally discovered by Weierstrass.
Proof. We may assume, without loss of generality, that $[a, b]=[0,1]$. We may also assume that $f(0)=f(1)=0$. For if the theorem is proved for this case, consider

$$
g(x)=f(x)-f(0)-x[f(1)-f(0)] \quad(0 \leq x \leq 1)
$$

Here $g(0)=g(1)=0$, and if $g$ can be obtained as the limit of a uniformly convergent sequence of polynomials, it is clear that the same is true for $f$, since $f-g$ is a polynomial.

Furthermore, we define $f(x)$ to be zero for $x$ outside $[0,1]$. Then $f$ is uniformly continuous on the whole line.

We put

$$
\mathrm{Q}_{n}(\mathrm{x})=\mathrm{c}_{n}\left(1-\mathrm{x}^{2}\right)^{n} \quad(n=1,2,3, \ldots)
$$

where $c_{n}$ is chosen so that

$$
\int_{-1}^{1} Q_{n}(x) d x=1 \quad(n=1,2,3, \ldots)
$$

We need some information about the order of magnitude of $c_{n}$. Since

$$
\begin{aligned}
\int_{-1}^{1}\left(1-x^{2}\right)^{n} d x=2 \int_{0}^{1}\left(1-x^{2}\right)^{n} d x & \geq 2 \int_{0}^{1 / \sqrt{n}}\left(1-x^{2}\right)^{n} d x \\
& \geq 2 \int_{0}^{1 / \sqrt{n}}\left(1-n x^{2}\right) d x \\
& =\frac{4}{3 \sqrt{n}} \\
& >\frac{1}{\sqrt{n}}
\end{aligned}
$$

it follows from (7.48) that

$$
c_{n}<\sqrt{n}
$$

The inequality $\left(1-x^{2}\right)^{n} \geq 1-n x^{2}$ which we used above is easily shown to be true by considering the function

$$
\left(1-x^{2}\right)^{n}-1+n x^{2}
$$

which is zero at $x=0$ an whose derivative is positive in $(0,1)$.
For any $\delta>0,(7.49)$ implies

$$
\mathrm{Q}_{n}(\mathrm{x}) \leq \sqrt{n}\left(1-\delta^{2}\right)^{n} \quad(\delta \leq|\mathrm{x}| \leq 1)
$$

so that $Q_{n} \rightarrow 0$ uniformly in $\delta \leq|x| \leq 1$.
Now set

$$
P_{n}(x)=\int_{-1}^{1} f(x+t) Q_{n}(t) d t \quad(0 \leq x \leq 1)
$$

Our assumptions about $f$ show, by a simple change of variable, that

$$
P_{n}(x)=\int_{-x}^{1-x} f(x+t) Q_{n}(t) d t=\int_{0}^{1} f(t) Q_{n}(t-x) d t
$$

and the last integral is clearly a polynomial in $x$. Thus $\left(P_{n}\right)$ is a sequence of polynomials, which are real if $f$ is real.

Given $\varepsilon>0$, we choose $\delta>0$ such that $|y-x|<\delta$ implies

$$
|f(y)-f(x)|<\frac{\varepsilon}{2}
$$

Let $M=\sup |f(x)|$. Using (7.48), (7.50), and the fact that $Q_{n}(x) \geq 0$, we see that for $0 \leq x \leq 1$,

$$
\begin{aligned}
\left|P_{n}(x)-f(x)\right| & =\left|\int_{-1}^{1}[f(x+t)-f(x)] Q_{n}(t) d t\right| \\
& \leq \int_{-1}^{1}|f(x+t)-f(x)| Q_{n}(t) d t \\
& \leq 2 M \int_{-1}^{-\delta} Q_{n}(t) d t+\frac{\varepsilon}{2} \int_{-\delta}^{\delta} Q_{n}(t) d t+2 M \int_{\delta}^{1} Q_{n}(t) d t \\
& \leq 4 M \sqrt{n}\left(1-\delta^{2}\right)^{n}+\frac{\varepsilon}{2} \\
& <\varepsilon
\end{aligned}
$$

for all large enough $n$, which proves the theorem.
It is instructive to sketch the graphs of $Q_{n}$ for a few values of $n$; also, note that we needed uniform continuity of $f$ to deduce uniform convergence of $\left(P_{n}\right)$.

In the proof of Theorem 7.32 we shall not need the full strength of Theorem 7.26, but only the following special case, which we state as a corollary.
7.27 Corollary. For every interval $[-\mathrm{a}, \mathrm{a}]$ there is a sequence of real polynomials $\mathrm{P}_{\mathrm{n}}$ such that $\mathrm{P}_{\mathrm{n}}(0)=0$ and such that

$$
\lim _{n \rightarrow \infty} P_{n}(x)=|x|
$$

uniformly on $[-\mathrm{a}, \mathrm{a}]$.
Proof. By Theorem 7.26, there exists a sequence $\left(\mathrm{P}_{\mathrm{n}}^{*}\right)$ of real polynomials which converges to $|x|$ uniformly on $[-\mathrm{a}, \mathrm{a}]$. In particular, $\mathrm{P}_{\mathrm{n}}^{*}(0) \rightarrow 0$ as $\mathrm{n} \rightarrow \infty$. The polynomials

$$
P_{n}(x)=P_{n}^{*}(x)-P_{n}^{*}(0) \quad(n=1,2,3, \ldots)
$$

have desired properties.
We shall now isolate those properties of the polynomials which make the Weierstrass theorem possible.

7.28 Definition. A family $\mathscr{A}$ of complex functions defined on a set E is said to be an algebra if (i) $f+g \in \mathscr{A}$, (ii) $f g \in \mathscr{A}$, and (iii) $c f \in \mathscr{A}$ for all $f \in \mathscr{A}, g \in \mathscr{A}$ and all complex constants c , that is, if $\mathscr{A}$ is closed under addition, multiplication, and scalar multiplication. We shall also have to consider algebras of real functions; in this case, (iii) is of course only required to hold for all real c .

If $\mathscr{A}$ has the property that $f \in \mathscr{A}$ whenever $f_{n} \in \mathscr{A}(n=1,2,3, \ldots)$ and $f_{n} \rightarrow f$ uniformly on $E$, then $\mathscr{A}$ is said to be uniformly closed.

Let $\mathscr{B}$ be the set of all functions which are limits of uniformly convergent sequence of members of $\mathscr{A}$. Then $\mathscr{B}$ is called the uniform closure of $\mathscr{A}$. (See Definition 7.14.)

For example, the set of all polynomials is an algebra, and the Weierstrass theorem may be stated by saying that the set of continuous functions on $[a, b]$ is the uniform closure of the set of polynomials on $[a, b]$.
7.29 Theorem. Let $\mathscr{B}$ be the uniform closure of an algebra $\mathscr{A}$ of bounded functions. Then $\mathscr{B}$ is a uniformly closed algebra.

Proof. If $f \in \mathscr{B}$ and $g \in \mathscr{B}$, there exist uniformly convergent sequences $\left\{f_{n}\right\},\left\{g_{n}\right\}$ such that $f_{n} \rightarrow f, g_{n} \rightarrow g$ and $f_{n} \in \mathscr{A}, g_{n} \in \mathscr{A}$. Since we are dealing with bounded functions, it is easy to show that

$$
f_{n}+g_{n} \rightarrow f+g, \quad f_{n} g_{n} \rightarrow f g, \quad c f_{n} \rightarrow c f
$$

where c is any constant, the convergence being uniform in each case. Hence $f+g \in \mathscr{B}, f g \in \mathscr{B}$, and $c f \in \mathscr{B}$, so that $\mathscr{B}$ is an algebra. By Theorem 2.27, $\mathscr{B}$ is (uniformly) closed.
7.30 Definition. Let $\mathscr{A}$ be a family of functions on a set E . Then $\mathscr{A}$ is said to separate points on $E$ if to every pair of distinct points $x_{1}, x_{2} \in E$ there corresponds a function $f \in \mathscr{A}$ such that $f\left(x_{1}\right) \neq f\left(x_{2}\right)$.

If to each $x \in E$ there corresponds a function $g \in \mathscr{A}$ such that $g(x) \neq 0$, we say that $\mathscr{A}$ vanishes at no point of E .

The algebra of all polynomials in one variable clearly has these properties on $\mathbb{R}^{1}$. An example of an algebra which does not separate points is the set of all even polynomials, say on $[-1,1]$, since $f(-x)=f(x)$ for every even function $f$.

The following theorem will illustrate these concepts further.
7.31 Theorem. Suppose $\mathscr{A}$ is an algebra of functions on a set $\mathrm{E}, \mathscr{A}$ separates points on E , and $\mathscr{A}$ vanishes at no point of E . Suppose $\mathrm{x}_{1}, \mathrm{x}_{2}$ are distinct points of E , and $\mathrm{c}_{1}, \mathrm{c}_{2}$ are constants (real if $\mathscr{A}$ is a real algebra). Then $\mathscr{A}$ contains a function f such that

$$
f\left(x_{1}\right)=c_{1}, \quad f\left(x_{2}\right)=c_{2}
$$

Proof. The assumptions show that $\mathscr{A}$ contains functions $\mathrm{g}, \mathrm{h}$, and k such that

$$
g\left(x_{1}\right) \neq g\left(x_{2}\right), \quad h\left(x_{1}\right) \neq 0, \quad k\left(x_{2}\right) \neq 0
$$

Put

$$
u=g k-g\left(x_{1}\right) k, \quad v=g h-g\left(x_{2}\right) h
$$

Then $u \in \mathscr{A}, v \in \mathscr{A}, u\left(x_{1}\right)=v\left(x_{2}\right)=0, u\left(x_{2}\right) \neq 0$, and $v\left(x_{1}\right) \neq 0$. Therefore

$$
f=\frac{c_{1} v}{v\left(x_{1}\right)}+\frac{c_{2} u}{u\left(x_{2}\right)}
$$

has the desired properties.
We now have all the material needed for Stone's generalization of the Weierstrass theorem.
7.32 Theorem. Let $\mathscr{A}$ be an algebra of real continuous functions on a compact set K . If $\mathscr{A}$ separates points on K and if $\mathscr{A}$ vanishes at no point of K , then the uniform closure $\mathscr{B}$ of $\mathscr{A}$ consists of all real continuous functions on K .

We shall divide the proof into four steps.
STEP 1 If $\mathrm{f} \in \mathscr{B}$, then $|\mathrm{f}| \in \mathscr{B}$.
Proof. Let

$$
a=\sup |f(x)| \quad(x \in K)
$$

and let $\varepsilon>0$ be given. By Corollary 7.27 there exist real numbers $c_{1}, \ldots, c_{n}$ such that

$$
\left|\sum_{i=1}^{n} c_{i} y^{i}-|y|\right|<\varepsilon \quad(-\alpha \leq y \leq \alpha)
$$

Since $\mathscr{B}$ is an algebra, the function

$$
g=\sum_{i=1}^{n} c_{i} f^{i}
$$

is a member of $\mathscr{B}$. By (7.52) and (7.53), we have

$$
|g(x)-|f(x)||<\varepsilon \quad(x \in K)
$$

Since $\mathscr{B}$ is uniformly closed, this shows that $|f| \in \mathscr{B}$.
STEP 2 If $\mathrm{f} \in \mathscr{B}$ and $\mathrm{g} \in \mathscr{B}$, then $\max (\mathrm{f}, \mathrm{g}) \in \mathscr{B}$ and $\min (\mathrm{f}, \mathrm{g}) \in \mathscr{B}$.
By $\max (\mathrm{f}, \mathrm{g})$ we mean the function h defined by

$$
h(x)= \begin{cases}f(x) & \text { if } f(x) \geq g(x) \\ g(x) & \text { if } f(x)<g(x)\end{cases}
$$

and $\min (\mathrm{f}, \mathrm{g})$ is defined likewise.

Proof. Step 2 follows from step 1 and identities

$$
\begin{aligned}
& \max (f, g)=\frac{f+g}{2}+\frac{|f-g|}{2} \\
& \min (f, g)=\frac{f+g}{2}-\frac{|f-g|}{2}
\end{aligned}
$$

By iteration, the result can of course be extended to any finite set of functions: If $f_{1}, \ldots, f_{n} \in \mathscr{B}$, then $\max \left(f_{1}, \ldots, f_{n}\right) \in \mathscr{B}$ and $\min \left(f_{1}, \ldots, f_{n}\right) \in \mathscr{B}$.
STEP 3 Given a real function f , continuous on K , a point $\mathrm{x} \in \mathrm{K}$, and $\varepsilon>0$, there exists a function $\mathrm{g}_{\mathrm{x}} \in \mathscr{B}$ such that $\mathrm{g}_{\mathrm{x}}(\mathrm{x})=\mathrm{f}(\mathrm{x})$ and

$$
g_{x}(t)>f(t)-\varepsilon \quad(t \in K)
$$

Proof. Since $\mathscr{A} \subset \mathscr{B}$ and $\mathscr{A}$ satisfies the hypotheses of Theorem 7.31 so does $\mathscr{B}$. Hence, for every $y \in K$, we can find a function $h_{y} \in \mathscr{B}$ such that

$$
h_{y}(x)=f(x), \quad h_{y}(y)=f(y)
$$

By the continuity of $h_{y}$ there exists an open set $J_{y}$, containing $y$, such that

$$
h_{y}(t)>f(t)-\varepsilon \quad\left(t \in J_{y}\right)
$$

Since K is compact, there is a finite set of points $y_{1}, \ldots, y_{n}$ such that

$$
K \subset J_{y_{1}} \cup \cdots \cup J_{y_{n}}
$$

Put

$$
g_{x}=\max \left(h_{y_{1}}, \ldots, h_{y_{n}}\right)
$$

By step $2, g_{x} \in \mathscr{B}$, and the relations (7.55) to (7.57) show that $g_{x}$ has the other required properties.

STEP 4 Given a real function f , continuous on K , and $\varepsilon>0$, there exists a function $\mathrm{h} \in \mathscr{B}$ such that

$$
|h(x)-f(x)|<\varepsilon \quad(x \in K)
$$

Since $\mathscr{B}$ is uniformly closed, this statement is equivalent to the conclusion of the theorem.

Proof. Let us consider the functions $g_{x}$, for each $x \in K$ constructed in step 3. By the continuity of $g_{x}$, there exist open sets $V_{x}$ containing $x$, such that

$$
g_{x}(t)<f(t)+\varepsilon \quad\left(t \in V_{x}\right)
$$

Since K is compact, there exists a finite set of points $\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{m}}$ such that

$$
K \subset V_{x_{1}} \cup \cdots \cup V_{x_{m}}
$$

Put

$$
\mathrm{h}=\min \left(\mathrm{g}_{\mathrm{x}_{1}}, \ldots, \mathrm{~g}_{\mathrm{x}_{m}}\right)
$$

By step $2, \mathrm{~h} \in \mathscr{B}$, and (7.54) implies

$$
h(t)>f(t)-\varepsilon \quad(t \in K)
$$

whereas (7.59) and (7.60) imply

$$
h(t)<f(t)+\varepsilon \quad(t \in K)
$$

Finally, (7.58) follows from (7.61) and (7.62).
Theorem 7.32 does not hold for complex algebras. A counterexample is given in Exercise 7.21. However, the conclusion of the theorem does hold, even for complex algebras, if an extra condition is imposed on $\mathscr{A}$, namely, that $\mathscr{A}$ be self-adjoint. This means that for every $\mathrm{f} \in \mathscr{A}$ its complex conjugate $\overline{\mathrm{f}}$ also belong to $\mathscr{A} ; \overline{\mathrm{f}}$ is defined by $\overline{\mathrm{f}}(\mathrm{x})=\overline{\mathrm{f}(\mathrm{x})}$.
7.33 Theorem. Suppose $\mathscr{A}$ is a self-adjoint algebra of complex continuous functions on a compact set $\mathrm{K}, \mathscr{A}$ separates points on K , and $\mathscr{A}$ vanishes at no point of K . Then the uniform closure $\mathscr{B}$ of $\mathscr{A}$ consists of all complex continuous functions on K . In other words, $\mathscr{A}$ is dense $\mathscr{C}(\mathrm{K})$.

Proof. Let $\mathscr{A}_{\mathbb{R}}$ be the set of all real functions on K which belong to $\mathscr{A}$.
If $\mathrm{f} \in \mathscr{A}$ and $\mathrm{f}=\mathrm{u}+\mathrm{iv}$ with $\mathrm{u}, \mathrm{v}$ real, then $2 \mathrm{u}=\mathrm{f}+\overline{\mathrm{f}}$ and, since $\mathscr{A}$ is selfadjoint, we see that $u \in \mathscr{A}_{\mathbb{R}}$. If $x_{1} \neq x_{2}$, there exists $f \in \mathscr{A}$ such that $f\left(x_{1}\right)=1$, $f\left(x_{2}\right)=0$; hence $0=u\left(x_{2}\right) \neq u\left(x_{1}\right)=1$, which shows that $\mathscr{A}_{\mathbb{R}}$ separates points on K. If $\mathrm{x} \in \mathrm{K}$, then $\mathrm{g}(\mathrm{x}) \neq 0$ for some $\mathrm{g} \in \mathscr{A}$, and there is a complex number such that $\lambda g(x)>0$; if $f=\lambda g, f=u+i v$, it follows that $u(x)>0$; hence $\mathscr{A}_{\mathbb{R}}$ vanishes at no point of K .

Thus $\mathscr{A}_{\mathbb{R}}$ satisfies the hypotheses of Theorem 7.32. It follows that every real continuous function on K lies in the uniform closure of $\mathscr{A}_{\mathbb{R}}$ hence lies in $\mathscr{B}$. If f is a complex continuous function on $\mathrm{K}, \mathrm{f}=\mathrm{u}+\mathrm{iv}$, then $\mathrm{u} \in \mathscr{B}, v \in \mathscr{B}$, hence $\mathrm{f} \in \mathscr{B}$. This completes the proof.

# EXERCISES 

7.1. Prove that every uniformly convergent sequence of bounded functions is uniformly bounded.
7.2. If $\left(f_{n}\right)$ and $\left(g_{n}\right)$ converge uniformly on a set $E$, prove that $\left(f_{n}+g_{n}\right)$ converges uniformly on E. If, in addition, $\left(f_{n}\right)$ and $\left(g_{n}\right)$ are sequences of bounded functions, prove that $\left(f_{n} g_{n}\right)$ converges uniformly on $E$.
7.3. Construct sequences $\left(f_{n}\right),\left(g_{n}\right)$ which converge uniformly on some set $E$, but such that $\left(f_{n} g_{n}\right)$ does not converge uniformly on $E$ (of course, $\left(f_{n} g_{n}\right)$ must converge on $E$ ).

# 7.4. Consider 

$$
f(x)=\sum_{n=1}^{\infty} \frac{1}{1+n^{2} x}
$$

For what values of $x$ does the series converge absolutely? On what intervals does it converge uniformly? On what intervals does it fail to converge uniformly? Is $f$ continuous wherever the series converges? Is $f$ bounded?
7.5. Let

$$
f_{n}(x)= \begin{cases}0 & \left(x<\frac{1}{n+1}\right) \\ \sin ^{2} \frac{n}{x} & \left(\frac{1}{n+1} \leq x \leq \frac{1}{n}\right) \\ 0 & \left(\frac{1}{n}<x\right)\end{cases}
$$

Show that $\left(f_{n}\right)$ converges to a continuous function, but not uniformly. Use the series $\Sigma f_{n}$ to show that absolute convergence, even for all $x$, does not imply uniform convergence.
7.6. Prove that the series

$$
\sum_{n=1}^{\infty}(-1)^{n} \frac{x^{2}+n}{n^{2}}
$$

converges uniformly in every bounded interval, but does not converge absolutely for any value of $x$.
7.7. For $n=1,2,3, \ldots, x$ real, put

$$
f_{n}(x)=\frac{x}{1+n x^{2}}
$$

Show that $\left(f_{n}\right)$ converges uniformly to a function $f$, and that the equation

$$
f^{\prime}(x)=\lim _{n \rightarrow \infty} f_{n}^{\prime}(x)
$$

is correct if $x \neq 0$, but false if $x=0$.
7.8. If

$$
I(x)= \begin{cases}0 & (x \leq 0) \\ 1 & (x>0)\end{cases}
$$

if $\left(x_{n}\right)$ is a sequence of distinct points of $(a, b)$, and if $\Sigma\left|c_{n}\right|$ converges, prove that the series

$$
f(x)=\sum_{n=1}^{\infty} c_{n} I\left(x-x_{n}\right) \quad(a \leq x \leq b)
$$

converges uniformly, and that $f$ is continuous for every $x \neq x_{n}$.
7.9. Let $\left(f_{n}\right)$ be a sequence of continuous functions which converges uniformly to a function $f$ on a set $E$. Prove that

$$
\lim _{n \rightarrow \infty} f_{n}\left(x_{n}\right)=f(x)
$$

for every sequence of points $x_{n} \in E$ such that $x_{n} \rightarrow x$, and $x \in E$. Is the converse of this true?
7.10. Letting $(x)$ denote the factorial part of the real number $x$ (see Exercise 4.16 for the definition), consider the function

$$
f(x)=\sum_{n=1}^{\infty} \frac{(n x)}{n^{2}} \quad(x \text { real })
$$

Find all discontinuities of $f$, and show that they form a countable dense set. Show that $f$ is nevertheless Riemann-integrable on every bounded interval.
7.11. Suppose $\left(f_{n}\right),\left(g_{n}\right)$ are defined on $E$, and

(a) $\Sigma \mathrm{f}_{\mathrm{n}}$ has uniformly bounded partial sums;
(b) $g_{n} \rightarrow 0$ uniformly on E ;
(c) $g_{1}(x) \geq g_{2}(x) \geq g_{3}(x) \geq \ldots$ for every $x \in E$.

Prove that $\Sigma \mathrm{f}_{\mathrm{n}} \mathrm{g}_{\mathrm{n}}$ converges uniformly on E. Hint: Compare with Theorem 3.42.
7.12. Suppose $g$ and $f_{n}(n=1,2,3, \ldots)$ are defined on $(0, \infty)$, are Riemann-integrable on $[t, T]$ whenever $0<\mathrm{t}<\mathrm{T}<\infty,\left|\mathrm{f}_{\mathrm{n}}\right| \leq \mathrm{g}, \mathrm{f}_{\mathrm{n}} \rightarrow \mathrm{f}$ uniformly on every compact subset of $(0, \infty)$, and

$$
\int_{0}^{\infty} g(x) d x<\infty
$$

Prove that

$$
\lim _{n \rightarrow \infty} \int_{0}^{\infty} f_{n}(x) d x=\int_{0}^{\infty} f(x) d x
$$

(See Exercises 6.7 and 6.8 for the relevant definitions.)
This is a rather weak form of Lebesgue's dominated convergence theorem (Theorem 11.32). Even in the context of the Riemann integral, uniform convergence can be replaced by pointwise convergence if it is assumed that $\mathrm{f} \in \mathscr{R}$. (See the articles by F. Cunningham in Math. Mag., vol. 40, 1967, pp. 179-186 [Cun67], and by H. Kestelman in Amer. Math. Monthly, vol. 77, 1970, pp. 182-187 [Kes70].)
7.13. Assume that $\left(f_{n}\right)$ is a sequence of monotonically increasing functions on $\mathbb{R}^{1}$ with $0 \leq$ $\mathrm{f}_{\mathrm{n}}(\mathrm{x}) \leq 1$ for all x and all n .
(a) Prove that there is a function $f$ and a sequence $\left(n_{k}\right)$ such that

$$
f(x)=\lim _{k \rightarrow \infty} f_{n_{k}}(x)
$$

for every $x \in \mathbb{R}^{1}$. (The existence of such a pointwise convergent subsequence is usually called Helly's selection theorem.)
(b) If, moreover, $f$ is continuous, prove that $f_{n_{k}} \rightarrow f$ uniformly on compact sets.

Hint: (i) Some subsequence $\left\{\mathrm{f}_{\mathrm{n}_{\mathrm{i}}}\right.$ ) converges at all rational points $\tau$, say, to $\mathrm{f}(\tau)$. (ii) Define $\mathrm{f}(\mathrm{x})$, for any $\mathrm{x} \in \mathbb{R}^{1}$, to be $\sup \mathrm{f}(\tau)$, the sup being taken over all $\tau \leq \mathrm{x}$. (iii) Show that $f_{n_{i}}(x) \rightarrow f(x)$ at every $x$ at which $f$ is continuous. (This is where monotonicity is strongly used.) (iv) A subsequence of $\left\{\mathrm{f}_{\mathrm{n}_{\mathrm{i}}}\right.$ ) converges at every point of discontinuity of f since there are at most countably many such points. This proves (a). To prove (b), modify your proof of (iii) appropriately.
7.14. Let $f$ be a continuous real function on $\mathbb{R}^{1}$ with the following properties: $0 \leq f(t) \leq 1$, $f(t+2)=f(t)$ for every $t$, and

$$
f(t)= \begin{cases}0 & (0 \leq t \leq \frac{1}{3}) \\ 1 & \left(\frac{2}{3} \leq t \leq 1\right)\end{cases}
$$

Put $\Phi(\mathrm{t})=(\mathrm{x}(\mathrm{t}), \mathrm{y}(\mathrm{t}))$, where

$$
x(t)=\sum_{n=1}^{\infty} 2^{-n} f\left(3^{2 n-1} t\right), \quad y(t)=\sum_{n=1}^{\infty} 2^{-n} f\left(3^{2 n} t\right)
$$

Prove that $\Phi$ is continuous and that $\Phi$ maps $I=[0,1]$ onto the unit square $I^{2} \subset \mathbb{R}^{2}$. In fact, show that $\Phi$ maps the Cantor set onto $\mathrm{I}^{2}$.

Hint: Each $\left(x_{0}, y_{0}\right) \in I^{2}$ has the form

$$
x_{0}=\sum_{n=1}^{\infty} 2^{-n} a_{2 n-1}, \quad y_{0}=\sum_{n=1}^{\infty} 2^{-n} a_{2 n}
$$

where each $a_{i}$ is 0 or 1 . If

$$
\mathrm{t}_{0}=\sum_{\mathrm{i}=1}^{\infty} 3^{-\mathrm{i}-1}\left(2 \mathrm{a}_{\mathrm{i}}\right)
$$

show that $f\left(3^{k} t_{0}\right)=a_{k}$, and hence that $x\left(t_{0}\right)=x_{0}, y\left(t_{0}\right)=y_{0}$.
(This simple example of a so-called "space-filling curve" is due to I. J. Schoenberg, Bull. A.M.S., vol. 44, 1938, pp. 519.)
7.15. Suppose $f$ is a real continuous function on $\mathbb{R}^{1}, f_{n}(t)=f(n t)$ for $n=1,2,3, \ldots$, and $\left(f_{n}\right)$ is equicontinuous on $[0,1]$. What conclusion can you draw about $f$ ?
7.16. Suppose $\left(f_{n}\right)$ is an equicontinuous sequence of functions on a compact set $K$, and $\left(f_{n}\right)$ converges pointwise on K. Prove that $\left(f_{n}\right)$ converges uniformly on $K$.
7.17. Define the notions of uniform convergence and equicontinuity for mappings into any metric space. Show that Theorems 7.9 and 7.12 are valid for mappings into any metric space, that Theorems 7.8 and 7.11 are valid for mappings into any complete metric space, and that Theorems $7.10,7.16,7.17,7.24$, and 7.25 hold for vector-valued functions, that is, for mappings into any $\mathbb{R}^{k}$.
7.18. Let $\left(f_{n}\right)$ be a uniformly bounded sequence of functions which are Riemann-integrable on $[a, b]$, and put

$$
F_{n}(x)=\int_{a}^{x} f_{n}(t) d t \quad(a \leq x \leq b)
$$

Prove that there exists a subsequence $\left(F_{n_{k}}\right)$ which converges uniformly on $[a, b]$.
7.19. Let K be a compact metric space, let S be a subset of $\mathscr{C}(\mathrm{K})$. Prove that S is compact (with respect to the metric defined in Definition 7.14) if and only if $S$ is uniformly closed, pointwise bounded, and equicontinuous. (If $S$ is not equicontinuous, then $S$ contains a sequence which has no equicontinuous subsequence, hence has no subsequence that converges uniformly on K.)
7.20. If $f$ is continuous on $[0,1]$ and if

$$
\int_{0}^{1} f(x) x^{n} d x=0 \quad(n=0,1,2, \ldots)
$$

prove that $f(x)=0$ on $[0,1]$. Hint: The integral of the product of $f$ with any polynomial is zero. Use the Weierstrass theorem to show that $\int_{0}^{1} f^{2}(x) d x=0$.
7.21. Let K be the unit circle in the complex plane (i.e., the set of all $z$ with $|z|=1$ ), and let $\mathscr{A}$ be the algebra of all functions of the form

$$
f\left(e^{i \theta}\right)=\sum_{n=0}^{N} c_{n} e^{i n \theta} \quad(\theta \text { real })
$$

Then $\mathscr{A}$ separates points on K and $\mathscr{A}$ vanishes at no point of K , but nevertheless there are continuous functions on K which are not in the uniform closure of $\mathscr{A}$.
Hint: For every $f \in \mathscr{A}$

$$
\int_{0}^{2 \pi} f\left(e^{i \theta}\right) e^{i \theta} d \theta=0
$$

and this is also true for every $f$ in the closure of $\mathscr{A}$.
7.22. Assume $f \in \mathscr{R}(\alpha)$ on $[a, b]$, and prove that there are polynomials $P_{n}$ such that

$$
\lim _{n \rightarrow \infty} \int_{a}^{b}\left|f-P_{n}\right|^{2} d \alpha=0
$$

(Compare with Exercise 6.12.)

7.23. Put $P_{0}=0$, and define, for $n=0,1,2, \ldots$,

$$
P_{n+1}(x)=P_{n}(x)+\frac{x^{2}-P_{n}^{2}(x)}{2}
$$

Prove that

$$
\lim _{n \rightarrow \infty} P_{n}(x)=|x|
$$

uniformly on $[-1,1]$.
(This makes it possible to prove the Stone-Weierstrass theorem without first proving Theorem 7.26.)

Hint: Use the identity

$$
|x|-P_{n+1}(x)=\left\|x\right\|-P_{n}(x) \mid\left[1-\frac{|x|+P_{n}(x)}{2}\right]
$$

to prove that $0 \leq \mathrm{P}_{\mathrm{n}}(\mathrm{x}) \leq \mathrm{P}_{\mathrm{n}+1}(\mathrm{x}) \leq|\mathrm{x}|$ if $|\mathrm{x}| \leq 1$, and that

$$
|x|-P_{n}(x) \leq|x|\left(1-\frac{|x|}{2}\right)^{n}<\frac{2}{n+1}
$$

if $|x| \leq 1$.
7.24. Let $X$ be a metric space, with metric $d$. Fix a point $a \in X$. Assign to each $p \in X$ the function $f_{p}$ defined by

$$
f_{p}(x)=d(x, p)-d(x, a) \quad(x \in X)
$$

Prove that $\left|f_{p}(x)\right| \leq d(a, p)$ for all $x \in X$, and that therefore $f_{p} \in \mathscr{C}(X)$.
Prove that

$$
\left\|f_{p}-f_{q}\right\|=d(p, q)
$$

for all $p, q \in X$.
If $\Phi(p)=f_{p}$ it follows that $\Phi$ is an isometry (a distance-preserving mapping) of $X$ onto $\Phi(X) \subset \mathscr{C}(X)$.

Let $Y$ be the closure of $\Phi(X)$ in $\mathscr{C}(X)$. Show that $Y$ is complete.
Conclusion: X is isometric to a dense subset of a complete metric space Y. (Exercise 3.24 contains a different proof of this.)
7.25. Suppose $\phi$ is a continuous bounded real function in the strip defined by $0 \leq x \leq 1$, $-\infty<y<\infty$. Prove that the initial value problem

$$
y^{\prime}=\phi(x, y), \quad y(0)=c
$$

has a solution. (Note that the hypotheses of this existence theorem are less stringent than those of the corresponding uniqueness theorem; see Exercise 5.27.)

Hint: Fix n. For $i=0, \ldots, n$, put $x_{i}=i / n$. Let $f_{n}$ be a continuous function on $[0,1]$ such that $f_{n}(0)=c$,

$$
f_{n}^{\prime}(t)=\phi\left(x_{i}, f_{n}\left(x_{i}\right)\right) \quad \text { if } x_{i}<t<x_{i+1}
$$

and put

$$
\Delta_{n}(t)=f_{n}^{\prime}(t)-\phi\left(t, f_{n}(t)\right)
$$

except at the points $x_{i}$, where $\Delta_{n}(t)=0$. Then

$$
f_{n}(x)=c+\int_{0}^{x}\left|\phi\left(t, f_{n}(t)\right)+\Delta_{n}(t)\right| d t
$$

Choose $M<\infty$ so that $|\phi| \leq M$. Verify the following assertions.
(a) $\left|f_{n}^{\prime}\right| \leq M,\left|\Delta_{n}\right| \leq 2 M, \Delta_{n} \in \mathscr{R}$, and $\left|f_{n}\right| \leq|c|+M=M_{1}$, say, on $[0,1]$, for all $n$.
(b) $\left(f_{n}\right)$ is equicontinuous on $[0,1]$, since $\left|f_{n}^{\prime}\right| \leq M$.

(c) Some $\left(f_{n_{k}}\right)$ converges to some $f$, uniformly on $[0,1]$.
(d) Since $\phi$ is uniformly continuous on the rectangle $0 \leq x \leq 1,|y| \leq M_{1}$,

$$
\phi\left(t, f_{n_{k}}(t)\right) \rightarrow \phi(t, f(t))
$$

uniformly on $[0,1]$.
(e) $\Delta_{n}(t) \rightarrow 0$ uniformly on $[0,1]$, since

$$
\Delta_{n}(t)=\phi\left(x_{i}, f_{n}\left(x_{i}\right)\right)-\phi\left(t, f_{n}(t)\right)
$$

in $\left(x_{i}, x_{i+1}\right)$.
(f) Hence

$$
f(x)=c+\int_{0}^{x} \phi(t, f(t)) d t
$$

This $f$ is a solution of the given problem.
7.26. Prove an analogous existence theorem for the initial-value problem

$$
\mathbf{y}^{\prime}=\Phi(\mathrm{x}, \mathbf{y}), \quad \mathbf{y}(0)=\mathbf{c}
$$

where now $\mathbf{c} \in \mathbb{R}^{\mathrm{k}}, \mathbf{y} \in \mathbb{R}^{\mathrm{k}}$, and $\Phi$ is a continuous bounded mapping of the part of $\mathbb{R}^{\mathrm{k}+1}$ defined by $0 \leq \mathrm{x} \leq 1, \mathbf{y} \in \mathbb{R}^{\mathrm{k}}$ into $\mathbb{R}^{\mathrm{k}}$. (Compare Exercise 5.28.) Hint: Use the vector-valued version of Theorem 7.25.

# Chapter 8 

## SOME SPECIAL FUNCTIONS

## POWER SERIES

In this section we shall derive some properties of functions which are represented by power series, i.e., functions of the form

$$
f(x)=\sum_{n=0}^{\infty} c_{n} x^{n}
$$

or, more generally,

$$
f(x)=\sum_{n=0}^{\infty} c_{n}(x-a)^{n}
$$

These are called analytic functions.
We shall restrict ourselves to real values of $x$. Instead of circles of convergence (see Theorem 3.39) we shall therefore encounter intervals of convergence.

If (8.1) converges for all $x$ in $(-R, R)$, for some $R>0(R$ may be $+\infty)$, we say that $f$ is expanded in a power series about the point $x=0$. Similarly, if (8.2) converges for $|x-a|<R, f$ is said to be expanded in a power series about the point $x=a$. As a matter of convenience, we shall often take $a=0$ without any loss of generality.
8.1 Theorem. Suppose the series

$$
\sum_{n=0}^{\infty} c_{n} x^{n}
$$

converges for $|x|<R$, and define

$$
f(x)=\sum_{n=0}^{\infty} c_{n} x^{n} \quad(|x|<R)
$$

Then (8.3) converges uniformly on $[-R+\varepsilon, R-\varepsilon]$, no matter which $\varepsilon>0$ is chosen. The function f is continuous and differentiable in $(-\mathrm{R}, \mathrm{R})$, and

$$
f^{\prime}(x)=\sum_{n=1}^{\infty} n c_{n} x^{n-1} \quad(|x|<R)
$$

Proof. Let $\varepsilon>0$ be given. For $|x| \leq R-\varepsilon$, we have

$$
\left|c_{n} x^{n}\right| \leq\left|c_{n}(R-\varepsilon)^{n}\right|
$$

and since

$$
\sum c_{n}(R-\varepsilon)^{n}
$$

converges absolutely (every power series converges absolutely in the interior of its interval of convergence, by the root test), Theorem 7.10 shows the uniform convergence of (8.3) on $[-R+\varepsilon, R-\varepsilon]$.

Since $\sqrt[n]{n} \rightarrow 1$ as $n \rightarrow \infty$, we have

$$
\limsup _{n \rightarrow \infty} \sqrt[n]{\left|c_{n}\right|}=\limsup _{n \rightarrow \infty} \sqrt[n]{\left|c_{n}\right|}
$$

so that the series (8.4) and (8.5) have the same interval of convergence.
Since (8.5) is a power series, it converges uniformly in $[-R+\varepsilon, R-\varepsilon]$ for every $\varepsilon>0$, and we can apply Theorem 7.17 (for series instead of sequences). It follows that (8.5) holds if $|x| \leq R-\varepsilon$.

But, given any $x$ such that $|x|<R$, we can find an $\varepsilon>0$ such that $|x|<R-\varepsilon$. This shows that (8.5) holds for $|x|<R$.

Continuity of $f$ follows from the existence of $f^{\prime}$ (Theorem 5.2).
Corollary. Under the hypothesis of Theorem 8.1, f has derivatives of all orders in $(-\mathrm{R}, \mathrm{R})$, which are given by

$$
f^{(k)}(x)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n} x^{n-k}
$$

In particular,

$$
f^{(k)}(0)=k!c_{k} \quad(k=0,1,2, \ldots)
$$

(Here $f^{(0)}$ means $f$, and $f^{(k)}$ is the $k$ th derivative of $f$, for $k=1,2,3, \ldots$ ).
Proof. Equation (8.6) follows if we apply Theorem 8.1 successively to $f, f^{\prime}, f^{\prime \prime}, \ldots$ Putting $x=0$ in (8.6), we obtain (8.7).

Formula (8.7) is very interesting. It shows, on the one hand, that the coefficients of the power series development of $f$ are determined by the values of $f$ and of its derivatives at a single point. On the other hand, if the coefficients are given, the

values of the derivatives of $f$ at the center of the interval of convergence can be read off immediately from the power series.

Note, however, that although a function $f$ may have derivatives of all orders, the series $\sum c_{n} x^{n}$, where $c_{n}$ is computed by (8.7), need not converge to $f(x)$ for any $x \neq 0$. In this case, $f$ cannot be expanded in a power series about $x=0$. For if we had $f(x)=\sum a_{n} x^{n}$, we should have

$$
n!a_{n}=f^{(n)}(0)
$$

hence $a_{n}=c_{n}$. An example of this situation is given in Exercise 8.1.
If the series (8.3) converges at an endpoint, say at $x=R$, then $f$ is continuous not only in $(-R, R)$, but also at $x=R$. This follows from Abel's theorem (for simplicity of notation, we take $R=1$ ):
8.2 Theorem. Suppose $\sum c_{n}$ converges. Put

$$
f(x)=\sum_{n=0}^{\infty} c_{n} x^{n} \quad(-1<x<1)
$$

Then

$$
\lim _{x \rightarrow 1} f(x)=\sum_{n=0}^{\infty} c_{n}
$$

Proof. Let $s_{n}=c_{0}+\cdots+c_{n}, s_{-1}=0$. Then

$$
\sum_{n=0}^{\infty} c_{n} x^{n}=\sum_{n=0}^{m}\left(s_{n}-s_{n-1}\right) x^{n}=(1-x) \sum_{n=0}^{m-1} s_{n} x^{n}+s_{m} x^{m}
$$

For $|x|<1$, we let $m \rightarrow \infty$ and obtain

$$
f(x)=(1-x) \sum_{n=0}^{\infty} s_{n} x^{n}
$$

Suppose $s=\lim _{n \rightarrow \infty} s_{n}$. Let $\varepsilon>0$ be given. Choose $N$ so that $n>N$ implies

$$
\left|s-s_{n}\right|<\frac{\varepsilon}{2}
$$

Then, since

$$
(1-x) \sum_{n=0}^{\infty} x^{n}=1 \quad(|x|<1)
$$

we obtain from (8.9)

$$
|f(x)-s|=\left|(1-x) \sum_{n=0}^{\infty}\left(s_{n}-s\right) x^{n}\right| \leq(1-x) \sum_{n=0}^{N}\left|s_{n}-s\right||x|^{n}+\frac{\varepsilon}{2} \leq \varepsilon
$$

if $x>1-\delta$, for some suitably chosen $\delta>0$. This implies (8.8).
As an application, let us prove Theorem 3.51, which asserts: If $\sum a_{n}, \sum b_{n}, \sum c_{n}$, converge to $A, B, C$, and if $c_{n}=a_{0} b_{n}+\ldots+a_{n} b_{0}$, then $C=A B$. We let

$$
f(x)=\sum_{n=0}^{\infty} a_{n} x^{n}, \quad g(x)=\sum_{n=0}^{\infty} b_{n} x^{n}, \quad h(x)=\sum_{n=0}^{\infty} c_{n} x^{n}
$$

for $0 \leq x \leq 1$. For $x<1$, these series converge absolutely and hence may be multiplied according to Definition 3.48; when the multiplication is carried out, we see that

$$
f(x) \cdot g(x)=h(x) \quad(0 \leq x<1)
$$

By Theorem 8.2,

$$
f(x) \rightarrow A, \quad g(x) \rightarrow B, \quad h(x) \rightarrow C
$$

as $x \rightarrow 1$. Equations (8.10) and (8.11) imply $A B=C$.
We now require a theorem concerning an inversion in the order of summation. (See Exercises 8.2 and 8.3.)
8.3 Theorem. Given a double sequence $\left(a_{i j}\right), i=1,2,3 \ldots, j=1,2,3, \ldots$, suppose that

$$
\sum_{j=1}^{\infty}\left|a_{i j}\right|=b_{i} \quad(i=1,2,3, \ldots)
$$

and $\sum \mathrm{b}_{\mathrm{i}}$ converges. Then

$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{i j}=\sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{i j}
$$

Proof. We could establish (8.13) by a direct procedure similar to (although more involved than) the one used in Theorem 3.55. However, the following method seems more interesting.

Let $E$ be a countable set, consisting of the points $x_{0}, x_{1}, x_{2}, \ldots$, and suppose $x_{n} \rightarrow x_{0}$ as $n \rightarrow \infty$. Define

$$
\begin{array}{rlrl}
f_{i}\left(x_{0}\right) & =\sum_{j=1}^{\infty} a_{i j} & & (i=1,2,3, \ldots) \\
f_{i}\left(x_{n}\right) & =\sum_{j=1}^{n} a_{i j} & & (i, n=1,2,3, \ldots) \\
g(x) & =\sum_{i=1}^{\infty} f_{i}(x) & & (x \in E)
\end{array}
$$

Now, (8.14) and (8.15), together with (8.12), show that each $f_{i}$ is continuous at $\mathrm{x}_{0}$. Since $\left|\mathrm{f}_{\mathrm{i}}(\mathrm{x})\right| \leq \mathrm{b}_{\mathrm{i}}$ for $\mathrm{x} \in \mathrm{E}$, (8.16) converges uniformly, so that g is continuous at $x_{0}$ (Theorem 7.11). It follows that

$$
\begin{aligned}
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{i j} & =\sum_{i=1}^{\infty} f_{i}\left(x_{0}\right)=g\left(x_{0}\right)=\lim _{n \rightarrow \infty} g\left(x_{n}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{\infty} f_{i}\left(x_{n}\right)=\lim _{n \rightarrow \infty} \sum_{i=1}^{\infty} \sum_{j=1}^{n} a_{i j} \\
& =\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \sum_{i=1}^{\infty} a_{i j}=\sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{i j}
\end{aligned}
$$

8.4 Theorem. Suppose

$$
f(x)=\sum_{n=0}^{\infty} c_{n} x^{n}
$$

the series converging in $|x|<R$. If $-\mathrm{R}<\mathrm{a}<\mathrm{R}$, then f can be expanded in a power series about the point $\mathrm{x}=\mathrm{a}$ which converges in $|\mathrm{x}-\mathrm{a}|<\mathrm{R}-|\mathrm{a}|$, and

$$
f(x)=\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^{n} \quad(|x-a|<R-|a|)
$$

This is an extension of Theorem 5.15 and is also known as Taylor's theorem.
Proof. We have

$$
\begin{aligned}
f(x) & =\sum_{n=0}^{\infty} c_{n}[(x-a)+a]^{n} \\
& =\sum_{n=0}^{\infty} c_{n} \sum_{m=0}^{n}\binom{n}{m} a^{n-m}(x-a)^{m} \\
& =\sum_{m=0}^{\infty}\left[\sum_{n=m}^{\infty}\binom{n}{m} c_{n} a^{n-m}\right](x-a)^{m}
\end{aligned}
$$

This is the desired expansion about the point $x=a$. To prove its validity, we have to justify the change which was made in the order of summation. Theorem 8.3 shows that this is permissible if

$$
\sum_{n=0}^{\infty} \sum_{m=0}^{n}\left|c_{n}\binom{n}{m} a^{n-m}(x-a)^{m}\right|
$$

converges. But (8.18) is the same as

$$
\sum_{n=0}^{\infty}\left|c_{n}\right| \cdot(|x-a|+|a|)^{n}
$$

and (8.19) converges if $|x-a|+|a|<R$
Finally, the form of the coefficients in (8.17) follows from (8.7).
It should be noted that (8.17) may actually converge in a larger interval than the one given by $|x-a|<R-|a|$.

If two power series converge to the same function in $(-R, R),(8.7)$ shows that the two series must be identical, i.e., they must have the same coefficients. It is interesting that the same conclusion can be deduced from much weaker hypotheses:
8.5 Theorem. Suppose the series $\sum a_{n} x^{n}$ and $\sum b_{n} x^{n}$ converge in the segment $S=$ $(-R, R)$. Let $E$ be the set of all $x \in S$ at which

$$
\sum_{n=0}^{\infty} a_{n} x^{n}=\sum_{n=0}^{\infty} b_{n} x^{n}
$$

If E has a limit point in S , then $a_{n}=b_{n}$ for $n=0,1,2, \ldots$ Hence (8.20) holds for all $x \in S$.

Proof. Put $c_{n}=a_{n}-b_{n}$ and

$$
f(x)=\sum_{n=0}^{\infty} c_{n} x^{n} \quad(x \in S)
$$

Then $f(x)=0$ on $E$.
Let $A$ be the set of all limit points of $E$ in $S$, and let $B$ consist of all other points of $S$. It is clear from the definition of "limit point" that $B$ is open. Suppose we can prove that $A$ is open. Then $A$ and $B$ are disjoint open sets. Hence they are separated (Definition 2.45). Since $S=A \cup B$, and $S$ is connected, one of $A$ and $B$ must be empty. By hypothesis, $A$ is not empty. Hence $B$ is empty, and $A=S$. Since $f$ is continuous in $S, A \subset E$. Thus $E=S$, and (8.7) shows that $c_{n}=0$ for $n=0,1,2, \ldots$, which is the desired conclusion.

Thus we have to prove that $A$ is open. If $x_{0} \in A$, Theorem 8.4 shows that

$$
f(x)=\sum_{n=0}^{\infty} d_{n}\left(x-x_{0}\right)^{n} \quad\left(\left|x-x_{0}\right|<R-\left|x_{0}\right|\right)
$$

We claim that $d_{n}=0$ for all $n$. Otherwise, let $k$ be the smallest non-negative integer such that $d_{k} \neq 0$. Then

$$
f(x)=\left(x-x_{0}\right)^{k} g(x) \quad\left(\left|x-x_{0}\right|<R-\left|x_{0}\right|\right)
$$

where

$$
g(x)=\sum_{m=0}^{\infty} d_{k+m}\left(x-x_{0}\right)^{m}
$$

Since $g$ is continuous at $x_{0}$ and

$$
g\left(x_{0}\right)=d_{k} \neq 0
$$

there exists a $\delta>0$ such that $g(x) \neq 0$ if $\left|x-x_{0}\right|<\delta$. It follows from (8.23) that $f(x) \neq 0$ if $0<\left|x-x_{0}\right|<\delta$. But this contradicts the fact that $x_{0}$ is a limit point of $E$.

Thus $d_{n}=0$ for all $n$, so that $f(x)=0$ for all $x$ for which (8.22) holds, i.e., a neighborhood of $x_{0}$. This shows that $A$ is open and completes the proof.

# THE EXPONENTIAL AND LOGARITHMIC FUNCTIONS 

We define

$$
E(z)=\sum_{n=0}^{\infty} \frac{z^{n}}{n!}
$$

The ratio test shows that this series converges for every complex $z$. Applying Theorem 3.50 on multiplication of absolutely convergent series, we obtain

$$
\begin{aligned}
E(z) E(w) & =\sum_{n=0}^{\infty} \frac{z^{n}}{n!} \sum_{m=0}^{\infty} \frac{w^{m}}{m!}=\sum_{n=0}^{\infty} \sum_{k=0}^{n} \frac{z^{k} w^{n-k}}{k!(n-k)!} \\
& =\sum_{n=0}^{\infty} \frac{1}{n!} \sum_{k=0}^{n}\binom{n}{k} z^{k} w^{n-k}=\sum_{n=0}^{\infty} \frac{(z+w)^{n}}{n!}
\end{aligned}
$$

which gives us the important addition formula

$$
E(z+w)=E(z) E(w) \quad(z, w \text { complex })
$$

One consequence is that

$$
E(z) E(-z)=E(z-z)=E(0)=1 \quad(z \text { complex })
$$

This shows that $E(z) \neq 0$ for all $z$. By (8.25), $E(x)>0$ if $x>0$; hence (8.27) shows that $E(x)>0$ for all real $x$. By (8.25), $E(x) \rightarrow+\infty$ as $x \rightarrow+\infty$; hence (8.27) shows that $E(x) \rightarrow 0$ as $x \rightarrow-\infty$ along the real axis. By (8.25), $0<x<y$ implies that $E(x)<E(y)$; by (8.27), it follows that $E(-y)<E(-x)$; hence $E$ is strictly increasing on the whole real axis.

The addition formula also shows that

$$
\lim _{h \rightarrow 0} \frac{E(z+h)-E(z)}{h}=E(z) \lim _{h \rightarrow 0} \frac{E(h)-1}{h}=E(z)
$$

the last equality follows directly from (8.25).
Iteration of (8.26) gives

$$
E\left(z_{1}+\cdots+z_{n}\right)=E\left(z_{1}\right) \cdots E\left(z_{n}\right)
$$

Let us take $z_{1}=\cdots=z_{n}=1$. Since $E(1)=e$, where $e$ is the number defined in Definition 3.30, we obtain

$$
E(n)=e^{n} \quad(n=1,2,3, \ldots)
$$

If $p=n / m$, where $n, m$ are positive integers, then

$$
[E(p)]^{m}=E(m p)=E(n)=e^{n}
$$

so that

$$
E(p)=e^{p} \quad(p>0, p \text { rational })
$$

It follows from (8.27) that $E(-p)=e^{-p}$ if $p$ is positive and rational. Thus (8.32) holds for all rational $p$.

In Exercise 1.6, we suggested the definition

$$
x^{y}=\sup x^{p}
$$

where the sup is taken over all rational $p$ such that $p<y$, for any real $y$, and $x>1$. If we thus define, for any real $x$,

$$
e^{x}=\sup e^{p} \quad(p<x, p \text { rational })
$$

the continuity and monotonicity properties of $E$, together with (8.32), show that

$$
E(x)=e^{x}
$$

for all real $x$. Equation (8.35) explains why $E$ is called the exponential function.
The notation $\exp (x)$ is often used in place of $e^{x}$, especially when $x$ is a complicated expression.

Actually one may very well use (8.35) instead of (8.34) as the definition of $e^{x}$; (8.35) is a much more convenient starting point for the investigation of the properties of $e^{x}$. We shall see presently that (8.33) may also be replaced by a more convenient definition [see (8.43)].

We now revert to the customary notation, $e^{x}$, in place of $E(x)$, and summarize what we have proved so far.
8.6 Theorem. Let $e^{x}$ be defined on $\mathbb{R}^{1}$ by (8.35) and (8.25). Then
(a) $e^{x}$ is continuous and differentiable for all $x$;
(b) $\left(e^{x}\right)^{\prime}=e^{x}$;
(c) $e^{x}$ is a strictly increasing function of $x$, and $e^{x}>0$;

(d) $\mathrm{e}^{\mathrm{x}+\mathrm{y}}=\mathrm{e}^{\mathrm{x}} \mathrm{e}^{\mathrm{y}}$
(e) $\mathrm{e}^{\mathrm{x}} \rightarrow+\infty$ as $\mathrm{x} \rightarrow+\infty, \mathrm{e}^{\mathrm{x}} \rightarrow 0$ as $\mathrm{x} \rightarrow-\infty$;
(f) $\lim _{x \rightarrow+\infty} x^{n} e^{-x}=0$ for every $n$.

Proof. We have already proved (a) to (e); (8.25) shows that

$$
e^{x}>\frac{x^{n+1}}{(n+1)!}
$$

for $x>0$, so that

$$
x^{n} e^{-x}<\frac{(n+1)!}{x}
$$

and (f) follows. Part (f) shows that $\mathrm{e}^{\mathrm{x}}$ tends to $+\infty$ "faster" than any power of x as $x \rightarrow+\infty$.

Since $E$ is strictly increasing and differentiable on $\mathbb{R}^{1}$, it has an inverse function $L$ which is also strictly increasing and differentiable and whose domain is $E\left(\mathbb{R}^{1}\right)$, that is, the set of all positive numbers. L is defined by

$$
E(L(y))=y \quad(y>0)
$$

or, equivalently, by

$$
L(E(x))=x \quad(x \text { real })
$$

Differentiating (8.37), we get (compare Theorem 5.5)

$$
L^{\prime}(E(x)) \cdot E(x)=1
$$

Writing $y=E(x)$, this gives us

$$
L^{\prime}(y)=\frac{1}{y} \quad(y>0)
$$

Taking $x=0$ in (8.37), we see that $L(1)=0$. Hence (8.38) implies

$$
L(y)=\int_{1}^{y} \frac{d x}{x}
$$

Quite frequently, (8.39) is taken as the starting point of the theory of the logarithm and the exponential function. Writing $u=E(x), v=E(y)$, (8.26) gives

$$
L(u v)=L(E(x) \cdot E(y))=L(E(x+y))=x+y
$$

so that

$$
L(u v)=L(u)+L(v) \quad(u>0, v>0)
$$

This shows that $L$ has the familiar property which makes logarithms useful tools for computation. The customary notation $L(x)$ is of course $\log x$.

As to the behavior of $\log x$ as $x \rightarrow+\infty$ and as $x \rightarrow 0$, Theorem 8.6(e) shows that

$$
\begin{array}{ll}
\log x \rightarrow+\infty & \text { as } x \rightarrow+\infty \\
\log x \rightarrow-\infty & \text { as } x \rightarrow 0
\end{array}
$$

It is easily seen that

$$
x^{n}=E(n L(x))
$$

if $x>0$ and $n$ is an integer. Similarly, if $m$ is a positive integer, we have

$$
x^{1 / m}=E\left(\frac{1}{m} L(x)\right)
$$

since each term of (8.42), when raised to the mth power, yields the corresponding term of (8.36). Combining (8.41) and (8.42), we obtain

$$
x^{\alpha}=E(\alpha L(x))=e^{\alpha \log x}
$$

for any rational $\alpha$.
We now define $x^{\alpha}$, for any real $\alpha$ and any $x>0$, by (8.43). The continuity and monotonicity of $E$ and $L$ show that this definition leads to the same result as the previously suggested one. The facts stated in Exercise 1.6 are trivial consequences of (8.43).

If we differentiate (8.43), we obtain, by Theorem 5.5,

$$
\left(x^{\alpha}\right)^{\prime}=E(\alpha L(x)) \cdot \frac{\alpha}{x}=\alpha x^{\alpha-1}
$$

Note that we have previously used (8.44) only for integral values of $\alpha$, in which case (8.44) follows easily from Theorem 5.3(b). To prove (8.44) directly from the definition of the derivative, if $x^{\alpha}$ is defined by (8.33) and $\alpha$ is irrational, is quite troublesome.

The well-known integration formula for $x^{\alpha}$ follows from (8.44) if $\alpha \neq-1$, and from (8.38) if $\alpha=-1$. We wish to demonstrate one property of $\log x$, namely,

$$
\lim _{x \rightarrow+\infty} x^{-\alpha} \log x=0
$$

for every $\alpha>0$. That is, $\log x \rightarrow+\infty$ "slower" than any positive power of $x$ as $x \rightarrow+\infty$.

For if $0<\varepsilon<\alpha$, and $x>1$, then

$$
\begin{aligned}
x^{-\alpha} \log x & =x^{-\alpha} \int_{1}^{x} t^{-1} d t<x^{-\alpha} \int_{1}^{x} t^{\varepsilon-1} d t \\
& =x^{-\alpha} \cdot \frac{x^{\varepsilon}-1}{\varepsilon}<\frac{x^{\varepsilon-\alpha}}{\varepsilon}
\end{aligned}
$$

and (8.45) follows. We could also have used Theorem 8.6(f) to derive (8.45).

# THE TRIGONOMETRIC FUNCTIONS 

Let us define

$$
C(x)=\frac{1}{2}[E(i x)+E(-i x)], \quad S(x)=\frac{1}{2 i}[E(i x)-E(-i x)]
$$

We shall show that $C(x)$ and $S(x)$ coincide with the functions $\cos x$ and $\sin x$, whose definition is usually based on geometric considerations. By (8.25), $E(\bar{z})=\overline{E(z)}$. Hence (8.46) shows that $C(x)$ and $S(x)$ are real for real $x$. Also,

$$
E(i x)=C(x)+i S(x)
$$

Thus $C(x)$ and $S(x)$ are the real and imaginary parts, respectively, of $E(i x)$, if $x$ is real. By (8.27),

$$
|E(i x)|^{2}=E(i x) \overline{E(i x)}=E(i x) E(-i x)=1
$$

so that

$$
|E(i x)=1| \quad(x \text { real })
$$

From (8.46) we can read off that $C(0)=1, S(0)=0$, and (8.28) shows that

$$
C^{\prime}(x)=-S(x), \quad S^{\prime}(x)=C(x)
$$

We assert that there exist positive numbers $x$ such that $C(x)=0$. For suppose this is not so. Since $C(0)=1$, it then follows that $C(x)>0$ for all $x>0$, hence $S^{\prime}(x)>0$, by (8.49), hence $S$ is strictly increasing; and since $S(0)=0$, we have $S(x)>0$ if $x>0$. Hence if $0<x<y$, we have

$$
S(x)(y-x)<\int_{x}^{y} S(t) d t=C(x)-C(y) \leq 2
$$

The last inequality follows from (8.48) and (8.47). Since $S(x)>0$, (8.50) cannot be true for large $y$, and we have a contradiction.

Let $x_{0}$ be the smallest positive number such that $C\left(x_{0}\right)=0$. This exists, since the set of zeroes of a continuous function is closed, and $C(0) \neq 0$. We define the

number $\pi$ by

$$
\pi=2 x_{0}
$$

Then $C(\pi / 2)=0$, and (8.48) shows that $S(\pi / 2)= \pm 1$. Since $C(x)>0$ in $(0, \pi / 2), S$ is increasing in $(0, \pi / 2)$; hence $S(\pi / 2)=1$. Thus

$$
E\left(\frac{\pi i}{2}\right)=i
$$

and the addition formula gives

$$
E(\pi i)=-1, \quad E(2 \pi i)=1
$$

hence

$$
E(z+2 \pi i)=E(z) \quad(z \text { complex })
$$

# 8.7 Theorem. 

(a) The function E is periodic, with period $2 \pi \mathrm{i}$.
(b) The functions $C$ and $S$ are periodic, with period $2 \pi$.
(c) If $0<t<2 \pi$, then $E(i t) \neq 1$.
(d) If $z$ is a complex number with $|z|=1$, there is a unique $t$ in $[0,2 \pi)$ such that $E(i t)=z$.

Proof. By (8.53), (a) holds; and (b) follows from (a) and (8.46).
Suppose $0<t<\pi / 2$ and $E(i t)=x+i y$, with $x, y$ real. Our preceding work shows that $0<x<1,0<y<1$. Note that

$$
E(4 i t)=(x+i y)^{4}=x^{4}-6 x^{2} y^{2}+y^{4}+4 i x y\left(x^{2}-y^{2}\right)
$$

If $E(4 i t)$ is real, it follows that $x^{2}-y^{2}=0$; since $x^{2}+y^{2}=1$, by (8.48), we have $x^{2}=y^{2}=\frac{1}{2}$, hence $E(4 i t)=-1$. This proves (c).

If $0 \leq \mathrm{t}_{1}<\mathrm{t}_{2}<2 \pi$, then

$$
E\left(i t_{2}\right)\left[E\left(i t_{1}\right)\right]^{-1}=E\left(i t_{2}-i t_{1}\right) \neq 1
$$

by (c). This establishes the uniqueness assertion in (d).
To prove the existence assertion in (d), fix $z$ so that $|z|=1$. Write $z=x+i y$, with $x$ and $y$ real. Suppose first that $x \geq 0$ and $y \geq 0$. On $[0, \pi / 2], C$ decreases from 1 to 0 . Hence $C(t)=x$ for some $t \in[0, \pi / 2]$. Since $C^{2}+S^{2}=1$ and $S \geq 0$ on $[0, \pi / 2]$, it follows that $z=E(i t)$.

If $x<0$ and $y \geq 0$, the preceding conditions are satisfied by $-i z$. Hence $-i z=$ $E(i t)$ for some $t \in[0, \pi / 2]$, and since $i=E(\pi i / 2)$, we obtain $z=E(i(t+\pi / 2))$.

Finally, if $y<0$, the preceding two cases show that $-z=E(i t)$ for some $t \in(0, \pi)$. Hence $z=-E(i t)=E(i(t+\pi))$.

This proves (d), and hence the theorem.
It follows from (d) and (8.48) that the curve $\gamma$ defined by

$$
\gamma(t)=E(i t) \quad(0 \leq t \leq 2 \pi)
$$

is a simple closed curve whose range is the unit circle in the plane. Since $\gamma^{\prime}(t)=$ $i E(i t)$, the length of $\gamma$ is

$$
\int_{0}^{2 \pi}\left|\gamma^{\prime}(t)\right| d t=2 \pi
$$

by Theorem 6.27. This is of course the expected result for the circumference of a circle of radius 1 . It shows that $\pi$, defined by (8.51), has the usual geometric significance.

In the same way we see that the point $\gamma(t)$ describes a circular arc of length $t_{0}$ as $t$ increases from 0 to $t_{0}$. Consideration of the triangle whose vertices are

$$
z_{1}=0, \quad z_{2}=\gamma\left(t_{0}\right), \quad z_{3}=C\left(t_{0}\right)
$$

shows that $C(t)$ and $S(t)$ are indeed identical with $\cos t$ and $\sin t$, if the latter are defined in the usual way as ratios of the sides of a right triangle.

It should be stressed that we derived the basic properties of the trigonometric functions from (8.46) and (8.25), without any appeal to the geometric notion of angle. There are other nongeometric approaches to these functions. The papers by W. F. Eberlein (Amer. Math. Monthly, vol. 74, 1967, pp. 1223 -1225 [Ebe54]) and by G. B. Robison (Math. Mag., vol. 41, 1968, pp. 66 -70 [Rob68]) deal with these topics.

# THE ALGEBRAIC COMPLETENESS OF THE COMPLEX FIELD 

We are now in a position to give a simple proof of the fact that the complex field is algebraically complete, that is to say, that every nonconstant polynomial with complex coefficients has a complex root.
8.8 Theorem. Suppose $a_{0}, \ldots, a_{n}$ are complex numbers, $n \geq 1, a_{n} \neq 0$,

$$
\mathrm{P}(z)=\sum_{\mathrm{k}=0}^{\mathrm{n}} \mathrm{a}_{\mathrm{k}} \mathrm{z}^{\mathrm{k}}
$$

Then $\mathrm{P}(z)=0$ for some complex number $z$.
Proof. Without loss of generality, assume $a_{n}=1$. Put

$$
\mu=\inf |\mathrm{P}(z)| \quad(z \text { complex })
$$

If $|z|=R$, then

$$
|\mathrm{P}(z)| \geq \mathrm{R}^{\mathrm{n}}\left[1-\left|\mathrm{a}_{\mathrm{n}-1}\right| \mathrm{R}^{-1}-\cdots-\left|\mathrm{a}_{0}\right| \mathrm{R}^{-\mathrm{n}}\right]
$$

The right side of (8.56) tends to $\infty$ as $R \rightarrow \infty$. Hence there exists $R_{0}$ such that $|\mathrm{P}(z)|>\mu$ if $|z|>R_{0}$. Since $|P|$ is continuous on the closed disc with center at 0 and radius $R_{0}$, Theorem 4.16 shows that $\left|P\left(z_{0}\right)\right|=\mu$ for some $z_{0}$.

We claim that $\mu=0$.
If not, put $\mathrm{Q}(z)=\mathrm{P}\left(z+z_{0}\right) / \mathrm{P}\left(z_{0}\right)$. Then Q is a nonconstant polynomial, $\mathrm{Q}(0)=1$, and $|\mathrm{Q}(z)| \geq 1$ for all $z$. There is a smallest integer $\mathrm{k}, 1 \leq \mathrm{k} \leq \mathrm{n}$, such that

$$
\mathrm{Q}(z)=1+b_{k} z^{k}+\cdots+b_{n} z^{n}, \quad b_{k} \neq 0
$$

By Theorem 8.7(d) there is a real $\theta$ such that

$$
\mathrm{e}^{\mathrm{i} k \theta} \mathrm{~b}_{\mathrm{k}}=-\left|\mathrm{b}_{\mathrm{k}}\right|
$$

If $r>0$ and $r^{k}\left|b_{k}\right|<1$, (8.58) implies

$$
\left|1+b_{k} r^{k} e^{i k \theta}\right|=1-r^{k}\left|b_{k}\right|
$$

so that

$$
\left|Q\left(r e^{i \theta}\right)\right| \leq 1-r^{k}\left\{\left|b_{k}\right|-r\left|b_{k+1}\right|-\cdots-r^{n-k}\left|b_{n}\right|\right\}
$$

For sufficiently small $r$, the expression in braces is positive; hence $\left|Q\left(r e^{i \theta}\right)\right|<1$, a contradiction.

Thus $\mu=0$, that is, $\mathrm{P}\left(z_{0}\right)=0$.
Exercise 8.27 contains a more general result.

# FOURIER SERIES 

8.9 Definition. A trigonometric polynomial is a finite sum of the form

$$
f(x)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos n x+b_{n} \sin n x\right) \quad(x \text { real })
$$

where $a_{0}, \ldots, a_{N}, b_{1}, \ldots, b_{N}$ are complex numbers. On account of the identities (8.46), (8.59) can also be written in the form

$$
f(x)=\sum_{n=-N}^{N} c_{n} e^{i n x} \quad(x \text { real })
$$

which is more convenient for most purposes. It is clear that every trigonometric polynomial is periodic, with period $2 \pi$.

If $n$ is a nonzero integer, $e^{\text {in }}$ is the derivative of $e^{\text {in } / / \text { in }}$, which also has period $2 \pi$. Hence

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i n x} d x= \begin{cases}1 & \text { (if } n=0) \\ 0 & \text { (if } n= \pm 1, \pm 2, \ldots)\end{cases}
$$

Let us multiply (8.60) by $\mathrm{e}^{-\mathrm{imx}}$, where m is an integer; if we integrate the product, (8.61) shows that

$$
c_{m}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) e^{-i m x} d x
$$

for $|m| \leq N$. If $|m|>N$, the integral in (8.62) is 0 .
The following observation can be read off from (8.60) and (8.62): The trigonometric polynomial $f$ given by (8.60) is real if and only if $c_{-n}=\bar{c}_{n}$ for $n=0, \ldots, N$.

In agreement with (8.60), we define a trigonometric series to be a series of the form

$$
\sum_{n=-\infty}^{\infty} c_{n} e^{i n x} \quad(x \text { real })
$$

the Nth partial sum of (8.63) is defined to be the right side of (8.60).
If $f$ is an integrable function on $[-\pi, \pi]$, the numbers $c_{m}$ defined by (8.62) for all integers $m$ are called the Fourier coefficients of $f$, and the series (8.63) formed with these coefficients is called the Fourier series of $f$.

The natural question which now arises is whether the Fourier series of $f$ converges to $f$, or more generally, whether $f$ is determined by its Fourier series. That is to say, if we know the Fourier coefficients of a function, can we find the function, and if so, how?

The study of such series, and, in particular, the problem of representing a given function by a trigonometric series, originated in physical problems such as the theory of oscillations and the theory of heat conduction (Fourier's "Théorie analytique de la chaleur" was published in 1822). The many difficult and delicate problems which arouse during this study caused a thorough revision and reformulation of the whole theory of functions of a real variable. Among many prominent names, those of Riemann, Cantor, and Lebesgue are intimately connected with this field, which nowadays, with all its generalizations and ramifications, may well be said to occupy a central position in the whole of analysis.

We shall be content to derive some basic theorems which are easily accessible by the methods developed in the preceding chapters. For more thorough investigations, the Lebesgue integral is a natural and indispensable tool.

We shall first study more general systems of functions which share a property

analogous to (8.61).
8.10 Definition. Let $\left(\phi_{n}\right)(n=1,2,3, \ldots)$ be a sequence of complex functions on $[a, b]$, such that

$$
\int_{a}^{b} \phi_{n}(x) \overline{\phi_{m}(x)} d x=0 \quad(n \neq m)
$$

Then $\left(\phi_{n}\right)$ is said to be an orthogonal system of functions on $[a, b]$. If, in addition,

$$
\int_{a}^{b}\left|\phi_{n}(x)\right|^{2} d x=1
$$

for all $n,\left(\phi_{n}\right)$ is said to be orthonormal.
For example, the functions $(2 \pi)^{-1 / 2} \mathrm{e}^{\mathrm{i} n x}$ form an orthonormal system on $[-\pi, \pi]$. So do the real functions

$$
\frac{1}{\sqrt{2 \pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\cos 2 x}{\sqrt{\pi}}, \frac{\sin 2 x}{\sqrt{\pi}}, \ldots
$$

If $\left(\phi_{n}\right)$ is orthonormal on $[a, b]$ and if

$$
c_{n}=\int_{a}^{b} f(t) \overline{\phi_{n}(t)} d t \quad(n=1,2,3, \ldots)
$$

we call $c_{n}$ the $n$th Fourier coefficient of $f$ relative to $\left(\phi_{n}\right)$. We write

$$
f(x) \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}(x)
$$

and call this series the Fourier series of $f$ (relative to $\left(\phi_{n}\right)$ ).
Note that the symbol $\sim$ used in (8.67) implies nothing about the convergence of the series; it merely says that the coefficients are given by (8.66).

The following theorems show that the partial sums of the Fourier series of $f$ have a certain minimum property. We shall assume here and in the rest of this chapter that $f \in \mathscr{R}$, although this hypothesis can be weakened.
8.11 Theorem. Let $\left(\phi_{n}\right)$ be orthonormal on $[a, b]$. Let

$$
s_{n}(x)=\sum_{m=1}^{n} c_{m} \phi_{m}(x)
$$

be the $n$th partial sum of the Fourier series of $f$, and suppose

$$
t_{n}(x)=\sum_{m=1}^{n} \gamma_{m} \phi_{m}(x)
$$

Then

$$
\int_{a}^{b}\left|f-s_{n}\right|^{2} d x \leq \int_{a}^{b}\left|f-t_{n}\right|^{2} d x
$$

and equality holds if and only if

$$
\gamma_{m}=c_{m} \quad(m=1, \ldots, n)
$$

That is to say, among all functions $t_{n}, s_{n}$ gives the best possible mean square approximation to f .

Proof. Let $\int$ denote the integral over $[a, b], \Sigma$ the sum from 1 to $n$. Then

$$
\int \overline{\mathrm{f}} \overline{\mathrm{t}}_{n}=\int \mathrm{f} \sum \bar{\gamma}_{m} \bar{\phi}_{m}=\sum c_{m} \bar{\gamma}_{m}
$$

by the definition of $\left(c_{m}\right)$,

$$
\int\left|t_{n}\right|^{2}=\int t_{n} \overline{t_{n}}=\int \sum \gamma_{m} \phi_{m} \sum \bar{\gamma}_{k} \bar{\phi}_{k}=\sum\left|\gamma_{m}\right|^{2}
$$

since $\left(\phi_{m}\right)$ is orthonormal, and so

$$
\begin{aligned}
\int\left|f-t_{n}\right|^{2} & =\int|f|^{2}-\int f \bar{t}_{n}-\int \bar{f} t_{n}+\int\left|t_{n}\right|^{2} \\
& =\int|f|^{2}-\sum c_{m} \bar{\gamma}_{m}-\sum \bar{c}_{m} \gamma_{m}+\sum \gamma_{m} \bar{\gamma}_{m} \\
& =\int|f|^{2}-\sum\left|c_{m}\right|^{2}+\sum\left|\gamma_{m}-c_{m}\right|^{2}
\end{aligned}
$$

which is evidently minimized if and only if $\gamma_{m}=c_{m}$.
Putting $\gamma_{m}=c_{m}$ in this calculation, we obtain

$$
\int_{a}^{b}\left|s_{n}(x)\right|^{2} d x=\sum_{m=1}^{n}\left|c_{m}\right|^{2} \leq \int_{a}^{b}|f(x)|^{2} d x
$$

since $\int\left|f-t_{n}\right|^{2} \geq 0$.
8.12 Theorem. If $\left(\phi_{n}\right)$ is orthonormal on $[a, b]$, and if

$$
f(x) \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}(x)
$$

then

$$
\sum_{n=1}^{\infty}\left|c_{n}\right|^{2} \leq \int_{a}^{b}|f(x)|^{2} d x
$$

In particular,

$$
\lim _{n \rightarrow \infty} c_{n}=0
$$

Proof. Letting $n \rightarrow \infty$ in (8.72), we obtain (8.73), the so-called "Bessel inequality."
8.13 Trigonometric series. From now on we shall deal only with the trigonometric system. We shall consider functions $f$ that have period $2 \pi$ and that are Riemannintegrable on $[-\pi, \pi]$ (and hence on every bounded interval). The Fourier series of $f$ is then the series (8.63) whose coefficients $c_{n}$ are given by the integrals (8.62), and

$$
s_{N}(x)=s_{N}(f ; x)=\sum_{n=-N}^{N} c_{n} e^{i n x}
$$

is the Nth partial sum of Fourier series of $f$. The inequality (8.72) now takes the form

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|s_{N}(x)\right|^{2} d x=\sum_{n=-N}^{N}\left|c_{n}\right|^{2} \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi}|f(x)|^{2} d x
$$

In order to obtain an expression for $s_{N}$ that is more manageable than (8.75) we introduce the Dirichlet kernel

$$
D_{N}(x)=\sum_{n=-N}^{N} e^{i n x}=\frac{\sin \left(N+\frac{1}{2}\right) x}{\sin (x / 2)}
$$

The first of these equalities is the definition of $D_{N}(x)$. The second follows if both sides of the identity

$$
\left(e^{i x}-1\right) D_{N}(x)=e^{i(N+1) x}-e^{-i N x}
$$

are multiplied by $\mathrm{e}^{-i x / 2}$.
By (8.62) and (8.75), we have

$$
\begin{aligned}
s_{N}(f ; x) & =\sum_{n=-N}^{N} \frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) e^{-i n t} d t e^{i n x} \\
& =\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) \sum_{n=-N}^{N} e^{i n(x-t)} d t
\end{aligned}
$$

so that

$$
s_{N}(f ; x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) D_{N}(x-t) d t=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-t) D_{N}(t) d t
$$

The periodicity of all functions involved shows that it is immaterial over which interval we integrate, as long as its length is $2 \pi$. This shows that the two integrals in (8.78) are equal.

We shall prove just one theorem about the pointwise convergence of Fourier series.
8.14 Theorem. If, for some $x$, there are constants $\delta>0$ and $M<\infty$ such that

$$
|f(x+t)-f(x)| \leq M|t|
$$

for all $\mathrm{t} \in(-\delta, \delta)$, then

$$
\lim _{N \rightarrow \infty} s_{N}(f ; x)=f(x)
$$

Proof. Define

$$
g(t)=\frac{f(x-t)-f(x)}{\sin (t / 2)}
$$

for $0<|t| \leq \pi$, and put $g(0)=0$. By the definition (8.77),

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} D_{N}(x) d x=1
$$

Hence (8.78) shows that

$$
\begin{aligned}
s_{N}(f ; x) & -f(x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(t) \sin \left(N+\frac{1}{2}\right) t d t \\
& =\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left[g(t) \cos \frac{t}{2}\right] \sin N t d t+\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left[g(t) \sin \frac{t}{2}\right] \cos N t d t
\end{aligned}
$$

By (8.79) and (8.81), $g(t) \cos (t / 2)$ and $g(t) \sin (t / 2)$ are bounded. The last two integrals thus tend to 0 as $\mathrm{N} \rightarrow \infty$, by (8.74). This proves (8.80).

Corollary. If $f(x)=0$ for all $x$ in some segment $J$, then $\lim s_{N}(f ; x)=0$ for every $x \in J$.
Here is another formulation of this corollary:
If $f(t)=g(t)$ for all $t$ in some neighborhood of $x$, then

$$
s_{N}(f ; x)-s_{N}(g ; x)=s_{N}(f-g ; x) \rightarrow 0 \text { as } N \rightarrow \infty
$$

This is usually called the localization theorem. It shows that the behaviour of the sequence $\left(s_{N}(f ; x)\right)$, as far as convergence is concerned, depends only on the values of $f$ in some (arbitrarily small) neighborhood of $x$. Two Fourier series may thus have the same behaviour in one interval, but may behave in entirely different ways in some other interval. We have here a very striking contrast between Fourier series and power series (Theorem 8.5).

We conclude with two other approximation theorems.

8.15 Theorem. If f is continuous (with period $2 \pi$ ) and if $\varepsilon>0$, then there is a trigonometric polynomial P such that

$$
|\mathrm{P}(\mathrm{x})-\mathrm{f}(\mathrm{x})|<\varepsilon
$$

for all real x .
Proof. If we identify x and $\mathrm{x}+2 \pi$, we may regard the $2 \pi$-periodic functions on $\mathbb{R}^{1}$ as functions on the unit circle T , by means of the mapping $\mathrm{x} \rightarrow \mathrm{e}^{\mathrm{ix}}$. The trigonometric polynomials, i.e., the functions of the form (8.60), form a self-adjoint algebra $\mathscr{A}$, which seperates points on T , and which vanishes at no point of T . Since T is compact, Theorem 7.33 tells us that $\mathscr{A}$ is dense in $\mathscr{C}(\mathrm{T})$. This is exactly what the theorem asserts.

A more precise form of this theorem appears in Exercise 8.15.
8.16 Theorem (Parseval's Theorem). Suppose f and g are Riemann-integrable functions with period $2 \pi$, and

$$
f(x) \sim \sum_{n=-\infty}^{\infty} c_{n} e^{i n x}, \quad g(x) \sim \sum_{n=-\infty}^{\infty} \gamma_{n} e^{i n x}
$$

Then

$$
\begin{aligned}
\lim _{N \rightarrow \infty} \frac{1}{2 \pi} \int_{-\pi}^{\pi}|f(x)-s_{N}(f ; x)|^{2} d x & =0 \\
\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) \overline{g(x)} d x & =\sum_{n=-\infty}^{\infty} c_{n} \bar{\gamma}_{n} \\
\frac{1}{2 \pi} \int_{-\pi}^{\pi}|f(x)|^{2} d x & =\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2}
\end{aligned}
$$

Proof. Let us use the notation

$$
\|\mathrm{h}\|_{2}=\left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi}|h(x)|^{2} d x\right\}^{1 / 2}
$$

Let $\varepsilon>0$ be given. Since $f \in \mathscr{R}$ and $f(\pi)=f(-\pi)$, the construction described in Exercise 6.12 yields a continuous $2 \pi$-periodic function h with

$$
\|\mathrm{f}-\mathrm{h}\|_{2}<\varepsilon
$$

By Theorem 8.15, there is a trigonometric polynomial P such that $|h(x)-P(x)|<$ $\varepsilon$ for all x . Hence $\|\mathrm{h}-\mathrm{P}\|_{2}<\varepsilon$. If P has degree $\mathrm{N}_{0}$, Theorem 8.11 shows that

$$
\left\|\mathrm{h}-\mathrm{s}_{\mathrm{N}}(\mathrm{~h})\right\|_{2} \leq\|\mathrm{h}-\mathrm{P}\|_{2}<\varepsilon
$$

for all $\mathrm{N} \geq \mathrm{N}_{0}$. By (8.72), with $\mathrm{h}-\mathrm{f}$ in place of f ,

$$
\left\|s_{N}(h)-s_{N}(f)\right\|_{2}=\left\|s_{N}(h-f)\right\|_{2} \leq\|h-f\|_{2}<\varepsilon
$$

Now the triangle inequality (Exercise 6.11), combined with (8.87), (8.88), and (8.89), shows that

$$
\left\|\mathrm{f}-\mathrm{s}_{\mathrm{N}}(\mathrm{f})\right\|_{2}<3 \varepsilon \quad\left(\mathrm{~N} \geq \mathrm{N}_{0}\right)
$$

This proves (8.83). Next,

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} s_{N}(f) \bar{g} d x=\sum_{n=-N}^{N} c_{n} \frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i n x} \overline{g(x)} d x=\sum_{n=-N}^{N} c_{n} \bar{\gamma}_{n}
$$

and the Schwarz inequality shows that

$$
\left|\int f \bar{g}-\int s_{N}(f) \bar{g}\right| \leq \int\left|f-s_{N}(f)\right||g| \leq\left\{\int\left|f-s_{N}\right|^{2} \int|g|^{2}\right\}^{1 / 2}
$$

which tends to 0 , as $\mathrm{N} \rightarrow \infty$, by (8.83). Comparison of (8.91) and (8.92) gives (8.84). Finally, (8.85) is the special case $g=f$ of (8.84).

A more general version of Theorem 8.16 appears in Chap. 11.

# THE GAMMA FUNCTION 

This function is closely related to factorials and crops up in many unexpected places in analysis. Its origin, history, and development are very well described in an interesting article by P. J. Davis (Amer. Math. Monthly, vol. 66, 1959, pp. 849 -869 [Dav59]). Artin's book [Art64] (cited in the Bibliography) is another good elementary introduction.

Our presentation will be very condensed, with only a few comments after each theorem. This section may thus be regarded as a large exercise, and as an opportunity to apply some of the material that has been presented so far.
8.17 Definition. For $0<x<\infty$,

$$
\Gamma(x)=\int_{0}^{\infty} t^{x-1} e^{-t} d t
$$

The integral converges for these $x$. (When $x<1$, both 0 and $\infty$ have to be looked at.)

### 8.18 Theorem.

(a) The functional equation

$$
\Gamma(x+1)=x \Gamma(x)
$$

holds if $0<\mathrm{x}<\infty$.
(b) $\Gamma(\mathrm{n}+1)=\mathrm{n}$ ! for $\mathrm{n}=1,2,3, \ldots$
(c) $\log \Gamma$ is convex on $(0, \infty)$.

Proof. An integration by parts proves (a). Since $\Gamma(1)=1$, (a) implies (b), by induction. If $1<\mathrm{p}<\infty$ and $(1 / \mathrm{p})+(1 / \mathrm{q})=1$, apply Hölder's inequality (Exercise 6.10) to (8.93), and obtain

$$
\Gamma\left(\frac{x}{p}+\frac{y}{q}\right) \leq \Gamma(x)^{1 / p} \Gamma(y)^{1 / q}
$$

This is equivalent to (c).
It is a rather surprising fact, discovered by Bohr and Mollerup, that these three properties characterize $\Gamma$ completely.
8.19 Theorem. If f is a positive function on $(0, \infty)$ such that
(a) $\mathrm{f}(\mathrm{x}+1)=\mathrm{xf}(\mathrm{x})$,
(b) $\mathrm{f}(1)=1$,
(c) $\log \mathrm{f}$ is convex,
then $\mathrm{f}(\mathrm{x})=\Gamma(\mathrm{x})$.
Proof. Since $\Gamma$ satisfies (a), (b), and (c), it is enough to prove that $f(x)$ is uniquely determined by (a), (b), (c) for all $x>0$. By (a), it is enough to do this for $x \in(0,1)$.

Put $\phi=\log \mathrm{f}$. Then

$$
\phi(\mathrm{x}+1)=\phi(\mathrm{x})+\log \mathrm{x} \quad(0<\mathrm{x}<\infty)
$$

$\phi(1)=0$, and $\phi$ is convex. Suppose $0<x<1$, and $n$ is a positive integer. By (8.94), $\phi(n+1)=\log (n!)$. Consider the difference quotients of $\phi$ on the intervals $[\mathrm{n}, \mathrm{n}+1],[\mathrm{n}+1, \mathrm{n}+1+\mathrm{x}],[\mathrm{n}+1, \mathrm{n}+2]$. Since $\phi$ is convex

$$
\log n \leq \frac{\phi(n+1+x)-\phi(n+1)}{x} \leq \log (n+1)
$$

Repeated application of (8.94) gives

$$
\phi(\mathrm{n}+1+\mathrm{x})=\phi(\mathrm{x})+\log [\mathrm{x}(\mathrm{x}+1) \cdots(\mathrm{x}+\mathrm{n})]
$$

Thus

$$
0 \leq \phi(\mathrm{x})-\log \left[\frac{\mathrm{n!n}^{\mathrm{x}}}{\mathrm{x}(\mathrm{x}+1) \cdots(\mathrm{x}+\mathrm{n})}\right] \leq \mathrm{x} \log \left(1+\frac{1}{\mathrm{n}}\right)
$$

The last expression tends to 0 as $n \rightarrow \infty$. Hence $\phi(x)$ is determined, and the proof is complete.

As a by-product we obtain the relation

$$
\Gamma(x)=\lim _{n \rightarrow \infty} \frac{n!n^{x}}{x(x+1) \cdots(x+n)}
$$

at least when $0<x<1$; from this one can deduce that (8.95) holds for all $x>0$, since $\Gamma(x+1)=x \Gamma(x)$.
8.20 Theorem. If $x>0$ and $y>0$, then

$$
\int_{0}^{1} t^{x-1}(1-t)^{y-1} d t=\frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}
$$

This integral is the so-called beta function $\mathrm{B}(\mathrm{x}, \mathrm{y})$.
Proof. Note that $B(1, y)=1 / y$, that $\log B(x, y)$ is a convex function of $x$, for each fixed $y$, by Hölder's inequality, as in Theorem 8.18, and that

$$
B(x+1, y)=\frac{x}{x+y} B(x, y)
$$

To prove (8.97), perform an integration by parts on

$$
B(x+1, y)=\int_{0}^{1}\left(\frac{t}{1-t}\right)^{x}(1-t)^{x+y-1} d t
$$

These three properties of $B(x, y)$ show, for each $y$, that Theorem 8.19 applies to the function $f$ defined by

$$
f(x)=\frac{\Gamma(x+y)}{\Gamma(y)} B(x, y)
$$

Hence $f(x)=\Gamma(x)$.
8.21 Some consequences. The substitution $t=\sin ^{2} \theta$ turns (8.96) into

$$
2 \int_{0}^{\pi / 2}(\sin \theta)^{2 x-1}(\cos \theta)^{2 y-1} \mathrm{~d} \theta=\frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}
$$

The special case $x=y=1 / 2$ gives

$$
\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}
$$

The substitution $t=s^{2}$ turns (8.93) into

$$
\Gamma(x)=2 \int_{0}^{\infty} s^{2 x-1} e^{-s^{2}} d s \quad(0<x<\infty)
$$

The special case $x=1 / 2$ gives

$$
\int_{-\infty}^{\infty} e^{-s^{2}} d s=\sqrt{\pi}
$$

By (8.99), the identity

$$
\Gamma(x)=\frac{2^{x-1}}{\sqrt{\pi}} \Gamma\left(\frac{x}{2}\right) \Gamma\left(\frac{x+1}{2}\right)
$$

follows directly from Theorem 8.19 .
8.22 Stirling's formula. This provides a simple approximate expression for $\Gamma(x+1)$ when $x$ is large (hence for $n$ ! when $n$ is large). The formula is

$$
\lim _{x \rightarrow \infty} \frac{\Gamma(x+1)}{(x / e)^{x} \sqrt{2 \pi x}}=1
$$

Here is a proof. Put $t=x(1+u)$ in (8.93). This gives

$$
\Gamma(x+1)=x^{x+1} e^{-x} \int_{-1}^{\infty}\left[(1+u) e^{-u}\right]^{x} d u
$$

Determine $h(u)$ so that $h(0)=1$ and

$$
(1+u) e^{-u}=\exp \left[-\frac{u^{2}}{2} h(u)\right]
$$

if $-1<u<\infty, u \neq 0$. Then

$$
h(u)=\frac{2}{u^{2}}[u-\log (1+u)]
$$

It follows that $h$ is continuous, and that $h(u)$ decreases monotonically from $\infty$ to 0 as $u$ increases from -1 to $\infty$.

The substitution $u=s \sqrt{2 / x}$ turns (8.104) into

$$
\Gamma(x+1)=x^{x} e^{-x} \sqrt{2 x} \int_{-\infty}^{\infty} \psi_{x}(s) d s
$$

where

$$
\psi_{x}(s)= \begin{cases}\exp \left[-s^{2} h(s \sqrt{2 / x})\right] & (-\sqrt{x / 2}<s<\infty) \\ 0 & (s \leq-\sqrt{x / 2})\end{cases}
$$

Note the following facts about $\psi_{x}(s)$ :
(a) For every $s, \psi_{x}(s) \rightarrow e^{-s^{2}}$ as $x \rightarrow \infty$.
(b) The convergence in (a) is uniform on $[-A, A]$, for every $A<\infty$.
(c) When $s<0$, then $0<\psi_{x}(s)<e^{-s^{2}}$.
(d) When $s>0$ and $x>1$, then $0<\psi_{x}(s)<\psi_{1}(s)$.

(e) $\int_{0}^{\infty} \psi_{1}(s) d s<\infty$.

The convergence theorem stated in Exercise 7.12 can therefore be applied to the integral (8.107), and shows that this integral converges to $\sqrt{\pi}$ as $x \rightarrow \infty$, by (8.101). This proves (8.103).

A more detailed version of this proof may be found in R. C. Buck's "Advanced Calculus," pp. 216-218 [Buc62a]. For two other, entirely different, proofs, see W. Feller's article in Amer. Math. Monthly, vol. 74, 1967, pp. 1223 -1225 [Fel67] (with a correction in vol. 75, 1968, p. 518 [Fel68]) and pp. 20 -24 of Artin's book [Art64].

Exercise 8.20 gives a simpler proof of a less precise result.

# EXERCISES 

8.1. Define

$$
f(x)= \begin{cases}e^{-1 / x^{2}} & (x \neq 0) \\ 0 & (x=0)\end{cases}
$$

Prove that $f$ has derivatives of all orders at $x=0$ and that $f^{(n)}(0)=0$ for $n=1,2,3, \ldots$
8.2. Let $a_{i j}$ be the number in the $i$ th row and $j$ th column of the array

$$
\begin{array}{cccccc}
-1 & 0 & 0 & 0 & \cdots \\
\frac{1}{2} & -1 & 0 & 0 & \cdots \\
\frac{1}{4} & \frac{1}{2} & -1 & 0 & \cdots \\
\frac{1}{8} & \frac{1}{4} & \frac{1}{2} & -1 & \cdots \\
\cdots & \cdots & \cdots & \cdots & \ddots
\end{array}
$$

so that

$$
a_{i j}= \begin{cases}0 & (i<j) \\ -1 & (i=j) \\ 2^{j-i} & (i>j)\end{cases}
$$

Prove that

$$
\sum_{i} \sum_{j} a_{i j}=-2 \quad \sum_{j} \sum_{i} a_{i j}=0
$$

8.3. Prove that

$$
\sum_{i} \sum_{j} a_{i j}=\sum_{j} \sum_{i} a_{i j}
$$

if $a_{i j} \geq 0$ for all $i$ and $j$ (the case $+\infty=+\infty$ may occur).
8.4. Prove the following limit relations:
(a) $\lim _{x \rightarrow 0} \frac{b^{x}-1}{x}=\log b \quad(b>0)$.
(b) $\lim _{x \rightarrow 0} \frac{\log (1+x)}{x}=1$.
(c) $\lim _{x \rightarrow 0}(1+x)^{1 / x}=e$.
(d) $\lim _{n \rightarrow \infty}\left(1+\frac{x}{n}\right)^{n}=e^{x}$.

8.5. Find the following limits:
(a) $\lim _{x \rightarrow 0} \frac{e-(1+x)^{1 / x}}{x}$.
(b) $\lim _{n \rightarrow \infty} \frac{n}{\log n}\left[n^{1 / n}-1\right]$.
(c) $\lim _{x \rightarrow 0} \frac{\tan x-x}{x(1-\cos x)}$.
(d) $\lim _{x \rightarrow 0} \frac{x-\sin x}{\tan x-x}$.
8.6. Suppose $f(x) f(y)=f(x+y)$ for all real $x$ and $y$.
(a) Assuming that $f$ is differentiable and not zero, prove that

$$
f(x)=e^{c x}
$$

where $c$ is a constant.
(b) Prove the same thing, assuming only that $f$ is continuous.
8.7. If $0<x<\frac{\pi}{2}$, prove that

$$
\frac{2}{\pi}<\frac{\sin x}{x}<1
$$

8.8. For $n=0,1,2, \ldots$ and $x$ real, prove that

$$
|\sin n x| \leq n|\sin x|
$$

Note that this inequality may be false for other values of $n$. For instance,

$$
\left|\sin \frac{1}{2} \pi\right|>\frac{1}{2}|\sin \pi|
$$

8.9 .
(a) Put $s_{N}=1+\left(\frac{1}{2}\right)+\cdots+(1 / N)$. Prove that

$$
\lim _{N \rightarrow \infty}\left(s_{N}-\log N\right)
$$

exists. (The limit, often denoted by $\gamma$, is called Euler's constant. Its numerical value is $0.5772 \ldots$ It is not known whether $\gamma$ is rational or not.)
(b) Roughly how large must $m$ be so that $N=10^{m}$ satisfies $s_{N}>100$ ?
8.10. Prove that $\sum 1 / p$ diverges; the sum extends over all primes.
(This shows that the primes form a fairly substantial subset of the positive integers.)
Hint: Given N , let $\mathrm{p}_{1}, \ldots, \mathrm{p}_{\mathrm{k}}$ be those primes that divide at least one integer $\leq \mathrm{N}$. Then

$$
\begin{aligned}
\sum_{n=1}^{N} \frac{1}{n} & \leq \prod_{j=1}^{k}\left(1+\frac{1}{p_{j}}+\frac{1}{p_{j}^{2}}+\cdots\right) \\
& =\prod_{j=1}^{k}\left(1-\frac{1}{p_{j}}\right)^{-1} \\
& \leq \exp \sum_{j=1}^{k} \frac{2}{p_{j}}
\end{aligned}
$$

The last inequality holds because

$$
(1-x)^{-1} \leq \mathrm{e}^{2 x}
$$

if $0 \leq x \leq \frac{1}{2}$.
(There are many proofs of this result. See, for instance, the article by I. Niven in Amer. Math. Monthly, vol. 78, 1971, pp. 272-273 [Niv71], and the one by R. Bellman in Amer. Math. Monthly, vol. 50, 1943, pp. 318-319 [Bel43].)
8.11. Suppose $f \in \mathscr{R}$ on $[0, A]$ for all $A<\infty$, and $f(x) \rightarrow 1$ as $x \rightarrow+\infty$. Prove that

$$
\lim _{t \rightarrow 0} t \int_{0}^{\infty} e^{-t x} f(x) d x=1 \quad(t>0)
$$

8.12. Suppose $0<\delta<\pi, f(x)=1$ if $|x| \leq \delta, f(x)=0$ if $\delta<|x| \leq \pi$, and $f(x+2 \pi)=f(x)$ for all x .
(a) Compute the Fourier coefficients of $f$.
(b) Conclude that

$$
\sum_{n=1}^{\infty} \frac{\sin (n \delta)}{n}=\frac{\pi-\delta}{2} \quad(0<\delta<\pi)
$$

(c) Deduce from Parseval's theorem that

$$
\sum_{n=1}^{\infty} \frac{\sin ^{2}(n \delta)}{n^{2} \delta}=\frac{\pi-\delta}{2}
$$

(d) Let $\delta \rightarrow 0$ and prove that

$$
\int_{0}^{\infty}\left(\frac{\sin x}{x}\right)^{2} d x=\frac{\pi}{2}
$$

(e) Put $\delta=\pi / 2$ in (c). What do you get?
8.13. Put $f(x)=x$ if $0 \leq x<2 \pi$, and apply Parseval's theorem to conclude that

$$
\sum_{n=1}^{\infty} \frac{1}{n^{2}}=\frac{\pi^{2}}{6}
$$

8.14. If $f(x)=(\pi-|x|)^{2}$ on $[-\pi, \pi]$, prove that

$$
f(x)=\frac{\pi^{2}}{3}+\sum_{n=1}^{\infty} \frac{4}{n^{2}} \cos n x
$$

and deduce that

$$
\sum_{n=1}^{\infty} \frac{1}{n^{2}}=\frac{\pi^{2}}{6}, \quad \sum_{n=1}^{\infty} \frac{1}{n^{4}}=\frac{\pi^{4}}{90}
$$

(A recent article by E. L. Stark contains many references to series of the form $\sum \mathrm{n}^{-\mathrm{s}}$, where $s$ is a positive integer. See Math. Mag., vol. 47, 1947, pp. 197-202.)
8.15. With $D_{n}$ as defined in (8.77), put

$$
\mathrm{K}_{\mathrm{N}}(\mathrm{x})=\frac{1}{\mathrm{~N}+1} \sum_{\mathrm{n}=0}^{\mathrm{N}} \mathrm{D}_{\mathrm{n}}(\mathrm{x})
$$

Prove that

$$
\mathrm{K}_{\mathrm{N}}(\mathrm{x})=\frac{1}{\mathrm{~N}+1} \cdot \frac{1-\cos (\mathrm{N}+1) \mathrm{x}}{1-\cos \mathrm{x}}
$$

and that
(a) $\mathrm{K}_{\mathrm{N}} \geq 0$,
(b) $\frac{1}{2 \pi} \int_{-\pi}^{\pi} \mathrm{K}_{\mathrm{N}}(\mathrm{x}) \mathrm{dx}=1$,
(c) $\mathrm{K}_{\mathrm{N}}(\mathrm{x}) \leq \frac{1}{\mathrm{~N}+1} \cdot \frac{2}{1-\cos \delta}$ if $0<\delta \leq|x| \leq \pi$.

If $s_{N}=s_{N}(f ; x)$ is the Nth partial sum of the Fourier series of $f$, consider the arithmetic means

$$
\sigma_{N}=\frac{s_{0}+s_{1}+\cdots+s_{N}}{N+1}
$$

Prove that

$$
\sigma_{N}(f ; x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x-t) K_{N}(t) d t
$$

and hence prove Fejér's Theorem:
If $f$ is continuous, with period $2 \pi$, then $\sigma_{N}(f ; x) \rightarrow f(x)$ uniformly on $[-\pi, \pi]$.
Hint: Use properties (a), (b), (c) to proceed as in Theorem 7.26.
8.16. Prove a pointwise version of Fejér's Theorem:

If $f \in \mathscr{R}$ and $f(x+), f(x-)$ exist for some $x$, then

$$
\lim _{N \rightarrow \infty} \sigma_{N}(f ; x)=\frac{1}{2}[f(x+)+f(x-)]
$$

8.17. Assume $f$ is bounded and monotonic on $[\pi, \pi]$, with Fourier coefficients $c_{n}$, as given by (8.62).
(a) Use Exercise 6.17 to prove that $\left(n c_{n}\right)$ is a bounded sequence.
(b) Combine (a) with Exercise 8.16 and with Exercise 3.14(e) to conclude that

$$
\lim _{N \rightarrow \infty} s_{N}(f ; x)=\frac{1}{2}[f(x+)+f(x-)]
$$

for every $x$.
(c) Assume only that $f \in \mathscr{R}$ on $[-\pi, \pi]$ and that $f$ is monotonic in some segment $(\alpha, \beta) \subset$ $[-\pi, \pi]$. Prove that the conclusion of (b) holds for every $x \in(\alpha, \beta)$.
(This is an application of the localization theorem.)
8.18. Define

$$
\begin{aligned}
& f(x)=x^{3}-\sin ^{2} x \tan x \\
& g(x)=2 x^{2}-\sin ^{2} x-x \tan x
\end{aligned}
$$

Find out, for each of these two functions, whether it is positive or negative for all $x \in(0, \pi / 2)$, or whether it changes sign. Prove your answer.
8.19. Suppose $f$ is a continuous function on $\mathbb{R}^{1}, f(x+2 \pi)=f(x)$, and $\alpha / \pi$ is irrational. Prove that

$$
\lim _{N \rightarrow \infty} \frac{1}{N} \sum_{n=1}^{N} f(x+n \alpha)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) d t
$$

for every x. Hint: Do it first for $f(x)=e^{i k x}$.
8.20. The following simple computation yields a good approximation to Stirling's formula.

For $m=1,2,3, \ldots$, define

$$
f(x)=(m+1-x) \log m+(x-m) \log (m+1)
$$

if $m \leq x \leq m+1$, and define

$$
g(x)=\frac{x}{m}-1+\log m
$$

if $m-\frac{1}{2} \leq x<m+\frac{1}{2}$. Draw the graphs of $f$ and $g$. Note that $f(x) \leq \log x \leq g(x)$ if $x \geq 1$ and that

$$
\int_{1}^{n} f(x) d x=\log (n!)-\frac{1}{2} \log n>-\frac{1}{8}+\int_{1}^{n} g(x) d x
$$

Integrate $\log x$ over $[1, n]$. Conclude that

$$
\frac{7}{8}<\log (n!)-\left(n+\frac{1}{2}\right) \log n+n<1
$$

for $n=2,3,4, \ldots$ (Note: $\log \sqrt{2 \pi} \sim 0.918$.) Thus

$$
e^{7 / 8}<\frac{n!}{(n / e)^{n} \sqrt{n}}<e
$$

8.21. Let

$$
L_{n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|D_{n}(t)\right| d t \quad(n=1,2,3, \ldots)
$$

Prove that there exists a constant $C>0$ such that

$$
L_{n}>C \log n \quad(n=1,2,3, \ldots)
$$

or, more precisely, that the sequence

$$
\left(L_{n}-\frac{4}{\pi^{2}} \log n\right)
$$

is bounded.
8.22. If $\alpha$ is real and $-1<x<1$, prove Newton's binomial theorem

$$
(1+x)^{\alpha}=1+\sum_{n=1}^{\infty} \frac{\alpha(\alpha-1) \cdots(\alpha-n+1)}{n!} x^{n}
$$

Hint: Denote the right side by $f(x)$. Prove that the series converges. Prove that

$$
(1+x) f^{\prime}(x)=\alpha f(x)
$$

and solve this differential equation.
Show also that

$$
(1-x)^{-\alpha}=\sum_{n=0}^{\infty} \frac{\Gamma(n+\alpha)}{n!\Gamma(\alpha)} x^{n}
$$

if $-1<x<1$ and $\alpha>0$.
8.23. Let $\gamma$ be a continuously differentiable closed curve in the complex plane, with parameter interval $[a, b]$, and assume that $\gamma(t) \neq 0$ for every $t \in[a, b]$. Define the index of $\gamma$ to be

$$
\operatorname{Ind}(\gamma)=\frac{1}{2 \pi i} \int_{a}^{b} \frac{\gamma^{\prime}(t)}{\gamma(t)} d t
$$

Prove that $\operatorname{Ind}(\gamma)$ is always an integer.
Hint: There exists $\phi$ on $[a, b]$ with $\phi^{\prime}=\gamma^{\prime} / \gamma, \phi(\alpha)=0$. Hence $\gamma \exp (-\phi)$ is constant. Since $\gamma(a)=\gamma(b)$ it follows that $\exp \phi(b)=\exp \phi(a)=1$. Note that $\phi(b)=2 \pi i \operatorname{Ind}(\gamma)$.

Compute $\operatorname{Ind}(\gamma)$ when $\gamma(t)=e^{i n t}, a=0, b=2 \pi$.
Explain why $\operatorname{Ind}(\gamma)$ is often called the winding number of $\gamma$ around 0 .

8.24. Let $\gamma$ be as in Exercise 8.23, and assume in addition that the range of $\gamma$ does not intersect the negative real axis. Prove that $\operatorname{Ind}(\gamma)=0$. Hint: For $0 \leq \mathrm{c}<\infty, \operatorname{Ind}(\gamma+\mathrm{c})$ is a continuous integer-valued function of c. Also, $\operatorname{Ind}(\gamma+\mathrm{c}) \rightarrow 0$ as $\mathrm{c} \rightarrow \infty$.
8.25. Suppose $\gamma_{1}$ and $\gamma_{2}$ are curves as in Exercise 8.23, and

$$
\left|\gamma_{1}(t)-\gamma_{2}(t)\right|<\left|\gamma_{1}(t)\right| \quad(a \leq t \leq b)
$$

Prove that $\operatorname{Ind}\left(\gamma_{1}\right)=\operatorname{Ind}\left(\gamma_{2}\right)$.
Hint: Put $\gamma=\gamma_{2} / \gamma_{1}$. Then $|1-\gamma|<1$, hence $\operatorname{Ind}(\gamma)=0$, by Exercise 8.24. Also,

$$
\frac{\gamma^{\prime}}{\gamma}=\frac{\gamma_{2}^{\prime}}{\gamma_{2}}-\frac{\gamma_{1}^{\prime}}{\gamma_{1}}
$$

8.26. Let $\gamma$ be a closed curve in the complex plane (not necessarily differentiable) with parameter interval $[0,2 \pi]$, such that $\gamma(t) \neq 0$ for every $t \in[0,2 \pi]$.

Choose $\delta>0$ so that $|\gamma(t)|>\delta$ for all $t \in[0,2 \pi]$. If $P_{1}$ and $P_{2}$ are trigonometric polynomials such that $\left|P_{j}(t)-\gamma(t)\right|<\delta / 4$ for all $t \in[0,2 \pi]$ (their existence is assured by Theorem 8.15), prove that

$$
\operatorname{Ind}\left(\mathrm{P}_{1}\right)=\operatorname{Ind}\left(\mathrm{P}_{2}\right)
$$

by applying Exercise 8.25 .
Define this common value to be $\operatorname{Ind}(\gamma)$.
Prove that the statements of Exercises 8.24 and 8.25 hold without any differentiability assumption.
8.27. Let $f$ be a continuous complex function defined in the complex plane. Suppose there is a positive integer $n$ and a complex number $c \neq 0$ such that

$$
\lim _{|z| \rightarrow \infty} z^{-n} f(z)=c
$$

Prove that $f(z)=0$ for at least one complex number $z$.
Note that this is a generalization of Theorem 8.8.
Hint: Assume $f(z) \neq 0$ for all $z$, define

$$
\gamma_{r}(t)=f\left(\operatorname{re}^{i t}\right)
$$

for $0 \leq r<\infty, 0 \leq t \leq 2 \pi$, and prove the following statements about the curves $\gamma_{r}$ :
(a) $\operatorname{Ind}\left(\gamma_{0}\right)=0$.
(b) $\operatorname{Ind}\left(\gamma_{r}\right)=n$ for all sufficiently large $r$.
(c) $\operatorname{Ind}\left(\gamma_{r}\right)$ is a continuous function of $r$ on $[0, \infty)$.
[In (b) and (c), use the last part of Exercise 8.26.]
Show that (a), (b), and (c) are contradictory, since $n>0$.
8.28. Let $\overline{\mathrm{D}}$ be the closed unit disc in the complex plane. (Thus $z \in \overline{\mathrm{D}}$ if and only if $|z| \leq 1$.) Let $g$ be a continuous mapping of $\overline{\mathrm{D}}$ into the unit circle T . (Thus, $|g(z)|=1$ for every $z \in \overline{\mathrm{D}}$.)

Prove that $g(z)=-z$ for at least one $z \in T$.
Hint: For $0 \leq r \leq 1,0 \leq t \leq 2 \pi$, put

$$
\gamma_{r}(t)=g\left(\operatorname{re}^{i t}\right)
$$

and put $\psi(t)=\mathrm{e}^{-i t} \gamma_{1}(t)$. If $g(z) \neq-z$ for every $z \in T$, then $\psi(t) \neq-1$ for every $t \in[0,2 \pi]$. Hence $\operatorname{Ind}(\psi)=0$, by Exercises 8.24 and 8.26. It follows that $\operatorname{Ind}\left(\gamma_{1}\right)=1$. But $\operatorname{Ind}\left(\gamma_{0}\right)=0$. Derive a contradiction, as in Exercise 8.27.
8.29. Prove that every continuous mapping $f$ of $\overline{\mathrm{D}}$ into $\overline{\mathrm{D}}$ has a fixed point in $\overline{\mathrm{D}}$.
(This is the 2-dimensional case of Brouwer's fixed-point theorem.)

Hint: Assume $f(z) \neq z$ for every $z \in \overline{\mathrm{D}}$. Associate to each $z \in \overline{\mathrm{D}}$ the point $g(z) \in \mathrm{T}$ which lies on the ray that starts at $f(z)$ and passes through $z$. Then $g$ maps $\overline{\mathrm{D}}$ into $\mathrm{T}, g(z)=z$ if $z \in \mathrm{~T}$, and g is continuous, because

$$
g(z)=z-s(z)[f(z)-z]
$$

where $s(z)$ is the unique nonnegative root of a certain quadratic equation whose coefficients are continuous functions of $f$ and $z$. Apply Exercise 8.28.
8.30. Use Stirling's formula to prove that

$$
\lim _{x \rightarrow \infty} \frac{\Gamma(x+c)}{x^{c} \Gamma(x)}=1
$$

for every real constant c .
8.31. In the proof of Theorem 7.26 it was shown that

$$
\int_{-1}^{1}\left(1-x^{2}\right)^{n} d x \geq \frac{4}{3 \sqrt{n}}
$$

for $n=1,2,3, \ldots$ Use Theorem 8.20 and Exercise 8.30 to show the more precise result

$$
\lim _{n \rightarrow \infty} \sqrt{n} \int_{-1}^{1}\left(1-x^{2}\right)^{n} d x=\sqrt{\pi}
$$

# Chapter 9 

## FUNCTIONS OF SEVERAL VARIABLES

## LINEAR TRANSFORMATIONS

We begin this chapter with a discussion of sets of vectors in euclidean $n$-space $\mathbb{R}^{n}$. The algebraic facts presented here extend without change to finite-dimensional vector spaces over any field of scalars. However, for our purposes it is quite sufficient to stay within the familiar framework provided by the euclidean spaces.

### 9.1 Definition.

(a) A nonempty set $X \subset \mathbb{R}^{n}$ is a vector space if $\mathbf{x}+\mathbf{y} \in X$ and $c \mathbf{x} \in X$ for all $\mathbf{x} \in X$, $\mathbf{y} \in X$, and for all scalars $c$.
(b) If $\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{k}} \in \mathbb{R}^{n}$ and $c_{1}, \ldots, c_{\mathrm{k}}$ are scalars, the vector

$$
c_{1} \mathbf{x}_{1}+\cdots+c_{\mathrm{k}} \mathbf{x}_{\mathrm{k}}
$$

is called a linear combination of $\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{k}}$. If $S \subset \mathbb{R}^{n}$ and if $E$ is the set of all linear combinations of elements of $S$, we say that $S$ spans $E$ or that $E$ is the span of $S$.

Observe that every span is a vector space.
(c) A set consisting of vectors $\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{k}}$ (we shall use the notation $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{k}}\right\}$ for such a set) is said to be independent if the relation $c_{1} \mathbf{x}_{1}+\cdots+c_{k} \mathbf{x}_{k}=0$ implies that $c_{1}=\cdots=c_{k}=0$. Otherwise $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{k}}\right\}$ is said to be dependent.

Observe that no independent set contains the null vector.
(d) If a vector space $X$ contains an independent set of $r$ vectors but contains no independent set of $r+1$ vectors, we say that $X$ has dimension $r$ and write: $\operatorname{dim} X=r$.

The set consisting of 0 alone is a vector space; its dimension is 0 .

(e) An independent subset of a vector space $X$ which spans $X$ is called a basis of X.

Observe that if $B=\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$ is a basis of $X$, then every $\mathbf{x} \in X$ has a unique representation of the form $\mathbf{x}=\Sigma c_{j} \mathbf{x}_{j}$. Such a representation exists since $B$ spans $X$, and it is unique since $B$ is independent. The numbers $c_{1}, \ldots, c_{r}$ are called the coordinates of $\mathbf{x}$ with respect to the basis $B$.

The most familiar example of a basis is the set $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$, where $\mathbf{e}_{j}$ is the vector in $\mathbb{R}^{n}$ whose $j$ th coordinate is 1 and whose other coordinates are all 0 . If $\mathbf{x} \in \mathbb{R}^{n}, \mathbf{x}=\left\{\mathrm{x}_{1}, \ldots, \mathrm{x}_{n}\right\}$, then $\mathbf{x}=\Sigma \mathrm{x}_{\mathrm{j}} \mathbf{e}_{\mathrm{j}}$. We shall call

$$
\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}
$$

the standard basis of $\mathbb{R}^{n}$.
9.2 Theorem. Let $r$ be a positive integer. If a vector space $X$ is spanned by a set of $r$ vectors, then $\operatorname{dim} X \leq r$.

Proof. If this is false, there is a vector space $X$ which contains an independent set $Q=\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{r+1}\right\}$ and which is spanned by a set $S_{0}$ consisting of $r$ vectors.

Suppose $0 \leq i<r$, and suppose a set $S_{i}$ has been constructed which spans $X$ and which consists of all $\mathbf{y}_{j}$ with $1 \leq j \leq i$ plus a certain collection of $r-i$ members of $S_{0}$, say $\mathbf{x}_{1}, \ldots, \mathbf{x}_{r-i}$. (In other words, $S_{i}$ is obtained from $S_{0}$ by replacing $i$ of its elements by members of $Q$, without altering the span.) Since $S_{i}$ spans $X, y_{i+1}$ is in the span of $S_{i}$; hence there are scalars $a_{1}, \ldots, a_{i+1}, b_{1}, \ldots, b_{r-i}$ with $a_{i+1}=1$ such that

$$
\sum_{j=1}^{i+1} a_{j} y_{j}+\sum_{k=1}^{r-i} b_{k} x_{k}=0
$$

if all $b_{k}$ 's were 0 , then independence of $Q$ would force all $a_{j}$ 's to be 0 , a contradiction. It follows that some $\mathbf{x}_{k} \in S_{i}$ is a linear combination of the other members of $T_{i}=S_{i} \cup\left\{y_{i+1}\right\}$. Remove this $\mathbf{x}_{k}$ from $T_{i}$ and call the remaining set $S_{i+1}$. Then $S_{i+1}$ spans the set set as $T_{i}$, namely $X$, so that $S_{i+1}$ has the properties postulated for $S_{i}$ with $i+1$ in place of $i$.

Starting with $S_{0}$, we thus construct sets $S_{1}, \ldots, S_{r}$. The last of these consists of $\mathbf{y}_{1}, \ldots, \mathbf{y}_{r}$ and our construction shows that it spans $X$. But $Q$ is independent; hence $\mathbf{y}_{r+1}$ is not in the span of $S_{r}$. This contradiction establishes the theorem.

Corollary. $\operatorname{dim} \mathbb{R}^{n}=n$.
Proof. Since $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ spans $\mathbb{R}^{n}$, the theorem shows that $\operatorname{dim} \mathbb{R}^{n} \leq n$. Since $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ is independent, $\operatorname{dim} \mathbb{R}^{n} \geq n$.
9.3 Theorem. Suppose $X$ is a vector space and $\operatorname{dim} X=n$.
(a) A set E of n vectors in X spans X if and only if E is independent.
(b) X has a basis, and every basis consists of n vectors.

(c) If $1 \leq \mathrm{r} \leq \mathrm{n}$ and $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{\mathrm{r}}\right\}$ is an independent set in X , then X has a basis containing $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{r}\right\}$.

Proof. Suppose $E=\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$. Since $\operatorname{dim} X=n$, the set $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}, \mathbf{y}\right\}$ is dependent for every $\mathbf{y} \in X$. If $E$ is independent, it follows that $\mathbf{y}$ is in the span of $E$; hence $E$ spans $X$. Conversely, if $E$ is independent, one of its members can be removed without changing the span of E. Hence E cannot span X, by Theorem 9.2. This proves (a).

Since $\operatorname{dim} X=n, X$ contains an independent set of $n$ vectors, and (a) shows that every such set is a basis of $X$; (b) now follows from Definition 9.1(d) and Theorem 9.2.

To prove (c), let $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$ be a basis of $X$. The set

$$
S=\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{r}, \mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}
$$

spans $X$ and is dependent since it contains more than $n$ vectors. The argument used in the proof of Theorem 9.2 shows that one of the $\mathbf{x}_{i}$ 's is a linear combination of the other members of $S$. If we remove this $\mathbf{x}_{i}$ from $S$, the remaining set still spans $X$. This process can be repeated $r$ times and leads to a basis of $X$ which contains $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{r}\right\}$, by (a).
9.4 Definitions. A mapping $A$ of a vector space $X$ into a vector space $Y$ is said to be a linear transformation if

$$
A\left(x_{1}+x_{2}\right)=A x_{1}+A x_{2}, \quad A(c x)=c A x
$$

for all $\mathbf{x}, \mathbf{x}_{1}, \mathbf{x}_{2} \in X$ and all scalars c. Note that one often writes $A \mathbf{x}$ instead of $A(\mathbf{x})$ if $A$ is linear.

Observe that $A 0=0$ if $A$ is linear. Observe also that a linear transformation $A$ of $X$ into $Y$ is completely determined by its action on any basis: If $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$ is a basis of $X$, then every $x \in X$ has a unique representation of the form

$$
\mathbf{x}=\sum_{i=1}^{n} c_{i} \mathbf{x}_{i}
$$

and the linearity of $A$ allows us to compute $A \mathbf{x}$ from the vectors $A \mathbf{x}_{1}, \ldots, A \mathbf{x}_{n}$ and the coordinates $c_{1}, \ldots, c_{n}$ by the formula

$$
A \mathbf{x}=\sum_{i=1}^{n} c_{i} A \mathbf{x}_{i}
$$

Linear transformations of $X$ into $X$ are often called linear operators on $X$. If $A$ is a linear operator on $X$ which (i) is one-to-one and (ii) maps $X$ onto $X$, we say that $A$ is invertible. In this case we can define an operator $A^{-1}$ on $X$ by requiring that

$A^{-1}(A x)=x$ for all $x \in X$. It is trivial to verify that we then also have $A\left(A^{-1} x\right)=x$ for all $x \in X$, and that $A^{-1}$ is linear.

An important fact about linear operators on finite dimensional vector spaces is that each of the above conditions (i) and (ii) implies the other:
9.5 Theorem. A linear operator A on a finite-dimensional vector space X is one-to-one if and only if the range of $A$ is all of $X$.

Proof. Let $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$ be a basis of $X$. Then linearity of $A$ shows that its range $\mathscr{R}(\mathrm{A})$ is the span of the set $\mathrm{Q}=\left\{\mathrm{A} \mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$. We therefore infer from Theorem 9.3(a) that $\mathscr{R}(\mathrm{A})=\mathrm{X}$ if and only if Q is independent. We have to prove that this happens if and only if $A$ is one-to-one.

Suppose $A$ is one-to-one and $\Sigma c_{i} A x_{i}=0$. Then $A\left(\Sigma c_{i} x_{i}\right)=0$, hence $\Sigma c_{i} x_{i}=0$, hence $c_{1}=\cdots=c_{n}=0$ and we conclude that $Q$ is independent.

Conversely, suppose $Q$ is independent and $A\left(\Sigma c_{i} x_{i}\right)=0$. Then $\Sigma c_{i} A x_{i}=0$, hence $c_{1}=\cdots=c_{n}=0$ and we conclude: $A \mathbf{x}=\mathbf{0}$ if and only if $\mathbf{x}=\mathbf{0}$. If now $A x=A y$, then $A(x-y)=A x-A y=0$, so that $x-y=0$, and this says that $A$ is one-to-one.

# 9.6 Definitions. 

(a) Let $L(X, Y)$ be the set of all linear transformations of the vector space $X$ into the vector space $Y$. Instead of $L(X, X)$, we shall simply write $L(X)$. If $A_{1}, A_{2} \in$ $L(X, Y)$ and if $c_{1}$ and $c_{2}$ are scalars, define $c_{1} A_{1}+c_{2} A_{2}$ by

$$
\left(c_{1} A_{1}+c_{2} A_{2}\right) \mathbf{x}=c_{1} A_{1} \mathbf{x}+c_{2} A_{2} \mathbf{x} \quad(\mathbf{x} \in \mathrm{X})
$$

It is then clear that $c_{1} A_{1}+c_{2} A_{2} \in L(X, Y)$.
(b) If $X, Y, Z$ are vector spaces, and if $A \in L(X, Y)$ and $B \in L(Y, Z)$, we define their product BA to be the composition of $A$ and $B$ :

$$
(B A) x=B(A x) \quad(x \in X)
$$

Then $B A \in L(X, Z)$. Note that $B A$ need not be the same as $A B$, even if $X=$ $Y=Z$.
(c) For $A \in L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$, define the norm $\|A\|$ of $A$ to be the sup of all numbers $|A \mathbf{x}|$, where $\mathbf{x}$ ranges over all vectors in $\mathbb{R}^{n}$ with $|x| \leq 1$.

Observe that the inequality

$$
|A \mathbf{x}| \leq\|A\||x|
$$

holds for all $\mathbf{x} \in \mathbb{R}^{n}$. Also, if $\lambda$ is such that $|A \mathbf{x}| \leq \lambda|\mathbf{x}|$ for all $\mathbf{x} \in \mathbb{R}^{n}$, then $\|A\| \leq \lambda$.

# 9.7 Theorem. 

(a) If $\mathrm{A} \in \mathrm{L}\left(\mathbb{R}^{\mathrm{n}}, \mathbb{R}^{\mathrm{m}}\right)$, then $\|\mathrm{A}\|<\infty$ and A is a uniformly continuous mapping of $\mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{m}}$.
(b) If $\mathrm{A}, \mathrm{B} \in \mathrm{L}\left(\mathbb{R}^{\mathrm{n}}, \mathbb{R}^{\mathrm{m}}\right)$ and c is a scalar, then

$$
\|\mathrm{A}+\mathrm{B}\| \leq\|\mathrm{A}\|+\|\mathrm{B}\|, \quad\|\mathrm{cA}\|=|\mathrm{c}|\|\mathrm{A}\|
$$

With the distance between A and B defined as $\|\mathrm{A}-\mathrm{B}\|, \mathrm{L}\left(\mathbb{R}^{\mathrm{n}}, \mathbb{R}^{\mathrm{m}}\right)$ is a metric space.
(c) If $\mathrm{A} \in \mathrm{L}\left(\mathbb{R}^{\mathrm{n}}, \mathbb{R}^{\mathrm{m}}\right)$ and $\mathrm{B} \in \mathrm{L}\left(\mathbb{R}^{\mathrm{m}}, \mathbb{R}^{\mathrm{k}}\right)$, then

$$
\|\mathrm{BA}\| \leq\|\mathrm{B}\|\|\mathrm{A}\|
$$

Proof.
(a) Let $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ be the standard basis in $\mathbb{R}^{n}$ and suppose $\mathbf{x}=\Sigma \mathrm{c}_{\mathrm{i}} \mathbf{e}_{\mathrm{i}}$ and $|\mathbf{x}| \leq 1$, so that $\left|c_{i}\right| \leq 1$ for $i=1, \ldots, n$. Then

$$
|A \mathbf{x}|=\left|\sum c_{i} A \mathbf{e}_{i}\right| \leq \sum\left|c_{i}\right|\left|A \mathbf{e}_{i}\right| \leq \sum\left|A \mathbf{e}_{i}\right|
$$

so that

$$
\|\mathrm{A}\| \leq \sum_{i=1}^{n}\left|\mathrm{~A} \mathbf{e}_{\mathrm{i}}\right|<\infty
$$

Since $|A \mathbf{x}-A \mathbf{y}| \leq\|\mathrm{A}\||\mathbf{x}-\mathbf{y}|$ if $\mathbf{x}, \mathbf{y} \in \mathbb{R}^{\mathrm{n}}$, we see that A is uniformly continuous.
(b) The inequality in (b) follows from

$$
|(\mathrm{A}+\mathrm{B}) \mathbf{x}|=|A \mathbf{x}+\mathrm{B} \mathbf{x}| \leq|A \mathbf{x}|+|\mathrm{B} \mathbf{x}| \leq(\|\mathrm{A}\|+\|\mathrm{B}\|)|\mathbf{x}|
$$

The second part of (b) is proved in the same manner. If

$$
\mathrm{A}, \mathrm{~B}, \mathrm{C} \in \mathrm{~L}\left(\mathbb{R}^{\mathrm{n}}, \mathbb{R}^{\mathrm{m}}\right)
$$

we have the triangle inequality

$$
\|\mathrm{A}-\mathrm{C}\|=\|(\mathrm{A}-\mathrm{B})+(\mathrm{B}-\mathrm{C})\| \leq\|\mathrm{A}-\mathrm{B}\|+\|\mathrm{B}-\mathrm{C}\|
$$

and it is easily verified that $\|A-B\|$ has the other properties of a metric (Definition 2.15).
(c) Finally, (c) follows from

$$
|(\mathrm{BA}) \mathbf{x}|=|\mathrm{B}(\mathrm{~A} \mathbf{x})| \leq\|\mathrm{B}\||\mathrm{Ax}| \leq\|\mathrm{B}\|\|\mathrm{A}\||\mathbf{x}|
$$

Since we now have metrics in the spaces $L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$, the concepts of open set, continuity, etc., make sense for these spaces. Our next theorem utilizes these concepts.
9.8 Theorem. Let $\Omega$ be the set of all invertible linear operators on $\mathbb{R}^{n}$,
(a) If $\mathrm{A} \in \Omega, \mathrm{B} \in \mathrm{L}\left(\mathbb{R}^{n}\right)$, and

$$
\|\mathrm{B}-\mathrm{A}\|\left\|\mathrm{A}^{-1}\right\|<1
$$

then $\mathrm{B} \in \Omega$.
(b) $\Omega$ is an open subset of $\mathrm{L}\left(\mathbb{R}^{n}\right)$ and the mapping $\mathrm{A} \mapsto \mathrm{A}^{-1}$ is continuous on $\Omega$. (This mapping is also obviously a 1-1 mapping of $\Omega$ onto $\Omega$ which is its own inverse.)

Proof.
(a) Put $\left\|\mathrm{A}^{-1}\right\|=1 / \alpha$, put $\|\mathrm{B}-\mathrm{A}\|=\beta$. Then $\beta<\alpha$. For every $\mathbf{x} \in \mathbb{R}^{n}$,

$$
\begin{aligned}
\alpha|\mathbf{x}| & =\alpha\left|\mathrm{A}^{-1} \mathrm{~A} \mathbf{x}\right| \leq \alpha\left\|\mathrm{~A}^{-1}\right\||A \mathbf{x}| \\
& =|\mathrm{Ax}| \leq|(\mathrm{A}-\mathrm{B}) \mathbf{x}|+|\mathrm{Bx}| \leq \beta|\mathbf{x}|+|\mathrm{Bx}|
\end{aligned}
$$

so that

$$
(\alpha-\beta)|\mathbf{x}| \leq|\mathrm{Bx}| \quad\left(\mathbf{x} \in \mathbb{R}^{n}\right)
$$

Since $\alpha-\beta>0$, (9.1) shows that $B \mathbf{x} \neq \mathbf{0}$ if $\mathbf{x} \neq \mathbf{0}$. Hence $B$ is 1-1. By Theorem 9.5, $\mathrm{B} \in \Omega$. This holds for all B with $\|\mathrm{B}-\mathrm{A}\|<\alpha$. Thus we have (a) and the fact that $\Omega$ is open.
(b) Next, replace $\mathbf{x}$ by $\mathrm{B}^{-1} \mathbf{y}$ in (9.1). The resulting inequality

$$
(\alpha-\beta)\left|\mathrm{B}^{-1} \mathbf{y}\right| \leq\left|\mathrm{BB}^{-1} \mathbf{y}\right|=|\mathbf{y}| \quad\left(\mathbf{y} \in \mathbb{R}^{n}\right)
$$

shows that $\left\|\mathrm{B}^{-1}\right\| \leq(\alpha-\beta)^{-1}$. The identity

$$
\mathrm{B}^{-1}-\mathrm{A}^{-1}=\mathrm{B}^{-1}(\mathrm{~A}-\mathrm{B}) \mathrm{A}^{-1}
$$

combined with Theorem 9.7(c), implies therefore that

$$
\left\|\mathrm{B}^{-1}-\mathrm{A}^{-1}\right\| \leq\left\|\mathrm{B}^{-1}\right\|\|\mathrm{A}-\mathrm{B}\|\left\|\mathrm{~A}^{-1}\right\| \leq \frac{\beta}{\alpha(\alpha-\beta)}
$$

This establishes the continuity assertion made in (b), since $\beta \rightarrow 0$ as $\mathrm{B} \rightarrow \mathrm{A}$.

9.9 Matrices. Suppose $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$ and $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{m}\right\}$ are bases of vector spaces $X$ and $Y$, respectively. Then every $A \in L(X, Y)$ determines a set of numbers $a_{i j}$ such that

$$
A \mathbf{x}_{j}=\sum_{i=1}^{m} a_{i j} \mathbf{y}_{i} \quad(1 \leq j \leq n)
$$

It is convenient to visualize these numbers in a rectangular array of $m$ rows and $n$ columns, called an $m$ by $n$ matrix:

$$
[A]=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]
$$

Observe that the coordinates $a_{i j}$ of the vector $A \mathbf{x}_{j}$ (with respect to the basis $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{m}\right\}$ ) appear in the jth column of $[A]$. The vectors $A \mathbf{x}_{j}$ are therefore sometimes called the column vectors of $[A]$. With this terminology, the range of $A$ is spanned by the column vectors $[A]$.

If $\mathbf{x}=\Sigma c_{j} \mathbf{x}_{j}$, the linearity of $A$ combined with (9.3) shows that

$$
A \mathbf{x}=\sum_{i=1}^{m}\left(\sum_{j=1}^{n} a_{i j} c_{j}\right) \mathbf{y}_{i}
$$

Thus the coordinates of $A \mathbf{x}$ are $\Sigma_{j} a_{i j} c_{j}$. Note that in (9.3) the summation ranges over the first subscript of $a_{i j}$, but that we sum over the second subscript when computing coordinates.

Suppose next that an $m$ by $n$ matrix is given, with real entries $a_{i j}$. If $A$ is then defined by (9.4), it is clear that $A \in L(X, Y)$ and that $[A]$ is the given matrix. Thus there is a natural 1-1 correspondence between $L(X, Y)$ and the set of all real $m$ by $n$ matrices. We emphasize, though, that $[A]$ depends not only on $A$ but also on the choice of bases in $X$ and $Y$. The same $A$ may give rise to many different matrices if we change bases, and vice versa. We shall not pursue this observation any further, since we shall usually work with fixed bases. (Some remarks on this may be found in Remark 9.37.)

If $Z$ is a third vector space with basis $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{p}\right\}$, if $A$ is given by (9.3), and if

$$
B \mathbf{y}_{i}=\sum_{k} b_{k i} \mathbf{z}_{k}, \quad(B A) \mathbf{x}_{j}=\sum_{k} c_{k j} \mathbf{z}_{k}
$$

then $A \in L(X, Y), B \in L(Y, Z), B A \in L(X, Z)$.

Since

$$
\begin{aligned}
B\left(A \mathbf{x}_{i}\right) & =B\left(\sum_{i} a_{i j} \mathbf{y}_{i}\right)=\sum_{i} a_{i j} B \mathbf{y}_{i} \\
& =\sum_{i} a_{i j} \sum_{k} b_{k i} \mathbf{z}_{k}=\sum_{k}\left(\sum_{i} b_{k i} a_{i j}\right) \mathbf{z}_{k}
\end{aligned}
$$

the independence of $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{p}\right\}$ implies that

$$
c_{k j}=\sum_{i} b_{k i} a_{i j} \quad(1 \leq k \leq p, 1 \leq j \leq n)
$$

This shows how to compute the $p$ by $n$ matrix $[B A]$ from $[B]$ and $[A]$. If we define the product $[B][A]$ to be $[B A]$, then (9.5) describes the usual rule of matrix multiplication.

Finally, suppose $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right\}$ and $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{m}\right\}$ are standard bases of $\mathbb{R}^{n}$ and $\mathbb{R}^{m}$ and $A$ is given by (9.4). The Schwarz inequality shows that

$$
|A \mathbf{x}|^{2}=\sum_{i}\left(\sum_{j} a_{i j} c_{j}\right)^{2} \leq \sum_{i}\left(\sum_{j} a_{i j}^{2} \cdot \sum_{j} c_{j}^{2}\right)=\sum_{i, j} a_{i j}^{2}|\mathbf{x}|^{2}
$$

Thus

$$
\|A\| \leq\left\{\sum_{i, j} a_{i j}^{2}\right\}^{1 / 2}
$$

If we apply (9.6) to $B-A$ in place of $A$, where $A, B \in L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$, we see that if the matrix elements $a_{i j}$ are continuous functions of a parameter, then the same is true of $A$. More precisely:

If $S$ is a metric space, if $a_{11}, \ldots, a_{m n}$ are real continuous functions on $S$, and if, for each $\mathrm{p} \in \mathrm{S}, \mathrm{A}_{\mathrm{p}}$ is the linear transformation of $\mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{m}}$ whose matrix has entries $a_{i j}(p)$, then the mapping $p \rightarrow A_{p}$ is a continuous mapping of $S$ into $L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$.

# DIFFERENTIATION 

9.10 Preliminaries. In order to arrive at a definition of the derivative of a function whose domain is $\mathbb{R}^{n}$ (or an open subset of $\mathbb{R}^{n}$ ), let us take another look at the familiar case $n=1$, and let us see how to interpret the derivative in that case in a way which will naturally extend to $n>1$.

If $f$ is a real function with domain $(a, b) \subset \mathbb{R}^{1}$ and if $x \in(a, b)$, then $f^{\prime}(x)$ is

usually defined to be the real number

$$
\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}
$$

provided, of course, that this limit exists. Thus

$$
f(x+h)-f(x)=f^{\prime}(x) h+r(h)
$$

where the "remainder" $r(h)$ is small, in the sense that

$$
\lim _{h \rightarrow 0} \frac{r(h)}{h}=0
$$

Note that (9.8) expressed the difference $f(x+h)-f(x)$ as the sum of a linear function that takes $h$ to $f^{\prime}(x) h$, plus a small remainder. We can therefore regard the derivative of $f$ at $x$, not as a real number, but as the linear operator on $\mathbb{R}^{1}$ that takes $h$ to $f^{\prime}(x) h$.
[Observe that every real number $\alpha$ gives rise to a linear operator $\mathbb{R}^{1}$; the operator in question is simply multiplication by $\alpha$. Conversely, every linear function that carries $\mathbb{R}^{1}$ to $\mathbb{R}^{1}$ is multiplication by some real number. It is this natural 1-1 correspondence between $\mathbb{R}^{1}$ and $L\left(\mathbb{R}^{1}\right)$ which motivates the preceding statements.]

Let us next consider a function $\mathbf{f}$ that maps $(a, b) \subset \mathbb{R}^{1}$ into $\mathbb{R}^{m}$. In that case, $\mathbf{f}^{\prime}(x)$ was defined to be the vector $\mathbf{y} \in \mathbb{R}^{m}$ (if there is one) for which

$$
\lim _{h \rightarrow 0}\left\{\frac{f(x+h)-f(x)}{h}-y\right\}=0
$$

We can again rewrite this in the form

$$
\mathbf{f}(\mathrm{x}+\mathrm{h})-\mathbf{f}(\mathrm{x})=\mathrm{h} \mathbf{y}+\mathbf{r}(\mathrm{h})
$$

where $\mathbf{r}(h) / h \rightarrow 0$ as $h \rightarrow 0$. The main term on the right side of (9.11) is again a linear function of $h$. Every $y \in \mathbb{R}^{m}$ induces a linear transformation of $\mathbb{R}^{1}$ into $\mathbb{R}^{m}$, by associating to each $h \in \mathbb{R}^{1}$ the vector $h y \in \mathbb{R}^{m}$. This identification of $\mathbb{R}^{m}$ with $\mathrm{L}\left(\mathbb{R}^{1}, \mathbb{R}^{m}\right)$ allows us to regard $f^{\prime}(x)$ as a member of $L\left(\mathbb{R}^{1}, \mathbb{R}^{m}\right)$.

Thus, if $\mathbf{f}$ is a differentiable mapping of $(a, b) \subset \mathbb{R}^{1}$ into $\mathbb{R}^{m}$, and if $x \in(a, b)$, then $\mathbf{f}^{\prime}(x)$ is the linear transformation of $\mathbb{R}^{1}$ into $\mathbb{R}^{m}$ that satisfies

$$
\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)-f^{\prime}(x) h}{h}=0
$$

or, equivalently,

$$
\lim _{h \rightarrow 0} \frac{\left|f(x+h)-f(x)-f^{\prime}(x) h\right|}{|h|}=0
$$

We are now ready for the case $n>1$.

9.11 Definition. Suppose $E$ is an open set in $\mathbb{R}^{n}$, $\mathbf{f}$ maps $E$ into $\mathbb{R}^{m}$, and $\mathbf{x} \in E$. If there exists a linear transformation of $A$ of $\mathbb{R}^{n}$ into $\mathbb{R}^{m}$ such that

$$
\lim _{\mathbf{h} \rightarrow 0} \frac{|\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-A \mathbf{h}|}{|\mathbf{h}|}=0
$$

then we say that $\mathbf{f}$ is differentiable at $\mathbf{x}$ and we write

$$
\mathbf{f}^{\prime}(\mathbf{x})=A
$$

If $\mathbf{f}$ is differentiable at every $\mathbf{x} \in \mathrm{E}$, we say that $\mathbf{f}$ is differentiable in E .
It is of course understood in (9.14) that $\mathbf{h} \in \mathbb{R}^{n}$. If $|\mathbf{h}|$ is small enough, then $\mathbf{x}+\mathbf{h} \in \mathrm{E}$, since E is open. Thus $\mathbf{f}(\mathbf{x}+\mathbf{h})$ is defined, $\mathbf{f}(\mathbf{x}+\mathbf{h}) \in \mathbb{R}^{m}$, and since $A \in L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right), A \mathbf{h} \in \mathbb{R}^{m}$. Thus

$$
\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-A \mathbf{h} \in \mathbb{R}^{m}
$$

The norm in the numerator of (9.14) is that of $\mathbb{R}^{m}$. In the denominator we have the $\mathbb{R}^{n}$-norm of $\mathbf{h}$.

There is an obvious uniqueness problem that has to be settled before we go any further.
9.12 Theorem. Suppose E and $\mathbf{f}$ are as in Definition 9.11, $\mathbf{x} \in \mathrm{E}$, and (9.14) holds with $A=A_{1}$ and with $A=A_{2}$. Then $A_{1}=A_{2}$.

Proof. If $B=A_{1}-A_{2}$, the inequality

$$
|\mathrm{Bh}| \leq|\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-A_{1} \mathbf{h}|+|\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-A_{2} \mathbf{h}|
$$

shows that $|\mathrm{Bh}| /|\mathbf{h}| \rightarrow 0$ as $\mathbf{h} \rightarrow \mathbf{0}$. For any fixed $\mathbf{h} \neq \mathbf{0}$, it follows that

$$
\frac{|\mathrm{B}[\mathbf{t h}]|}{|\mathbf{t h}|} \rightarrow 0 \quad \text { as } \quad \mathrm{t} \rightarrow 0
$$

The linearity of $B$ shows that the left side of (9.16) is independent of $t$. Thus $B \mathbf{h}=\mathbf{0}$ for every $\mathbf{h} \in \mathbb{R}^{n}$. Hence $B=0$.

# 9.13 Remarks. 

(a) The relation (9.14) can be written in the form

$$
\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})=\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{h}+\mathbf{r}(\mathbf{h})
$$

where the remainder $\mathbf{r}(\mathbf{h})$ satisfies

$$
\lim _{\mathbf{h} \rightarrow 0} \frac{|\mathbf{r}(\mathbf{h})|}{|\mathbf{h}|}=0
$$

We may interpret (9.17), as in Theorem 9.10, by saying that for fixed $\mathbf{x}$ and small $\mathbf{h}$, the left side of (9.17) is approximately equal to $\mathbf{f}^{\prime}(\mathbf{h})$, that is, to the value of a linear transformation applied to $\mathbf{h}$.
(b) Suppose $\mathbf{f}$ and $E$ are as in Definition 9.11 and $\mathbf{f}$ is differentiable in E. For every $\mathbf{x} \in \mathrm{E}, \mathbf{f}^{\prime}(\mathbf{x})$ is then a function, namely, a linear transformation of $\mathbb{R}^{n}$ into $\mathbb{R}^{m}$. But $\mathbf{f}^{\prime}$ is also a function: $\mathbf{f}^{\prime}$ maps $E$ into $L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$.
(c) A glance at (9.17) shows that $\mathbf{f}$ is continuous at any point at which $\mathbf{f}$ is differentiable.
(d) The derivative defined by (9.14) or (9.17) is often called the differential of $\mathbf{f}$ at $\mathbf{x}$, or the total derivative of $\mathbf{f}$ at $\mathbf{x}$, to distinguish it from the partial derivatives that will occur later.
9.14 Example. We have defined derivatives of functions carrying $\mathbb{R}^{n}$ to $\mathbb{R}^{m}$ to be linear transformations of $\mathbb{R}^{n}$ into $\mathbb{R}^{m}$. What is the derivative of such a linear transformation? The answer is very simple: If $A \in L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$ and if $\mathbf{x} \in \mathbb{R}^{n}$, then

$$
A^{\prime}(\mathbf{x})=A
$$

Note that $\mathbf{x}$ appears on the left side of (9.19) but not on the right. Both sides of (9.19) are members of $L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$, whereas $A \mathbf{x} \in \mathbb{R}^{m}$.

The proof of (9.19) is a triviality, since

$$
A(\mathbf{x}+\mathbf{h})-A \mathbf{x}=A \mathbf{h}
$$

by the linearity of $A$. With $\mathbf{f}(\mathbf{x})=A \mathbf{x}$, the numerator in (9.14) is thus 0 for every $\mathbf{h} \in \mathbb{R}^{n}$. In (9.17), $\mathbf{r}(\mathbf{h})=\mathbf{0}$.

We now extend the chain rule (Theorem 5.5) to the present situation.
9.15 Theorem. Suppose $E$ is an open set in $\mathbb{R}^{n}$, $\mathbf{f}$ maps $E$ into $\mathbb{R}^{m}, \mathbf{f}$ is differentiable at $\mathbf{x}_{0} \in \mathrm{E}, \mathbf{g}$ maps an open set containing $\mathbf{f}(\mathrm{E})$ into $\mathbb{R}^{\mathrm{k}}$, and $\mathbf{g}$ is differentiable at $\mathbf{f}\left(\mathbf{x}_{0}\right)$. Then the mapping $\mathbf{F}$ of $E$ into $\mathbb{R}^{\mathrm{k}}$ defined by

$$
\mathbf{F}(\mathbf{x})=\mathbf{g}(\mathbf{f}(\mathbf{x}))
$$

is differentiable at $\mathbf{x}_{0}$, and

$$
\mathbf{F}^{\prime}\left(\mathbf{x}_{0}\right)=\mathbf{g}^{\prime}\left(\mathbf{f}\left(\mathbf{x}_{0}\right)\right) \mathbf{f}^{\prime}\left(\mathbf{x}_{0}\right)
$$

On the right side of (9.21), we have the product of two linear transformations, as defined in Definition 9.6.

Proof. Put $\mathbf{y}_{0}=\mathbf{f}\left(\mathbf{x}_{0}\right), A=\mathbf{f}^{\prime}\left(\mathbf{x}_{0}\right), B=\mathbf{g}^{\prime}\left(\mathbf{y}_{0}\right)$, and define

$$
\begin{aligned}
& \mathbf{u}(\mathbf{h})=\mathbf{f}\left(\mathbf{x}_{0}+\mathbf{h}\right)-\mathbf{f}\left(\mathbf{x}_{0}\right)-A \mathbf{h} \\
& \mathbf{v}(\mathbf{k})=\mathbf{g}\left(\mathbf{y}_{0}+\mathbf{k}\right)-\mathbf{g}\left(\mathbf{y}_{0}\right)-B \mathbf{k}
\end{aligned}
$$

for all $\mathbf{h} \in \mathbb{R}^{n}$ and $\mathbf{k} \in \mathbb{R}^{m}$ for which $\mathbf{f}\left(\mathbf{x}_{0}+\mathbf{h}\right)$ and $\mathbf{g}\left(\mathbf{y}_{0}+\mathbf{k}\right)$ are defined. Then

$$
|\mathbf{u}(\mathbf{h})|=\varepsilon(\mathbf{h})|\mathbf{h}|, \quad|\mathbf{v}(\mathbf{k})|=\eta(\mathbf{k})|\mathbf{k}|
$$

where $\varepsilon(\mathbf{h}) \rightarrow 0$ as $\mathbf{h} \rightarrow \mathbf{0}$ and $\eta(\mathbf{k}) \rightarrow 0$ as $\mathbf{k} \rightarrow \mathbf{0}$.
Given $\mathbf{h}$, put $\mathbf{k}=\mathbf{f}\left(\mathbf{x}_{0}+\mathbf{h}\right)-\mathbf{f}\left(\mathbf{x}_{0}\right)$. Then

$$
|\mathbf{k}|=|\mathrm{A} \mathbf{h}+\mathbf{u}(\mathbf{h})| \leq[\|\mathrm{A}\|+\varepsilon(\mathbf{h})]|\mathbf{h}|
$$

and

$$
\begin{aligned}
\mathbf{F}\left(\mathbf{x}_{0}+\mathbf{h}\right)-\mathbf{F}\left(\mathbf{x}_{0}\right)-\mathrm{BAh} & =\mathbf{g}\left(\mathbf{y}_{0}+\mathbf{k}\right)-\mathbf{g}\left(\mathbf{y}_{0}\right)-\mathrm{BAh} \\
& =\mathrm{B}(\mathbf{k}-\mathrm{Ah})+\mathbf{v}(\mathbf{k}) \\
& =\mathrm{B} \mathbf{u}(\mathbf{h})+\mathbf{v}(\mathbf{k})
\end{aligned}
$$

Hence (9.22) and (9.23) imply, for $\mathbf{h} \neq \mathbf{0}$, that

$$
\frac{\left|\mathbf{F}\left(\mathbf{x}_{0}+\mathbf{h}\right)-\mathbf{F}\left(\mathbf{x}_{0}\right)-\mathrm{BAh}\right|}{|\mathbf{h}|} \leq\|\mathrm{B}\| \varepsilon(\mathbf{h})+[\|\mathrm{A}\|+\varepsilon(\mathbf{h})] \eta(\mathbf{k})
$$

Let $\mathbf{h} \rightarrow \mathbf{0}$. Then $\varepsilon(\mathbf{h}) \rightarrow 0$. Also $\mathbf{k} \rightarrow \mathbf{0}$, by (9.23), so that $\eta(\mathbf{k}) \rightarrow 0$. It follows that $\mathbf{F}^{\prime}\left(\mathbf{x}_{0}\right)=\mathrm{BA}$, which is what (9.21) asserts.
9.16 Partial Derivatives. We again consider a function $\mathbf{f}$ that maps an open set $\mathrm{E} \subset \mathbb{R}^{n}$ into $\mathbb{R}^{m}$. Let $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ and $\left\{\mathbf{u}_{1}, \ldots, \mathbf{u}_{m}\right\}$ be the standard bases of $\mathbb{R}^{n}$ and $\mathbb{R}^{m}$. The components of $\mathbf{f}$ are the real functions $f_{1}, \ldots, f_{m}$ defined by

$$
\mathbf{f}(\mathbf{x})=\sum_{i=1}^{m} f_{i}(\mathbf{x}) \mathbf{u}_{i} \quad(\mathbf{x} \in \mathrm{E})
$$

or, equivalently, by $f_{i}(\mathbf{x})=\mathbf{f}(\mathbf{x}) \cdot \mathbf{u}_{i}, 1 \leq i \leq m$.
For $\mathbf{x} \in \mathrm{E}, 1 \leq \mathrm{i} \leq \mathrm{m}, 1 \leq \mathrm{j} \leq \mathrm{n}$, we define

$$
\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})=\lim _{\mathrm{t} \rightarrow 0} \frac{\mathrm{f}_{\mathrm{i}}\left(\mathbf{x}+\mathrm{t} \mathbf{e}_{\mathrm{i}}\right)-\mathrm{f}_{\mathrm{i}}(\mathbf{x})}{\mathrm{t}}
$$

provided the limit exists. Writing $f_{i}\left(x_{1}, \ldots, x_{n}\right)$ in place of $f_{i}(\mathbf{x})$, we see that $D_{j} f_{i}$ is the derivative of $f_{i}$ with respect to $x_{j}$, keeping the other variables fixed. The notation

$$
\frac{\partial f_{i}}{\partial x_{j}}
$$

is therefore often used in place of $D_{j} f_{i}$, and $D_{j} f_{i}$ is called a partial derivative.
In many cases where the existence of a derivative is sufficient when dealing with functions of one variable, continuity or at least boundedness of the partial derivatives is needed for functions of several variables. For example, the functions

f and g described in Exercise 4.7 are not continuous, although their partial derivatives exist at every point of $\mathbb{R}^{2}$. Even for continuous functions, the existence of all partial derivatives does not imply differentiability in the sense of Definition 9.11; see Exercises 9.6 and 9.14 and Theorem 9.21.

However, if $\mathbf{f}$ is known to be differentiable at a point $\mathbf{x}$, then its partial derivatives exist at $\mathbf{x}$ and they determine the linear transformation $\mathbf{f}^{\prime}(\mathbf{x})$ completely:
9.17 Theorem. Suppose $\mathbf{f}$ maps an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{m}}$, and $\mathbf{f}$ is differentiable at a point $\mathbf{x} \in \mathrm{E}$. Then the partial derivatives $\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})$ exist and

$$
\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{e}_{\mathrm{j}}=\sum_{\mathrm{i}=1}^{\mathrm{m}}\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x}) \mathbf{u}_{\mathrm{i}} \quad(1 \leq \mathrm{j} \leq \mathrm{n})
$$

Here, as in Theorem 9.16, $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ and $\left\{\mathbf{u}_{1}, \ldots, \mathbf{u}_{m}\right\}$ are the standard bases of $\mathbb{R}^{n}$ and $\mathbb{R}^{m}$.

Proof. Fix j. Since $\mathbf{f}$ is differentiable at $\mathbf{x}$,

$$
\mathbf{f}\left(\mathbf{x}+\mathrm{t} \mathbf{e}_{\mathrm{j}}\right)-\mathbf{f}(\mathbf{x})=\mathbf{f}^{\prime}(\mathbf{x})\left(\mathrm{t} \mathbf{e}_{\mathrm{j}}\right)+\mathbf{r}\left(\mathrm{t} \mathbf{e}_{\mathrm{j}}\right)
$$

where $\left|\mathbf{r}\left(\mathrm{t} \mathbf{e}_{\mathrm{j}}\right)\right| / \mathrm{t} \rightarrow 0$ as $\mathrm{t} \rightarrow 0$. The linearity of $\mathbf{f}^{\prime}(\mathbf{x})$ shows therefore that

$$
\lim _{t \rightarrow 0} \frac{\mathbf{f}\left(\mathbf{x}+\mathrm{t} \mathbf{e}_{\mathrm{j}}\right)-\mathbf{f}(\mathbf{x})}{\mathrm{t}}=\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{e}_{\mathrm{j}}
$$

If we now represent $\mathbf{f}$ in terms of its components, as in (9.24), then (9.28) becomes

$$
\lim _{t \rightarrow 0} \sum_{i=1}^{m} \frac{f_{i}\left(x+t e_{j}\right)-f_{i}(x)}{t} u_{i}=f^{\prime}(x) e_{j}
$$

It follows that each quotient in this sum has a limit as $t \rightarrow 0$ (see Theorem 4.10), so that each $\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})$ exists, and then (9.27) follows from (9.29).

Here are some consequences of Theorem 9.17:
Let $\left[\mathbf{f}^{\prime}(\mathbf{x})\right]$ be the matrix that represents $\mathbf{f}^{\prime}(\mathbf{x})$ with respect to our standard bases, as in Theorem 9.9. Then $\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{e}_{\mathrm{j}}$ is the jth column vector of $\left[\mathbf{f}^{\prime}(\mathbf{x})\right]$ and (9.27) shows therefore that the number $\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})$ occupies the spot in the ith row and the jth column of $\left[\mathbf{f}^{\prime}(\mathbf{x})\right]$. Thus

$$
\left[\mathbf{f}^{\prime}(\mathbf{x})\right]=\left[\begin{array}{ccc}
\left(\mathrm{D}_{1} \mathrm{f}_{1}\right)(\mathbf{x}) & \cdots & \left(\mathrm{D}_{n} \mathrm{f}_{1}\right)(\mathbf{x}) \\
\vdots & \ddots & \vdots \\
\left(\mathrm{D}_{1} \mathrm{f}_{m}\right)(\mathbf{x}) & \cdots & \left(\mathrm{D}_{n} \mathrm{f}_{m}\right)(\mathbf{x})
\end{array}\right]
$$

If $\mathbf{h}=\Sigma \mathrm{h}_{\mathrm{j}} \mathbf{e}_{\mathrm{j}}$ is any vector in $\mathbb{R}^{\mathrm{n}}$, then (9.27) implies that

$$
\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{h}=\sum_{\mathrm{i}=1}^{\mathrm{m}}\left\{\sum_{\mathrm{j}=1}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x}) \mathrm{h}_{\mathrm{j}}\right\} \mathbf{u}_{\mathrm{i}}
$$

9.18 Example. Let $\gamma$ be a differentiable mapping of the segment $(a, b) \subset \mathbb{R}^{1}$ into an open set $E \subset \mathbb{R}^{n}$; in other words, $\gamma$ is a differentiable curve in $E$. Let $f$ be a realvalued differentiable function with domain $E$. Thus $f$ is a differentiable mapping of $E$ into $\mathbb{R}^{1}$. Define

$$
g(t)=f(\gamma(t)) \quad(a<t<b)
$$

The chain rule asserts then that

$$
g^{\prime}(t)=f^{\prime}(\gamma(t)) \gamma^{\prime}(t) \quad(a<t<b)
$$

Since $\gamma^{\prime}(t) \in L\left(\mathbb{R}^{1}, \mathbb{R}^{n}\right)$ and $f^{\prime}(\gamma(t)) \in L\left(\mathbb{R}^{n}, \mathbb{R}^{1}\right)$, (9.32) defines $g^{\prime}(t)$ as a linear operator on $\mathbb{R}^{1}$. This agrees with the fact that $g$ maps $(a, b)$ into $\mathbb{R}^{1}$. However, $g^{\prime}(t)$ can also be regarded as a real number. (This was discussed in Theorem 9.10.) This number can be computed in terms of the partial derivatives of $f$ and the derivatives with the components of $\gamma$, as we shall now see.

With respect to the standard basis $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ of $\mathbb{R}^{n},\left[\gamma^{\prime}(t)\right]$ is the $n$ by 1 matrix (a "column matrix") which has $\gamma_{\mathrm{i}}^{\prime}(\mathrm{t})$ in the ith row, where $\gamma_{1}, \ldots, \gamma_{n}$ are the components of $\gamma$. For every $\mathbf{x} \in \mathrm{E},\left[\mathrm{f}^{\prime}(\mathbf{x})\right]$ is the 1 by n matrix (a "row matrix") which has $\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}\right)(\mathbf{x})$ in the jth column. Hence $\left[\mathrm{g}^{\prime}(\mathrm{t})\right]$ is the 1 by 1 matrix whose only entry is the real number

$$
g^{\prime}(t)=\sum_{i=1}^{n}\left(D_{i} f\right)(\gamma(t)) \gamma_{i}^{\prime}(t)
$$

This is a frequently encountered special case of the chain rule. It can be rephrased in the following manner.

Associate with each $\mathbf{x} \in E$ a vector, the so-called "gradient" of $f$ at $\mathbf{x}$, defined by

$$
(\nabla f)(x)=\sum_{i=1}^{n}\left(D_{i} f\right)(x) e_{i}
$$

Since

$$
\gamma^{\prime}(t)=\sum_{i=1}^{n} \gamma_{i}^{\prime}(t) e_{i}
$$

(9.33) can be written in the form

$$
g^{\prime}(t)=(\nabla f)(\gamma(t)) \cdot \gamma^{\prime}(t)
$$

the scalar product of the vectors $(\nabla f)(\gamma(t))$ and $\gamma^{\prime}(t)$.
Let us now fix an $\mathbf{x} \in \mathrm{E}$, let $\mathbf{u} \in \mathbb{R}^{n}$ be a unit vector (that is, $|\mathbf{u}|=1$ ), and specialize $\gamma$ so that

$$
\gamma(t)=\mathbf{x}+\mathrm{tu} \quad(-\infty<\mathrm{t}<\infty)
$$

Then $\gamma^{\prime}(t)=\mathbf{u}$ for every $t$. Hence (9.36) shows that

$$
g^{\prime}(0)=(\nabla f)(x) \cdot u
$$

On the other hand, (9.37) shows that

$$
g(t)-g(0)=f(x+t u)-f(x)
$$

Hence (9.38) gives

$$
\lim _{t \rightarrow 0} \frac{f(x+t u)-f(x)}{t}=(\nabla f)(x) \cdot u
$$

The limit in (9.39) is usually called the directional derivative of $f$ at $\mathbf{x}$, in the direction of the unit vector $\mathbf{u}$, and may be denoted by $\left(\mathrm{D}_{\mathbf{u}} \mathrm{f}\right)(\mathbf{x})$. If f and x are fixed, but $\mathbf{u}$ varies, then (9.39) shows that $\left(\mathrm{D}_{\mathbf{u}} \mathrm{f}\right)(\mathbf{x})$ attains its maximum when $\mathbf{u}$ is a positive scalar multiple of $(\nabla f)(\mathbf{x})$. [The case $(\nabla f)(\mathbf{x})=0$ should be excluded here.]

If $\mathbf{u}=\Sigma u_{i} \mathbf{e}_{i}$, then (9.39) shows that $\left(\mathrm{D}_{\mathbf{u}} \mathrm{f}\right)(\mathbf{x})$ can be expressed in terms of the partial derivatives of $f$ at $\mathbf{x}$ by the formula

$$
\left(D_{\mathbf{u}} f\right)(\mathbf{x})=\sum_{i=1}^{n}\left(D_{i} f\right)(\mathbf{x}) u_{i}
$$

Some of these ideas will play a role in the following theorem.
9.19 Theorem. Suppose $\mathbf{f}$ maps a convex open set $\mathrm{E} \subset \mathbb{R}^{n}$ into $\mathbb{R}^{m}$, $\mathbf{f}$ is differentiable in E , and there is a real number M such that

$$
\left\|\mathbf{f}^{\prime}(\mathbf{x})\right\| \leq M
$$

for every $\mathbf{x} \in \mathrm{E}$. Then

$$
|\mathbf{f}(\mathbf{b})-\mathbf{f}(\mathbf{a})| \leq M(\mathbf{b}-\mathbf{a})
$$

for all $\mathbf{a} \in \mathrm{E}, \mathbf{b} \in \mathrm{E}$.
Proof. Fix $\mathbf{a} \in \mathrm{E}, \mathbf{b} \in \mathrm{E}$. Define

$$
\gamma(t)=(1-t) \mathbf{a}+t \mathbf{b}
$$

for all $t \in \mathbb{R}^{1}$ such that $\gamma(t) \in E$. Since $E$ is convex, $\gamma(t) \in E$ if $0 \leq t \leq 1$. Put

$$
\mathbf{g}(t)=\mathbf{f}(\gamma(t))
$$

Then

$$
\mathbf{g}^{\prime}(\mathrm{t})=\mathbf{f}^{\prime}(\gamma(\mathrm{t})) \gamma^{\prime}(\mathrm{t})=\mathbf{f}^{\prime}(\gamma(\mathrm{t}))(\mathbf{b}-\mathbf{a})
$$

so that

$$
\left|\mathbf{g}^{\prime}(\mathrm{t})\right| \leq\left|\mathbf{f}^{\prime}(\gamma(\mathrm{t}))\right||\mathbf{b}-\mathbf{a}| \leq \mathrm{M}|\mathbf{b}-\mathbf{a}|
$$

for all $t \in[0,1]$. By Theorem 5.19,

$$
|\mathbf{g}(1)-\mathbf{g}(0)| \leq \mathrm{M}|\mathbf{b}-\mathbf{a}|
$$

But $\mathbf{g}(0)=\mathbf{f}(\mathbf{a})$ and $\mathbf{g}(1)=\mathbf{f}(\mathbf{b})$. This completes the proof.
Corollary. If, in addition, $\mathbf{f}^{\prime}(\mathbf{x})=\mathbf{0}$ for all $\mathbf{x} \in \mathrm{E}$, then $\mathbf{f}$ is constant.
Proof. To prove this, note that the hypothesis of the theorem now hold with $M=$ 0 .
9.20 Definition. A differentiable mapping $\mathbf{f}$ of an open set $E \subset \mathbb{R}^{n}$ into $\mathbb{R}^{m}$ is said to be continuously differentiable if $E$ if $\mathbf{f}^{\prime}$ is a continuous mapping of $E$ into $\mathrm{L}\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$.

More explicitly, it is required that to every $\mathbf{x} \in \mathrm{E}$ and to every $\varepsilon>0$ corresponds a $\delta>0$ such that

$$
\left\|\mathbf{f}^{\prime}(\mathbf{y})-\mathbf{f}^{\prime}(\mathbf{x})\right\|<\varepsilon
$$

if $\mathbf{y} \in \mathrm{E}$ and $|\mathbf{x}-\mathbf{y}|<\delta$.
If this is so, we also say that $\mathbf{f}$ is a $\mathscr{C}^{1}$ mapping, or that $\mathbf{f} \in \mathscr{C}^{1}(\mathrm{E})$.
9.21 Theorem. Suppose $\mathbf{f}$ maps an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{m}}$. Then $\mathbf{f} \in \mathscr{C}^{1}(\mathrm{E})$ if and only if the partial derivatives exist and are continuous for $1 \leq \mathrm{i} \leq \mathrm{m}, 1 \leq \mathrm{j} \leq \mathrm{n}$.

Proof. Assume first that $\mathbf{f} \in \mathscr{C}^{1}(\mathrm{E})$. By (9.27),

$$
\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})=\left(\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{e}_{\mathrm{j}}\right) \cdot \mathbf{u}_{\mathrm{i}}
$$

for all $i, j$ and for all $\mathbf{x} \in \mathrm{E}$. Hence

$$
\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{y})-\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})=\left\{\left[\mathbf{f}^{\prime}(\mathbf{y})-\mathbf{f}^{\prime}(\mathbf{x})\right] \mathbf{e}_{\mathrm{j}}\right\} \cdot \mathbf{u}_{\mathrm{i}}
$$

and since $\left|\mathbf{u}_{\mathrm{i}}\right|=\left|\mathbf{e}_{\mathrm{j}}\right|=1$, it follows that

$$
\begin{aligned}
\left|\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{y})-\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})\right| & \leq\left|\left[\mathbf{f}^{\prime}(\mathbf{y})-\mathbf{f}^{\prime}(\mathbf{x})\right] \mathbf{e}_{\mathrm{j}}\right| \\
& \leq\left\|\mathbf{f}^{\prime}(\mathbf{y})-\mathbf{f}^{\prime}(\mathbf{x})\right\|
\end{aligned}
$$

Hence $D_{j} f_{i}$ is continuous.

For the converse, it suffices to consider the case $m=1$. (Why?) Fix $x \in E$ and $\varepsilon>0$. Since $E$ is open, there is an open ball $S \subset E$, with center at $x$ and radius $r$, and the continuity of the functions $D_{j} f$ shows that $r$ can be chosen so that

$$
\left|\left(D_{j} f\right)(y)-\left(D_{j} f\right)(x)\right|<\frac{\varepsilon}{n} \quad(y \in S, 1 \leq j \leq n)
$$

Suppose $\mathbf{h}=\Sigma h_{j} \mathbf{e}_{j},|\mathbf{h}|<r$, put $\mathbf{v}_{0}=\mathbf{0}$, and $\mathbf{v}_{\mathrm{k}}=h_{1} \mathbf{e}_{1}+\cdots+h_{k} \mathbf{e}_{k}$, for $1 \leq \mathrm{k} \leq \mathrm{n}$. Then

$$
f(x+h)-f(x)=\sum_{j=1}^{n}\left[f\left(x+v_{j}\right)-f\left(x+v_{j-1}\right)\right]
$$

Since $\left|\mathbf{v}_{\mathrm{k}}\right|<r$ for $1 \leq \mathrm{k} \leq \mathrm{n}$ and since $S$ is convex, the segments with end points $\mathbf{x}+\mathbf{v}_{\mathbf{j}-1}$ and $\mathbf{x}+\mathbf{v}_{\mathbf{j}}$ lie in $S$. Since $\mathbf{v}_{\mathbf{j}}=\mathbf{v}_{\mathbf{j}-1}+\mathrm{h}_{\mathbf{j}} \mathbf{e}_{\mathbf{j}}$, the mean value theorem (Theorem 5.10) shows that the jth summand in (9.42) is equal to

$$
h_{j}\left(D_{j} f\right)\left(x+v_{j-1}+\theta_{j} h_{j} e_{j}\right)
$$

for some $\theta_{j} \in(0,1)$, and this differs from $h_{j}\left(D_{j} f\right)(x)$ by less than $\left|h_{j}\right| \varepsilon / n$, using (9.41). By (9.42), it follows that

$$
\left|f(x+h)-f(x)-\sum_{j=1}^{n} h_{j}\left(D_{j} f\right)(x)\right| \leq \frac{1}{n} \sum_{j=1}^{n}\left|h_{j}\right| \varepsilon \leq|h| \varepsilon
$$

for all $\mathbf{h}$ such that $|\mathbf{h}|<r$.
This says that $f$ is differentiable at $x$ and that $f^{\prime}(x)$ is the linear function which assigns the number $\Sigma h_{j}\left(D_{j} f\right)(x)$ to the vector $\mathbf{h}=\Sigma h_{j} \mathbf{e}_{j}$. The matrix $\left[f^{\prime}(x)\right]$ consists of the row $\left(D_{1} f\right)(x), \ldots,\left(D_{n} f\right)(x)$; since $D_{1} f, \ldots, D_{n} f$ are continuous functions on E, the concluding remarks of Theorem 9.9 show that $f \in \mathscr{C}^{1}(\mathrm{E})$.

# THE CONTRACTION PRINCIPLE 

We now interrupt our discussion of differentiation to insert a fixed point theorem that is valid in arbitrary complete metric spaces. It will be used in the proof of the inverse function theorem.
9.22 Definition. Let $X$ be a metric space with metric $d$. If $\varphi$ maps $X$ into $X$ and if there is a number $\mathrm{c}<1$ such that

$$
\mathrm{d}(\varphi(\mathrm{x}), \varphi(\mathrm{y})) \leq \mathrm{cd}(\mathrm{x}, \mathrm{y})
$$

for all $x, y \in X$, then $\varphi$ is said to be a contraction of $X$ into $X$.
9.23 Theorem. If $X$ is a complete metric space and $\varphi$ is a contraction of $X$ into $X$, then there exists one and only one $\mathrm{x} \in \mathrm{X}$ such that $\varphi(\mathrm{x})=\mathrm{x}$.

In other words, $\varphi$ has a unique fixed point. The uniqueness is a triviality, for if $\varphi(\mathrm{x})=\mathrm{x}$ and $\varphi(\mathrm{y})=\mathrm{y}$, then (9.43) gives $\mathrm{d}(\mathrm{x}, \mathrm{y}) \leq \mathrm{cd}(\mathrm{x}, \mathrm{y})$ which can only happen when $\mathrm{d}(\mathrm{x}, \mathrm{y})=0$.

The existence of a fixed point of $\varphi$ is the essential part of the theorem. The proof actually furnishes a constructive method for locating the fixed point.

Proof. Pick $\mathrm{x}_{0} \in \mathrm{X}$ arbitrarily and define $\left(\mathrm{x}_{\mathrm{n}}\right)$ recursively, by setting

$$
x_{n+1}=\varphi\left(x_{n}\right) \quad(n=0,1,2, \ldots)
$$

Choose $\mathrm{c}<1$ so that (9.43) holds. For $\mathrm{n} \geq 1$ we then have

$$
\mathrm{d}\left(\mathrm{x}_{\mathrm{n}+1}, \mathrm{x}_{\mathrm{n}}\right)=\mathrm{d}\left(\varphi\left(\mathrm{x}_{\mathrm{n}}\right), \varphi\left(\mathrm{x}_{\mathrm{n}-1}\right)\right) \leq \mathrm{cd}\left(\mathrm{x}_{\mathrm{n}}, \mathrm{x}_{\mathrm{n}-1}\right)
$$

Hence induction gives

$$
\mathrm{d}\left(\mathrm{x}_{\mathrm{n}+1}, \mathrm{~d}_{\mathrm{n}}\right) \leq \mathrm{c}^{\mathrm{n}} \mathrm{~d}\left(\mathrm{x}_{1}, \mathrm{x}_{0}\right) \quad(\mathrm{n}=0,1,2, \ldots)
$$

If $\mathrm{n}<\mathrm{m}$, it follows that

$$
\begin{aligned}
\mathrm{d}\left(\mathrm{x}_{\mathrm{n}}, \mathrm{x}_{\mathrm{m}}\right) & \leq \sum_{\mathrm{i}=\mathrm{n}+1}^{\mathrm{m}} \mathrm{~d}\left(\mathrm{x}_{\mathrm{i}}, \mathrm{x}_{\mathrm{i}+1}\right) \\
& \leq\left(\mathrm{c}^{\mathrm{n}}+\mathrm{c}^{\mathrm{n}+1}+\cdots+\mathrm{c}^{\mathrm{m}-1}\right) \mathrm{d}\left(\mathrm{x}_{1}, \mathrm{x}_{0}\right) \\
& \leq\left[(1-\mathrm{c})^{-1} \mathrm{~d}\left(\mathrm{x}_{1}, \mathrm{x}_{0}\right)\right] \mathrm{c}^{\mathrm{n}}
\end{aligned}
$$

Thus $\left(\mathrm{x}_{\mathrm{n}}\right)$ is a Cauchy sequence. Since X is complete, $\lim \mathrm{x}_{\mathrm{n}}=\mathrm{x}$ for some $\mathrm{x} \in \mathrm{X}$.
Since $\varphi$ is a contraction, $\varphi$ is continuous (in fact, uniformly continuous) on X . Hence

$$
\varphi(\mathrm{x})=\lim _{\mathrm{n} \rightarrow \infty} \varphi\left(\mathrm{x}_{\mathrm{n}}\right)=\lim _{\mathrm{n} \rightarrow \infty} \varphi\left(\mathrm{x}_{\mathrm{n}+1}\right)=\mathrm{x}
$$

# THE INVERSE FUNCTION THEOREM 

The inverse function theorem states, roughly speaking, that a continuously differentiable mapping $\mathbf{f}$ is invertible in a neighborhood of any point $\mathbf{x}$ at which the linear transformation $\mathbf{f}^{\prime}(\mathbf{x})$ is invertible:
9.24 Theorem. Suppose $\mathbf{f}$ is a $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{n}$ into $\mathbb{R}^{n}, \mathbf{f}^{\prime}(\mathbf{a})$ is invertible for some $\mathbf{a} \in \mathrm{E}$, and $\mathbf{b}=\mathbf{f}(\mathbf{a})$. Then
(a) there exist open sets $U$ and $V$ in $\mathbb{R}^{n}$ such that $\mathbf{a} \in U, \mathbf{b} \in V, \mathbf{f}$ is one-to-one on $U$, and $\mathbf{f}(\mathrm{U})=\mathrm{V}$;
(b) if $\mathbf{g}$ is the inverse of $\mathbf{f}$ [which exists, by (a)], defined in $V$ by

$$
\mathbf{g}(\mathbf{f}(\mathbf{x}))=\mathbf{x} \quad(\mathbf{x} \in \mathrm{U})
$$

then $\mathbf{g} \in \mathscr{C}^{1}(\mathrm{~V})$.

Writing the equation $\mathbf{y}=\mathbf{f}(\mathbf{x})$ in component form, we arrive at the following interpretation of the conclusion of the theorem: The system of $n$ equations

$$
y_{i}=f_{i}\left(x_{1}, \ldots, x_{n}\right) \quad(1 \leq i \leq n)
$$

can be solved for $x_{1}, \ldots, x_{n}$ in terms of $y_{1}, \ldots, y_{n}$, if we restrict $x$ and $y$ to small enough neighborhoods of $\mathbf{a}$ and $\mathbf{b}$; the solutions are unique and continuously differentiable.

Proof.
(a) Put $\mathbf{f}^{\prime}(\mathbf{a})=A$ and choose $\lambda$ so that

$$
2 \lambda\left\|A^{-1}\right\|=1
$$

Since $\mathbf{f}^{\prime}$ is continuous at $\mathbf{a}$, there is an open ball $U \subset E$ with center $\mathbf{a}$ such that

$$
\left\|\mathbf{f}^{\prime}(\mathbf{x})-A\right\|<\lambda \quad(\mathbf{x} \in \mathrm{U})
$$

We associate to each $\mathbf{y} \in \mathbb{R}^{n}$ a function $\varphi$, defined by

$$
\varphi(\mathbf{x})=\mathbf{x}+\mathrm{A}^{-1}(\mathbf{y}-\mathbf{f}(\mathbf{x})) \quad(\mathbf{x} \in \mathrm{E})
$$

Note that $\mathbf{f}(\mathbf{x})=\mathbf{y}$ if and only if $\mathbf{x}$ is a fixed point of $\varphi$.
Since $\varphi^{\prime}(\mathbf{x})=I-A^{-1} \mathbf{f}^{\prime}(\mathbf{x})=A^{-1}\left(A-\mathbf{f}^{\prime}(\mathbf{x})\right),(9.46)$ and (9.47) imply that

$$
\left\|\varphi^{\prime}(\mathbf{x})\right\|<\frac{1}{2} \quad(\mathbf{x} \in \mathrm{U})
$$

Hence

$$
\left|\varphi\left(\mathbf{x}_{1}\right)-\varphi\left(\mathbf{x}_{2}\right)\right| \leq \frac{1}{2}\left|\mathbf{x}_{1}-\mathbf{x}_{2}\right| \quad\left(\mathbf{x}_{1}, \mathbf{x}_{2} \in \mathrm{U}\right)
$$

by Theorem 9.19. It follows that $\varphi$ has at most one fixed point in $U$, so that $\mathbf{f}(\mathbf{x})=\mathbf{y}$ for at most one $\mathbf{x} \in \mathrm{U}$.

Thus $\mathbf{f}$ is 1-1 in U.
Next, put $V=\mathbf{f}(U)$ and pick $\mathbf{y}_{0} \in V$. Then $\mathbf{y}_{0}=\mathbf{f}\left(\mathbf{x}_{0}\right)$ for some $\mathbf{x}_{0} \in U$. Let $B$ be an open ball with center at $\mathbf{x}_{0}$ and radius $r>0$, so small that its closure $\overline{\mathrm{B}}$ lies in $U$. We will show that $\mathbf{y} \in V$ whenever $\left|\mathbf{y}-\mathbf{y}_{0}\right|<\lambda r$. This proves, of course, that $V$ is open.

Fix $\mathbf{y},\left|\mathbf{y}-\mathbf{y}_{0}\right|<\lambda$ r. With $\varphi$ as in (9.48),

$$
\left|\varphi\left(\mathbf{x}_{0}\right)-\mathbf{x}_{0}\right|=\left|\mathrm{A}^{-1}\left(\mathbf{y}-\mathbf{y}_{0}\right)\right|<\left\|\mathrm{A}^{-1}\right\| \lambda r=\frac{r}{2}
$$

If $\mathbf{x} \in \overline{\mathrm{B}}$, it therefore follows from (9.50) that

$$
\begin{aligned}
\left|\varphi(\mathbf{x})-\mathbf{x}_{0}\right| & \leq\left|\varphi(\mathbf{x})-\varphi\left(\mathbf{x}_{0}\right)\right|+\left|\varphi\left(\mathbf{x}_{0}\right)-\mathbf{x}_{0}\right| \\
& <\frac{1}{2}\left|\mathbf{x}-\mathbf{x}_{0}\right|+\frac{\tau}{2} \leq \tau
\end{aligned}
$$

hence $\varphi(\mathbf{x}) \in \mathrm{B}$. Note that (9.50) holds if $\mathbf{x}_{1} \in \overline{\mathrm{B}}, \mathbf{x}_{2} \in \overline{\mathrm{B}}$.
Thus $\varphi$ is a contraction of $\overline{\mathrm{B}}$ into $\overline{\mathrm{B}}$. Being a closed subset of $\mathbb{R}^{n}, \overline{\mathrm{~B}}$ is complete. Theorem 9.23 implies therefore that $\varphi$ has a fixed point $\mathbf{x} \in \overline{\mathrm{B}}$. For this $\mathbf{x}, \mathbf{f}(\mathbf{x})=\mathbf{y}$. Thus $\mathbf{y} \in \mathbf{f}(\overline{\mathrm{B}}) \subset \mathbf{f}(\mathrm{U})=\mathrm{V}$. This proves part (a) of the theorem.
(b) Pick $\mathbf{y} \in V, \mathbf{y}+\mathbf{k} \in V$. Then there exist $\mathbf{x} \in \mathrm{U}, \mathbf{x}+\mathbf{h} \in \mathrm{U}$, so that $\mathbf{y}=\mathbf{f}(\mathbf{x})$, $\mathbf{y}+\mathbf{k}=\mathbf{f}(\mathbf{x}+\mathbf{h})$. With $\varphi$ as in (9.48),

$$
\varphi(\mathbf{x}+\mathbf{h})-\varphi(\mathbf{x})=\mathbf{h}+\mathrm{A}^{-1}[\mathbf{f}(\mathbf{x})-\mathbf{f}(\mathbf{x}+\mathbf{h})]=\mathbf{h}-\mathrm{A}^{-1} \mathbf{k}
$$

By (9.50), $\left|\mathbf{h}-\mathrm{A}^{-1} \mathbf{k}\right| \leq|\mathbf{h}| / 2$. Hence $\left|\mathrm{A}^{-1} \mathbf{k}\right| \geq|\mathbf{h}| / 2$ and

$$
|\mathbf{h}| \leq 2\left\|\mathrm{~A}^{-1}\right\|| | \mathbf{k}|=\lambda^{-1}|\mathbf{k}|
$$

By (9.46), (9.47), and Theorem 9.8, $\mathbf{f}^{\prime}(\mathbf{x})$ has an inverse, say T. Since

$$
\mathbf{g}(\mathbf{y}+\mathbf{k})-\mathbf{g}(\mathbf{y})-\mathrm{T} \mathbf{k}=\mathbf{h}-\mathrm{T} \mathbf{k}=-\mathrm{T}[\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{h}]
$$

(9.51) implies

$$
\frac{|\mathbf{g}(\mathbf{y}+\mathbf{k})-\mathbf{g}(\mathbf{y})-\mathrm{T} \mathbf{k}|}{|\mathbf{k}|} \leq \frac{\|\mathrm{T}\|}{\lambda} \cdot \frac{|\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-\mathbf{f}^{\prime}(\mathbf{x}) \mathbf{h}|}{|\mathbf{h}|}
$$

As $\mathbf{k} \rightarrow \mathbf{0}$, (9.51) shows that $\mathbf{h} \rightarrow \mathbf{0}$. The right side of the last inequality thus tends to 0 . Hence the same is true of the left. We have thus proved that $\mathbf{g}^{\prime}(\mathbf{y})=\mathrm{T}$. But T was chosen to be the inverse of $\mathbf{f}^{\prime}(\mathbf{x})=\mathbf{f}^{\prime}(\mathbf{g}(\mathbf{y}))$. Thus

$$
\mathbf{g}^{\prime}(\mathbf{y})=\left\{\mathbf{f}^{\prime}(\mathbf{g}(\mathbf{y}))\right\}^{-1} \quad(\mathbf{y} \in V)
$$

Finally, note that $\mathbf{g}$ is a continuous mapping of $V$ onto $U$ (since $\mathbf{g}$ is differentiable), that $\mathbf{f}^{\prime}$ is a continuous mapping of $U$ into the set $\Omega$ of all invertible elements of $L\left(\mathbb{R}^{n}\right)$, and that inversion is a continuous mapping of $\Omega$ onto $\Omega$, by Theorem 9.8. If we combine these facts with (9.52), we see that $\mathbf{g} \in \mathscr{C}^{1}(\mathrm{~V})$. This completes the proof.

Remark. The full force of the assumption that $\mathbf{f} \in \mathscr{C}^{1}(\mathrm{E})$ was only used in the last paragraph of the preceding proof. Everything else, down to (9.52), was derived from the existence of $\mathbf{f}^{\prime}(\mathbf{x})$ for $\mathbf{x} \in \mathrm{E}$, the invertibility of $\mathbf{f}^{\prime}(\mathbf{a})$, and the continuity of $\mathbf{f}^{\prime}$ at just the point a. In this connection, we refer to the article by A. Nijenhuis in Amer. Math. Monthly, vol. 81, 1974, pp. 969-980.

The following is an immediate consequence of part (a) of the inverse function theorem.
9.25 Theorem. If $\mathbf{f}$ is a $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{n}}$ and if $\mathbf{f}^{\prime}(\mathbf{x})$ is invertible for every $\mathbf{x} \in \mathrm{E}$, then $\mathbf{f}(W)$ is an open subset of $\mathbb{R}^{n}$ for every open set $W \subset \mathrm{E}$. In other words, $\mathbf{f}$ is an open mapping of E into $\mathbb{R}^{n}$.

The hypotheses made in this theorem ensure that each point $\mathbf{x} \in \mathrm{E}$ has a neighborhood in which $\mathbf{f}$ is 1-1. This may be expressed by saying that $\mathbf{f}$ is locally one-toone in E. But $\mathbf{f}$ need not be 1-1 in E under these circumstances. For an example, see Exercise 9.17.

# THE IMPLICIT FUNCTION THEOREM 

If $f$ is a continuously differentiable real function in the plane, then the equation $f(x, y)=0$ can be solved for $y$ in terms of $x$ in a neighborhood of any point $(a, b)$ at which $f(a, b)=0$ and $\partial f / \partial y \neq 0$. Likewise, one can solve for $x$ in terms of $y$ near $(a, b)$ if $\partial f / \partial x \neq 0$ at $(a, b)$. For a simple example which illustrates the need for assuming $\partial f / \partial y \neq 0$, consider $f(x, y)=x^{2}+y^{2}-1$.

The preceding very informal statement is the simplest case (the case $m=n=1$ of Theorem 9.28) of the so-called "implicit function theorem." Its proof makes strong use of the fact that continuously differentiable transformations behave locally very much like their derivatives. Accordingly, we first prove Theorem 9.27, the linear version of Theorem 9.28.
9.26 Notation. If $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right) \in \mathbb{R}^{n}$ and $\mathbf{y}=\left(y_{1}, \ldots, y_{m}\right) \in \mathbb{R}^{m}$, let us write $(\mathbf{x}, \mathbf{y})$ for the point (or vector)

$$
\left(x_{1}, \ldots, x_{n}, y_{1}, \ldots, y_{m}\right) \in \mathbb{R}^{n+m}
$$

In what follows, the first entry in $(\mathbf{x}, \mathbf{y})$ or in a similar symbol will always be a vector in $\mathbb{R}^{n}$, the second will be a vector in $\mathbb{R}^{m}$.

Every $A \in L\left(\mathbb{R}^{n+m}, \mathbb{R}^{n}\right)$ can be split into two linear transformations $A_{x}$ and $A_{y}$ defined by

$$
A_{x} \mathbf{h}=A(\mathbf{h}, \mathbf{0}), \quad A_{y} \mathbf{k}=A(\mathbf{0}, \mathbf{k})
$$

for any $\mathbf{h} \in \mathbb{R}^{n}, \mathbf{k} \in \mathbb{R}^{m}$. Then $A_{x} \in L\left(\mathbb{R}^{n}\right), A_{y} \in L\left(\mathbb{R}^{m}, \mathbb{R}^{n}\right)$, and

$$
A(\mathbf{h}, \mathbf{k})=A_{x} \mathbf{h}+A_{y} \mathbf{k}
$$

The linear version of the implicit function theorem is now almost obvious.

9.27 Theorem. If $\mathrm{A} \in \mathrm{L}\left(\mathbb{R}^{\mathrm{n}+\mathrm{m}}, \mathbb{R}^{\mathrm{n}}\right)$ and if $\mathrm{A}_{\mathrm{x}}$ is invertible, then there corresponds to every $\mathbf{k} \in \mathbb{R}^{\mathrm{m}}$ a unique $\mathbf{h} \in \mathbb{R}^{\mathrm{n}}$ such that $\mathrm{A}(\mathbf{h}, \mathbf{k})=\mathbf{0}$. This $\mathbf{h}$ can be computed from $\mathbf{k}$ by the formula

$$
\mathbf{h}=-\left(\mathrm{A}_{\mathrm{x}}\right)^{-1} \mathrm{~A}_{\mathrm{y}} \mathbf{k}
$$

Proof. By (9.54), $\mathrm{A}(\mathbf{h}, \mathbf{k})=\mathbf{0}$ if and only if

$$
A_{x} \mathbf{h}+A_{y} \mathbf{k}=\mathbf{0}
$$

which is the same as (9.55) when $A_{x}$ is invertible.
The conclusion of Theorem 9.27 is, in other words, that the equation $\mathrm{A}(\mathbf{h}, \mathbf{k})=\mathbf{0}$ can be solved (uniquely) for $\mathbf{h}$ if $\mathbf{k}$ is given, and that the solution $\mathbf{h}$ is a linear function of $\mathbf{k}$. Those who have some acquaintance with linear algebra will recognize this as a very familiar statement about systems of linear equations.
9.28 Theorem. Let $\mathbf{f}$ be a $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}+\mathrm{m}}$ into $\mathbb{R}^{\mathrm{n}}$ such that $\mathbf{f}(\mathbf{a}, \mathbf{b})=\mathbf{0}$ for some point $(\mathbf{a}, \mathbf{b}) \in \mathrm{E}$.

Put $\mathrm{A}=\mathbf{f}^{\prime}(\mathbf{a}, \mathbf{b})$ and assume that $\mathrm{A}_{\mathrm{x}}$ is invertible. Then there exist open sets $\mathrm{U} \subset$ $\mathbb{R}^{\mathrm{n}+\mathrm{m}}$ and $W \subset \mathbb{R}^{\mathrm{m}}$, with $(\mathbf{a}, \mathbf{b}) \in \mathrm{U}$ and $\mathbf{b} \in W$, having the following property:

To every $\mathbf{y} \in W$ corresponds a unique $\mathbf{x}$ such that

$$
(\mathbf{x}, \mathbf{y}) \in \mathrm{U} \quad \text { and } \quad \mathbf{f}(\mathbf{x}, \mathbf{y})=\mathbf{0}
$$

If this $\mathbf{x}$ is defined to be $\mathbf{g}(\mathbf{y})$, then $\mathbf{g}$ is a $\mathscr{C}^{1}$-mapping of $W$ into $\mathbb{R}^{\mathrm{n}}, \mathbf{g}(\mathbf{b})=\mathbf{a}$,

$$
\mathbf{f}(\mathbf{g}(\mathbf{y}), \mathbf{y})=\mathbf{0} \quad(\mathbf{y} \in W)
$$

and

$$
\mathbf{g}^{\prime}(\mathbf{b})=-\left(\mathrm{A}_{\mathrm{x}}\right)^{-1} \mathrm{~A}_{\mathrm{y}}
$$

The function $g$ is "implicitly" defined by (9.57). Hence the name of the theorem.
The equation $\mathbf{f}(\mathbf{x}, \mathbf{y})=\mathbf{0}$ can be written as a system of $n$ equations in $n+m$ variables:

$$
\left\{\begin{aligned}
f_{1}\left(x_{1}, \ldots, x_{n}, y_{1}, \ldots, y_{m}\right) & =0 \\
\vdots & \vdots \\
f_{n}\left(x_{1}, \ldots, x_{n}, y_{1}, \ldots, y_{m}\right) & =0
\end{aligned}\right.
$$

The assumption that $A_{x}$ is invertible means that the $n$ by $n$ matrix

$$
\left[\begin{array}{ccc}
D_{1} f_{1} & \cdots & D_{n} f_{1} \\
\vdots & \ddots & \vdots \\
D_{1} f_{n} & \cdots & D_{n} f_{n}
\end{array}\right]
$$

evaluated at $(\mathbf{a}, \mathbf{b})$ defines an invertible linear operator in $\mathbb{R}^{n}$; in other words, its column vectors should be independent, or, equivalently, its determinant should be nonzero. (See Theorem 9.36.) If, furthermore, (9.59) holds when $\mathbf{x}=\mathbf{a}$ and $\mathbf{y}=\mathbf{b}$, then the conclusion of the theorem is that (9.59) can be solved for $x_{1}, \ldots, x_{n}$ in terms of $y_{1}, \ldots, y_{m}$, for every $y$ near $b$, and that these solutions are continuously differentiable functions of $\mathbf{y}$.

Proof. Define $\mathbf{F}$ by

$$
\mathbf{F}(\mathbf{x}, \mathbf{y})=(\mathbf{f}(\mathbf{x}, \mathbf{y}), \mathbf{y}) \quad((\mathbf{x}, \mathbf{y}) \in \mathrm{E})
$$

Then $\mathbf{F}$ is a $\mathscr{C}^{1}$-mapping of E into $\mathbb{R}^{n+m}$. We claim that $\mathbf{F}^{\prime}(\mathbf{a}, \mathbf{b})$ is an invertible element of $\mathrm{L}\left(\mathbb{R}^{n+m}\right)$ :

Since $\mathbf{f}(\mathbf{a}, \mathbf{b})=\mathbf{0}$, we have

$$
\mathbf{f}(\mathbf{a}+\mathbf{h}, \mathbf{b}+\mathbf{k})=\mathrm{A}(\mathbf{h}, \mathbf{k})+\mathbf{r}(\mathbf{h}, \mathbf{k})
$$

where $\mathbf{r}$ is the remainder that occurs in the definition of $\mathbf{f}^{\prime}(\mathbf{a}, \mathbf{b})$. Since

$$
\begin{aligned}
\mathbf{F}(\mathbf{a}+\mathbf{h}, \mathbf{b}+\mathbf{k})-\mathbf{F}(\mathbf{a}, \mathbf{b}) & =(\mathbf{f}(\mathbf{a}+\mathbf{h}, \mathbf{b}+\mathbf{k}), \mathbf{k}) \\
& =(\mathrm{A}(\mathbf{h}, \mathbf{k}), \mathbf{k})+(\mathbf{r}(\mathbf{h}, \mathbf{k}), \mathbf{0})
\end{aligned}
$$

it follows that $\mathbf{F}^{\prime}(\mathbf{a}, \mathbf{b})$ is the linear operator on $\mathbb{R}^{n+m}$ that maps $(\mathbf{h}, \mathbf{k})$ to $(\mathrm{A}(\mathbf{h}, \mathbf{k}), \mathbf{k})$. If this image vector is $\mathbf{0}$, then $\mathrm{A}(\mathbf{h}, \mathbf{k})=\mathbf{0}$ and $\mathbf{k}=\mathbf{0}$, hence $\mathrm{A}(\mathbf{h}, \mathbf{0})=\mathbf{0}$ and Theorem 9.27 implies that $\mathbf{h}=\mathbf{0}$. It follows that $\mathbf{F}^{\prime}(\mathbf{a}, \mathbf{b})$ is $1-1$; hence it is invertible (Theorem 9.5).

The inverse function theorem can therefore be applied to $\mathbf{F}$. It shows that there exist open sets $U$ and $V$ in $\mathbb{R}^{n+m}$, with $(\mathbf{a}, \mathbf{b}) \in U,(0, \mathbf{b}) \in V$, such that $\mathbf{F}$ is a 1-1 mapping of $U$ onto $V$.

We let $W$ be the set of all $\mathbf{y} \in \mathbb{R}^{m}$ such that $(\mathbf{0}, \mathbf{y}) \in V$. Note that $\mathbf{b} \in W$. It is clear that $W$ is open since $V$ is open. If $\mathbf{y} \in W$, then $(\mathbf{0}, \mathbf{y})=\mathbf{F}(\mathbf{x}, \mathbf{y})$ for some $(\mathbf{x}, \mathbf{y}) \in U$. By (9.60), $\mathbf{f}(\mathbf{x}, \mathbf{y})=\mathbf{0}$ for this $\mathbf{x}$.

Suppose, with the same $\mathbf{y}$, that $\left(\mathbf{x}^{\prime}, \mathbf{y}\right) \in U$ and $\mathbf{f}\left(\mathbf{x}^{\prime}, \mathbf{y}\right)=\mathbf{0}$. Then

$$
\mathbf{F}\left(\mathbf{x}^{\prime}, \mathbf{y}\right)=\left(\mathbf{f}\left(\mathbf{x}^{\prime}, \mathbf{y}\right), \mathbf{y}\right)=(\mathbf{f}(\mathbf{x}, \mathbf{y}), \mathbf{y})=\mathbf{F}(\mathbf{x}, \mathbf{y})
$$

Since $\mathbf{F}$ is 1-1 in $U$, it follows that $\mathbf{x}^{\prime}=\mathbf{x}$. This proves the first part of the theorem.
For the second part, define $\mathbf{g}(\mathbf{y})$ for $\mathbf{y} \in W$, so that $(\mathbf{g}(\mathbf{y}), \mathbf{y}) \in U$ and (9.57) holds. Then

$$
\mathbf{F}(\mathbf{g}(\mathbf{y}), \mathbf{y})=(0, \mathbf{y}) \quad(\mathbf{y} \in W)
$$

If $\mathbf{G}$ is the mapping of $V$ onto $U$ that inverts $\mathbf{F}$, then $\mathbf{G} \in \mathscr{C}^{1}$ by the inverse function theorem and (9.61) gives

$$
(\mathbf{g}(\mathbf{y}), \mathbf{y})=\mathbf{G}(0, \mathbf{y}) \quad(\mathbf{y} \in W)
$$

Since $\mathbf{G} \in \mathscr{C}^{1}$, (9.62) shows that $\mathbf{g} \in \mathscr{C}^{1}$.
Finally, to compute $\mathbf{g}^{\prime}(\mathbf{b})$, put $(\mathbf{g}(\mathbf{y}), \mathbf{y})=\Phi(\mathbf{y})$. Then

$$
\Phi^{\prime}(\mathbf{y}) \mathbf{k}=\left(\mathbf{g}^{\prime}(\mathbf{y}) \mathbf{k}, \mathbf{k}\right) \quad\left(\mathbf{y} \in W, \mathbf{k} \in \mathbb{R}^{m}\right)
$$

By (9.57), $\mathbf{f}(\Phi(\mathbf{y}))=\mathbf{0}$ in $W$. The chain rule shows therefore that

$$
\mathbf{f}^{\prime}(\Phi(\mathbf{y})) \Phi^{\prime}(\mathbf{y})=0
$$

When $\mathbf{y}=\mathbf{b}$, then $\Phi(\mathbf{y})=(\mathbf{a}, \mathbf{b})$ and $\mathbf{f}^{\prime}(\Phi(\mathbf{y}))=A$. Thus

$$
A \Phi^{\prime}(\mathbf{b})=0
$$

It now follows from (9.64), (9.63), and (9.54) that

$$
A_{x} \mathbf{g}^{\prime}(\mathbf{b}) \mathbf{k}+A_{y} \mathbf{k}=A\left(\mathbf{g}^{\prime}(\mathbf{b}) \mathbf{k}, \mathbf{k}\right)=A \Phi^{\prime}(\mathbf{b}) \mathbf{k}=\mathbf{0}
$$

for every $\mathbf{k} \in \mathbb{R}^{m}$. Thus

$$
A_{x} \mathbf{g}^{\prime}(\mathbf{b})+A_{y}=0
$$

This is equivalent to (9.58) and completes the proof.
Note. In terms of the components of $\mathbf{f}$ and $\mathbf{g}$, (9.65) becomes

$$
\sum_{j=1}^{n}\left(D_{j} f_{i}\right)(\mathbf{a}, \mathbf{b})\left(D_{k} g_{j}\right)(\mathbf{b})=-\left(D_{n+k} f_{i}\right)(\mathbf{a}, \mathbf{b})
$$

or

$$
\sum_{j=1}^{n}\left(\frac{\partial f_{i}}{\partial x_{j}}\right)\left(\frac{\partial g_{j}}{\partial y_{k}}\right)=-\left(\frac{\partial f_{i}}{\partial y_{k}}\right)
$$

where $1 \leq \mathrm{i} \leq \mathrm{n}, 1 \leq \mathrm{k} \leq \mathrm{m}$.
For each $k$, this is a system of $n$ linear equations in which the derivatives $\partial g_{j} / \partial y_{k}(1 \leq j \leq n)$ are the unknowns.
9.29 Example. Take $n=2, m=3$ and consider the mapping $\mathbf{f}=\left(f_{1}, f_{2}\right)$ of $\mathbb{R}^{5}$ into $\mathbb{R}^{2}$ given by

$$
\begin{aligned}
& f_{1}\left(x_{1}, x_{2}, y_{1}, y_{2}, y_{3}\right)=2 e^{x_{1}}+x_{2} y_{1}-4 y_{2}+3 \\
& f_{2}\left(x_{1}, x_{2}, y_{1}, y_{2}, y_{3}\right)=x_{2} \cos x_{1}-6 x_{1}+2 y_{1}-y_{3}
\end{aligned}
$$

If $\mathbf{a}=(0,1)$ and $\mathbf{b}=(3,2,7)$, then $\mathbf{f}(\mathbf{a}, \mathbf{b})=\mathbf{0}$.
With respect to the standard bases, the matrix of the transformation $A=\mathbf{f}^{\prime}(\mathbf{a}, \mathbf{b})$ is

$$
[A]=\left[\begin{array}{cccc}
2 & 3 & 1 & -4 & 0 \\
-6 & 1 & 2 & 0 & -1
\end{array}\right]
$$

Hence

$$
\left[A_{x}\right]=\left[\begin{array}{cc}
2 & 3 \\
-6 & 1
\end{array}\right], \quad\left[A_{y}\right]=\left[\begin{array}{ccc}
1 & -4 & 0 \\
2 & 0 & -1
\end{array}\right]
$$

We see that the column vectors of $\left[A_{x}\right]$ are independent. Hence $A_{x}$ is invertible and the implicit function theorem asserts the existence of a $\mathscr{C}^{1}$-mapping $\mathbf{g}$, defined in a neighborhood of $(3,2,7)$, such that $\mathbf{g}(3,2,7)=(0,1)$ and $\mathbf{f}(\mathbf{g}(\mathbf{y}), \mathbf{y})=\mathbf{0}$.

We can use (9.58) to compute $\mathbf{g}^{\prime}(3,2,7)$ : Since

$$
\left[\left(A_{x}\right)^{-1}\right]=\left[A_{x}\right]^{-1}=\frac{1}{20}\left[\begin{array}{cc}
1 & -3 \\
6 & 2
\end{array}\right]
$$

(9.58) gives

$$
\left[\mathbf{g}^{\prime}(3,2,7)\right]=-\frac{1}{20}\left[\begin{array}{cc}
1 & -3 \\
6 & 2
\end{array}\right]\left[\begin{array}{ccc}
1 & -4 & 0 \\
2 & 0 & -1
\end{array}\right]=\left[\begin{array}{ccc}
1 & \frac{1}{2} & \frac{1}{2} & -\frac{3}{10} \\
-\frac{1}{2} & \frac{5}{5} & \frac{10}{10}
\end{array}\right]
$$

In terms of the partial derivatives, the conclusion is that

$$
\begin{array}{lll}
D_{1} g_{1}=\frac{1}{4} & D_{2} g_{1}=\frac{1}{5} & D_{3} g_{1}=-\frac{3}{20} \\
D_{1} g_{2}=-\frac{1}{2} & D_{2} g_{2}=\frac{6}{5} & D_{3} g_{2}=\frac{1}{10}
\end{array}
$$

at the point $(3,2,7)$.

# THE RANK THEOREM 

Although this theorem is not as important as the inverse function theorem or the implicit function theorem, we include it as another interesting illustration of the general principle that the local behavior of a continuously differentiable mapping $\mathbf{F}$ near a point $\mathbf{x}$ is similar to that of the linear transformation $\mathbf{F}^{\prime}(\mathbf{x})$. Before stating it, we need a few more facts about linear transformations.
9.30 Definitions. Suppose $X$ and $Y$ are vector spaces and $A \in L(X, Y)$, as in Definition 9.6. The null space of $A, \mathscr{N}(A)$, is the set of all $x \in X$ at which $A x=\mathbf{0}$. It is clear that $\mathscr{N}(A)$ is a vector space in $X$.

Likewise, the range of $A, \mathscr{R}(A)$, is a vector space in $Y$. The rank of $A$ is defined to be the dimension of $\mathscr{R}(\mathrm{A})$.

For example, the invertible elements of $L\left(\mathbb{R}^{n}\right)$ are precisely those whose rank is $n$. This follows from Theorem 9.5. If $A \in L(X, Y)$ and $A$ has rank 0 , then $A x=\mathbf{0}$ for all $x \in X$, hence $\mathscr{N}(A)=X$. In this connection, see Exercise 9.25.
9.31 Definition (Projections). Let $X$ be a vector space. An operator $P \in L(X)$ is said to be a projection in $X$ if $P^{2}=P$.

More explicitly, the requirement is that $P(P \mathbf{x})=P \mathbf{x}$ for every $\mathbf{x} \in X$. In other words, P fixes every vector in its range $\mathscr{R}(\mathrm{P})$. Here are some elementary properties of projections:
(a) If $P$ is a projection in $X$, then every $x \in X$ has a unique representation of the form

$$
\mathbf{x}=\mathbf{x}_{1}+\mathbf{x}_{2}
$$

where $\mathbf{x}_{1} \in \mathscr{R}(\mathrm{P}), \mathbf{x}_{2} \in \mathscr{N}(\mathrm{P})$.
Proof. To obtain the representation, put $\mathbf{x}_{1}=\mathrm{Px}, \mathbf{x}_{2}=\mathbf{x}-\mathbf{x}_{1}$. Then $\mathrm{Px}_{2}=$ $\mathrm{Px}-\mathrm{Px}_{1}=\mathrm{Px}-\mathrm{P}^{2} \mathbf{x}=0$. As regards the uniqueness, apply P to the equation $\mathbf{x}=\mathbf{x}_{1}+\mathbf{x}_{2}$. Since $\mathbf{x}_{1} \in \mathscr{R}(\mathrm{P}), \mathrm{Px}_{1}=\mathbf{x}_{1}$; since $\mathrm{Px}_{2}=0$, it follows that $\mathbf{x}_{1}=\mathrm{Px}$.
(b) If $X$ is a finite-dimensional vector space and if $X_{1}$ is a vector space in $X$, then there is a projection $P$ in $X$ with $\mathscr{R}(P)=X_{1}$.

Proof. If $X_{1}$ contains only 0 , this is trivial: put $P x=0$ for all $x \in X$.
Assume $\operatorname{dim} X_{1}=k>0$. By Theorem 9.3, $X$ has then a basis $\left\{\mathbf{u}_{1}, \ldots, \mathbf{u}_{n}\right\}$ such that $\left\{\mathbf{u}_{1}, \ldots, \mathbf{u}_{k}\right\}$ is a basis if $X_{1}$. Define

$$
P\left(c_{1} \mathbf{u}_{1}+\cdots+c_{n} \mathbf{u}_{n}\right)=c_{1} \mathbf{u}_{1}+\cdots+c_{k} \mathbf{u}_{k}
$$

for arbitrary scalars $c_{1}, \ldots, c_{n}$. Then $P x=x$ for every $x \in X_{1}$ and $X_{1}=\mathscr{R}(P)$.
Note that $\left\{\mathbf{u}_{k+1}, \ldots, \mathbf{u}_{n}\right\}$ is a basis of $\mathscr{N}(P)$. Note also that there are infinitely many projections in $X$ with range $X_{1}$ if $0<\operatorname{dim} X_{1}<\operatorname{dim} X$.
9.32 Theorem. Suppose $\mathrm{m}, \mathrm{n}, \tau$ are nonnegative integers, $\mathrm{m} \geq \tau, \mathrm{n} \geq \tau, \mathbf{F}$ is a $\mathscr{C}^{1}$ mapping of an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{m}}$, and $\mathbf{F}^{\prime}(\mathbf{x})$ has rank $\tau$ for every $\mathbf{x} \in \mathrm{E}$.

Fix $\mathbf{a} \in \mathrm{E}$, put $\mathrm{A}=\mathbf{F}^{\prime}(\mathbf{a})$, let $\mathrm{Y}_{1}$ be the range of A , and let P be a projection in $\mathbb{R}^{\mathrm{m}}$ whose range is $Y_{1}$. Let $Y_{2}$ be the null space of $P$.

Then there are open sets $U$ and $V$ in $\mathbb{R}^{n}$, with $\mathbf{a} \in U, U \subset E$, and there is a 1-1 $\mathscr{C}^{1}$-mapping $\mathbf{H}$ of $V$ onto $U$ (whose inverse is also of class $\mathscr{C}^{1}$ ) such that

$$
\mathbf{F}(\mathbf{H}(\mathbf{x}))=A \mathbf{x}+\varphi(A \mathbf{x}) \quad(\mathbf{x} \in V)
$$

where $\varphi$ is a $\mathscr{C}^{1}$-mapping of the open set $A(V) \subset Y_{1}$ into $Y_{2}$.
After the proof we shall give a more geometric description of the information that (9.66) contains.

Proof. If $\tau=0$, Theorem 9.19 shows that $\mathbf{F}(\mathbf{x})$ is constant in a neighborhood $U$ of a and (9.66) holds trivially with $V=U, \mathbf{H}(\mathbf{x})=\mathbf{x}, \varphi(0)=\mathbf{F}(\mathbf{a})$.

From now on we assume $\tau>0$. Since $\operatorname{dim} Y_{1}=\tau, Y_{1}$ has a basis $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{\tau}\right\}$. Choose $\mathbf{z}_{\mathrm{i}} \in \mathbb{R}^{\mathrm{n}}$ so that $A \mathbf{z}_{\mathrm{i}}=\mathbf{y}_{\mathrm{i}}(1 \leq \mathrm{i} \leq \tau)$, and define a linear mapping $S$ of $Y_{1}$ into $\mathbb{R}^{n}$ by setting

$$
S\left(c_{1} \mathbf{y}_{1}+\cdots+c_{\tau} \mathbf{y}_{\tau}\right)=c_{1} \mathbf{z}_{1}+\cdots+c_{\tau} \mathbf{z}_{\tau}
$$

for all scalars $c_{1}, \ldots, c_{r}$. Then $A S y_{i}=A z_{i}=y_{i}$ for $1 \leq i \leq r$. Thus

$$
A S \mathbf{y}=\mathbf{y} \quad\left(\mathbf{y} \in Y_{1}\right)
$$

Define a mapping $\mathbf{G}$ into $\mathbb{R}^{n}$ by setting

$$
\mathbf{G}(\mathbf{x})=\mathbf{x}+\operatorname{SP}[\mathbf{F}(\mathbf{x})-A \mathbf{x}] \quad(\mathbf{x} \in \mathrm{E})
$$

Since $\mathbf{F}^{\prime}(\mathbf{a})=A$, differentiation of (9.69) shows that $\mathbf{G}^{\prime}(\mathbf{a})=I$, the identity operator on $\mathbb{R}^{n}$. By the inverse function theorem, there are open sets $U$ and $V$ in $\mathbb{R}^{n}$, with $\mathbf{a} \in \mathrm{U}$, such that $\mathbf{G}$ is a 1-1 mapping of U onto V whose inverse $\mathbf{H}$ is also of class $\mathscr{C}^{1}$. Moreover, by shrinking $U$ and $V$, if necessary, we can arrange it so that $V$ is convex and $\mathbf{H}^{\prime}(\mathbf{x})$ is invertible for every $\mathbf{x} \in V$.

Note that ASPA $=$ A since PA $=$ A and (9.68) holds. Therefore (9.69) gives

$$
A \mathbf{G}(\mathbf{x})=\operatorname{PF}(\mathbf{x}) \quad(\mathbf{x} \in \mathrm{E})
$$

In particular, (9.70) holds for $\mathbf{x} \in \mathrm{U}$. If we replace $\mathbf{x}$ by $\mathbf{H}(\mathbf{x})$, we obtain

$$
\operatorname{PF}(\mathbf{H}(\mathbf{x}))=\mathrm{Ax} \quad(\mathbf{x} \in \mathrm{~V})
$$

Define

$$
\psi(\mathbf{x})=\mathbf{F}(\mathbf{H}(\mathbf{x}))-\mathrm{Ax} \quad(\mathbf{x} \in \mathrm{~V})
$$

Since $\mathrm{PA}=\mathrm{A},(9.71)$ implies that $\mathrm{P} \psi(\mathbf{x})=\mathbf{0}$ for all $\mathbf{x} \in \mathrm{V}$. This $\psi$ is a $\mathscr{C}^{1}$-mapping of $V$ into $Y_{2}$. Since $V$ is open it is clear that $A(V)$ is an open subset of its range $\mathscr{R}(\mathrm{A})=Y_{1}$.

To complete the proof, i.e., to go from (9.72) to (9.66), we have to show that there is a $\mathscr{C}^{1}$-mapping $\varphi$ of $A(V)$ into $Y_{2}$ which satisfies

$$
\varphi(A \mathbf{x})=\psi(\mathbf{x}) \quad(\mathbf{x} \in V)
$$

As a step toward (9.73), we will first prove that

$$
\psi\left(\mathbf{x}_{1}\right)=\psi\left(\mathbf{x}_{2}\right)
$$

if $\mathbf{x}_{1} \in V, \mathbf{x}_{2} \in V, A \mathbf{x}_{1}=A \mathbf{x}_{2}$.
Put $\Phi(\mathbf{x})=\mathbf{F}(\mathbf{H}(\mathbf{x}))$ for $\mathbf{x} \in V$. Since $\mathbf{H}^{\prime}(\mathbf{x})$ has rank n for every $\mathbf{x} \in V$ and $\mathbf{F}^{\prime}(\mathbf{x})$ has rank $r$ for every $\mathbf{x} \in \mathrm{U}$, it follows that

$$
\operatorname{rank} \Phi^{\prime}(\mathbf{x})=\operatorname{rank} \mathbf{F}^{\prime}(\mathbf{H}(\mathbf{x})) \mathbf{H}^{\prime}(\mathbf{x})=\mathrm{r} \quad(\mathbf{x} \in V)
$$

Fix $\mathbf{x} \in V$. Let $M$ be the range of $\Phi^{\prime}(\mathbf{x})$. Then $M \subset \mathbb{R}^{m}, \operatorname{dim} M=r$. By (9.71),

$$
\mathrm{P} \Phi^{\prime}(\mathbf{x})=\mathrm{A}
$$

Thus $P$ maps $M$ onto $\mathscr{R}(A)=Y_{1}$. Since $M$ and $Y_{1}$ have the same dimension, it

follows that P (restricted to M ) is 1-1.
Suppose now that $A \mathbf{h}=\mathbf{0}$. Then $P \Phi^{\prime}(\mathbf{x}) \mathbf{h}=\mathbf{0}$ by (9.76). But $\Phi^{\prime}(\mathbf{x}) \mathbf{h} \in M$ and $P$ is 1-1 on $M$. Hence $\Phi^{\prime}(\mathbf{x}) \mathbf{h}=\mathbf{0}$. A look at (9.72) shows now that we have proved the following:

If $\mathbf{x} \in V$ and $A \mathbf{h}=\mathbf{0}$, then $\psi^{\prime}(\mathbf{x}) \mathbf{h}=\mathbf{0}$.
We can now prove (9.74). Suppose $\mathbf{x}_{1} \in V, \mathbf{x}_{2} \in V, A \mathbf{x}_{1}=A \mathbf{x}_{2}$. Put $\mathbf{h}=\mathbf{x}_{2}-\mathbf{x}_{1}$ and define

$$
\mathbf{g}(\mathrm{t})=\psi\left(\mathbf{x}_{1}+\mathrm{th}\right) \quad(0 \leq \mathrm{t} \leq 1)
$$

The convexity of $V$ shows that $\mathbf{x}_{1}+t \mathbf{h} \in V$ for these $t$. Hence

$$
\mathbf{g}^{\prime}(\mathrm{t})=\psi^{\prime}\left(\mathbf{x}_{1}+\mathrm{th}\right) \mathbf{h}=\mathbf{0} \quad(0 \leq \mathrm{t} \leq 1)
$$

so that $\mathbf{g}(1)=\mathbf{g}(0)$. But $\mathbf{g}(1)=\psi\left(\mathbf{x}_{2}\right)$ and $\mathbf{g}(0)=\psi\left(\mathbf{x}_{1}\right)$. This proves (9.74).
By (9.74), $\psi(\mathbf{x})$ depends only on $A \mathbf{x}$ for $\mathbf{x} \in V$. Hence (9.73) defines $\varphi$ unambiguously in $A(V)$. It only remains to be proved that $\varphi \in \mathscr{C}^{1}$.

Fix $\mathbf{y}_{0} \in A(V)$, fix $\mathbf{x}_{0} \in V$ so that $A \mathbf{x}_{0}=\mathbf{y}_{0}$. Since $V$ is open, $\mathbf{y}_{0}$ was a neighborhood $W$ in $Y_{1}$ such that the vector

$$
\mathbf{x}=\mathbf{x}_{0}+S\left(\mathbf{y}-\mathbf{y}_{0}\right)
$$

lies in $V$ for all $\mathbf{y} \in W$. By (9.68),

$$
A \mathbf{x}=A \mathbf{x}_{0}+\mathbf{y}-\mathbf{y}_{0}=\mathbf{y}
$$

Thus (9.73) and (9.79) give

$$
\varphi(\mathbf{y})=\psi\left(\mathbf{x}_{0}-S \mathbf{y}_{0}+S \mathbf{y}\right) \quad(\mathbf{y} \in W)
$$

This formula shows that $\varphi \in \mathscr{C}^{1}$ in $W$, hence in $A(V)$, since $\mathbf{y}_{0}$ was chosen arbitrarily in $A(V)$. The proof is now complete.

Here is what the theorem tells us about the geometry of the mapping $\mathbf{F}$. If $\mathbf{y} \in \mathbf{F}(\mathrm{U})$ then $\mathbf{y}=\mathbf{F}(\mathbf{H}(\mathbf{x}))$ for some $\mathbf{x} \in V$ and (9.66) shows that $P \mathbf{y}=A \mathbf{x}$. Therefore

$$
\mathbf{y}=P \mathbf{y}+\varphi(P \mathbf{y}) \quad(\mathbf{y} \in \mathbf{F}(\mathrm{U}))
$$

This shows that $\mathbf{y}$ is determined by its projection $P \mathbf{y}$ and that $P$, restricted to $\mathbf{F}(U)$, is a 1-1 mapping of $\mathbf{F}(\mathrm{U})$ onto $A(V)$. Thus $\mathbf{F}(U)$ is an " $r$-dimensional surface" with precisely one point "over" each point of $A(V)$. We may also regard $\mathbf{F}(U)$ as the graph of $\varphi$.

If $\Phi(\mathbf{x})=\mathbf{F}(\mathbf{H}(\mathbf{x}))$, as in the proof, then (9.66) shows that the level sets of $\Phi$ (these are the sets in which $\Phi$ attains a given value) are precisely the level sets of $A$

in V . These are "flat" since they are intersections with V of translates of the vector space $\mathscr{N}(\mathrm{A})$. Note that $\operatorname{dim} \mathscr{N}(\mathrm{A})=\mathrm{n}-\mathrm{r}$ (Exercise 9.25).

The level sets of $\mathbf{F}$ in $U$ are the images under $\mathbf{H}$ of the flat level sets of $\Phi$ in $V$. They are thus " $(n-r)$-dimensional surfaces" in $U$.

# DETERMINANTS 

Determinants are numbers associated to square matrices, and hence to the operators represented by such matrices. They are 0 if and only if the corresponding operator fails to be invertible. They can therefore be used to decide whether the hypotheses of some of the preceding theorems are satisfied. They will play an even more important role in Chap. 10.
9.33 Definition. If $\left(j_{1}, \ldots, j_{n}\right)$ is an ordered $n$-tuple of integers, define

$$
s\left(j_{1}, \ldots, j_{n}\right)=\prod_{p<q} \operatorname{sgn}\left(j_{q}-j_{p}\right)
$$

where $\operatorname{sgn} x=1$ if $x>0, \operatorname{sgn} x=-1$ if $x<0, \operatorname{sgn} x=0$ if $x=0$. Then $s\left(j_{1}, \ldots, j_{n}\right)=1,-1$, or 0 , and it changes sign if any two of the $j$ 's are interchanged.

Let $[A]$ be the matrix of a linear operator $A$ on $\mathbb{R}^{n}$, relative to the standard basis $\left(\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right)$, with entries $a(i, j)$ in the $i$ th row and $j$ th column. The determinant of $[A]$ is defined to be the number

$$
\operatorname{det}[A]=\sum s\left(j_{1}, \ldots, j_{n}\right) a\left(1, j_{1}\right) a\left(2, j_{2}\right) \cdots a\left(n, j_{n}\right)
$$

The sum in (9.83) extends over all ordered $n$-tuples of integers $\left(j_{1}, \ldots, j_{n}\right)$ with $1 \leq j_{r} \leq n$. The column vectors $x_{j}$ of $[A]$ are

$$
\mathbf{x}_{j}=\sum_{i=1}^{n} a(i, j) \mathbf{e}_{i} \quad(1 \leq j \leq n)
$$

It will be convenient to think of $\operatorname{det}[A]$ as a function of the column vectors $[A]$. If we write

$$
\operatorname{det}\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)=\operatorname{det}[A]
$$

det is now a real function on the set of all ordered $n$-tuples of vectors in $\mathbb{R}^{n}$.

### 9.34 Theorem.

(a) If I is the identity operator on $\mathbb{R}^{n}$, then

$$
\operatorname{det}[I]=\operatorname{det}\left(\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right)=1
$$

(b) det is a linear function of each of the column vectors $\mathbf{x}_{j}$, if the others are held fixed.
(c) If $[A]_{1}$ is obtained from $[A]$ by interchanging two columns, then $\operatorname{det}[A]_{1}=-\operatorname{det}[A]$.

(d) If $[A]$ has two equal columns, then $\operatorname{det}[A]=0$.

Proof. If $A=I$, then $a(i, i)=1$ and $a(i, j)=0$ for all $i \neq j$. Hence

$$
\operatorname{det}[I]=s(1,2, \ldots, n)=1
$$

which proves (a). By (9.82), $s\left(j_{1}, \ldots, j_{n}\right)=0$ if any two of the $j$ 's are equal. Each of the remaining $n$ ! products in (9.83) contains exactly one factor from each column. This proves (b). Part (c) is an immediate consequence of the fact that $s\left(j_{1}, \ldots, j_{n}\right)$ changes sign if any two of the $j_{r}$ 's are interchanged, and (d) is a corollary of (c).
9.35 Theorem. If $[A]$ and $[B]$ are $n$ by $n$ matrices, then

$$
\operatorname{det}([B][A])=\operatorname{det}[B] \operatorname{det}[A]
$$

Proof. If $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$ are the columns of $[A]$, define

$$
\Delta_{\mathrm{B}}\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)=\Delta_{\mathrm{B}}[A]=\operatorname{det}([B][A])
$$

The columns of $[B][A]$ are the vectors $B \mathbf{x}_{1}, \ldots, B \mathbf{x}_{n}$. Thus

$$
\Delta_{\mathrm{B}}\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}\right)=\operatorname{det}\left(B \mathbf{x}_{1}, \ldots, B \mathbf{x}_{n}\right)
$$

By (9.86) and Theorem 9.34, $\Delta_{B}$ also has properties 9.34(b) to (d). By (b) and (9.84),

$$
\Delta_{\mathrm{B}}[A]=\Delta_{\mathrm{B}}\left(\sum_{\mathrm{i}} \mathrm{a}(\mathrm{i}, 1) \mathbf{e}_{\mathrm{i}}, \mathbf{x}_{2}, \ldots, \mathbf{x}_{n}\right)=\sum_{\mathrm{i}} \mathrm{a}(\mathrm{i}, 1) \Delta_{\mathrm{B}}\left(\mathbf{e}_{\mathrm{i}}, \mathbf{x}_{2}, \ldots, \mathbf{x}_{n}\right)
$$

Repeating this process with $\mathbf{x}_{2}, \ldots, \mathbf{x}_{n}$, we obtain

$$
\Delta_{\mathrm{B}}[A]=\sum \mathrm{a}\left(\mathrm{i}_{1}, 1\right) \mathrm{a}\left(\mathrm{i}_{2}, 2\right) \cdots \mathrm{a}\left(\mathrm{i}_{n}, n\right) \Delta_{\mathrm{B}}\left(\mathbf{e}_{\mathrm{i}_{1}}, \ldots, \mathbf{e}_{\mathrm{i}_{n}}\right)
$$

the sum being extended over all ordered n-tuples $\left(i_{1}, \ldots, i_{n}\right)$ with $1 \leq i_{r} \leq n$. By (c) and (d),

$$
\Delta_{\mathrm{B}}\left(\mathbf{e}_{\mathrm{i}_{1}}, \ldots, \mathbf{e}_{\mathrm{i}_{n}}\right)=\mathrm{t}\left(\mathrm{i}_{1}, \ldots, \mathrm{i}_{n}\right) \Delta_{\mathrm{B}}\left(\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right)
$$

where $t=1,0$, or -1 , and since $[B][I]=[B],(9.85)$ shows that

$$
\Delta_{\mathrm{B}}\left(\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right)=\operatorname{det}[B]
$$

Substituting (9.89) and (9.88) into (9.87), we obtain

$$
\operatorname{det}([B][A])=\left\{\sum a\left(i_{1}, 1\right) \cdots a\left(i_{n}, n\right) t\left(i_{1}, \ldots, i_{n}\right)\right\} \operatorname{det}[B]
$$

for all $n$ by $n$ matrices $[A]$ and $[B]$. Taking $B=I$, we see that the above sum in braces is $\operatorname{det}[A]$. This proves the theorem.

9.36 Theorem. A linear operator A on $\mathbb{R}^{n}$ is invertible if and only if $\operatorname{det}[A] \neq 0$.

Proof. If A is invertible, Theorem 9.35 shows that

$$
\operatorname{det}[A] \operatorname{det}\left[A^{-1}\right]=\operatorname{det}\left[A A^{-1}\right]=\operatorname{det}[I]=1
$$

so that $\operatorname{det}[A] \neq 0$.
If $A$ is not invertible, the columns $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$ of $[A]$ are dependent (Theorem 9.5); hence there is one, say $\mathbf{x}_{\mathrm{k}}$, such that

$$
\mathbf{x}_{\mathrm{k}}+\sum_{\mathrm{j} \neq \mathrm{k}} \mathrm{c}_{\mathrm{j}} \mathbf{x}_{\mathrm{j}}=0
$$

for certain scalars $c_{j}$. By Theorem 9.34(b) and (d), $\mathbf{x}_{k}$ can be replaced by $\mathbf{x}_{k}+$ $c_{j} \mathbf{x}_{j}$ without altering the determinant, if $j \neq k$. Repeating, we see that $\mathbf{x}_{k}$ can be replaced by the left side of (9.90), i.e., by $\mathbf{0}$, without altering the determinant. But a matrix which has $\mathbf{0}$ for one column has determinant 0 . Hence $\operatorname{det}[A]=0$.
9.37 Remark. Suppose $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{n}\right\}$ and $\left\{\mathbf{u}_{1}, \ldots, \mathbf{u}_{n}\right\}$ are bases in $\mathbb{R}^{n}$. Every linear operator $A$ on $\mathbb{R}^{n}$ determines matrices $[A]$ and $[A]_{U}$, with entries $a_{i j}$ and $\alpha_{i j}$ given by

$$
A \mathbf{e}_{j}=\sum_{i} a_{i j} \mathbf{e}_{i}, \quad A \mathbf{u}_{j} \sum_{i} \alpha_{i j} \mathbf{u}_{i}
$$

If $\mathbf{u}_{j}=B \mathbf{e}_{j}=\Sigma b_{i j} \mathbf{e}_{j}$, then $A \mathbf{u}_{j}$ is equal to

$$
\sum_{k} \alpha_{k j} B \mathbf{e}_{k}=\sum_{k} \alpha_{k j} \sum_{i} b_{i k} \mathbf{e}_{i}=\sum_{i}\left(\sum_{k} b_{i k} \alpha_{k j}\right) \mathbf{e}_{i}
$$

and also to

$$
A B \mathbf{e}_{j}=A \sum_{k} b_{k j} \mathbf{e}_{k}=\sum_{i}\left(\sum_{k} a_{i k} b_{k j}\right) \mathbf{e}_{i}
$$

Thus $\Sigma b_{i k} \alpha_{k j}=\Sigma a_{i k} b_{k j}$, or

$$
[B][A]_{U}=[A][B]
$$

Since $B$ is invertible, $\operatorname{det}[B] \neq 0$. Hence (9.91), combined with Theorem 9.35, shows that

$$
\operatorname{det}[A]_{U}=\operatorname{det}[A]
$$

The determinant of the matrix of a linear operator therefore does not depend on the basis which is used to construct the matrix. It is thus meaningful to speak of the determinant of a linear operator, without having any basis in mind.
9.38 Definition (Jacobians). If $\mathbf{f}$ maps an open set $E \subset \mathbb{R}^{n}$ into $\mathbb{R}^{n}$ and $\mathbf{f}$ is differentiable at a point $\mathbf{x} \in E$, the determinant of the linear operator $\mathbf{f}^{\prime}(\mathbf{x})$ is called the

Jacobian of $\mathbf{f}$ at $\mathbf{x}$. In symbols,

$$
J_{f}(\mathbf{x})=\operatorname{det} \mathbf{f}^{\prime}(\mathbf{x})
$$

We shall also use the notation

$$
\frac{\partial\left(y_{1}, \ldots, y_{n}\right)}{\partial\left(x_{1}, \ldots, x_{n}\right)}
$$

for $J_{f}(\mathbf{x})$ if $\left(y_{1}, \ldots, y_{n}\right)=\mathbf{f}\left(x_{1}, \ldots, x_{n}\right)$.
In terms of Jacobians, the crucial hypothesis in the inverse function theorem is that $J_{f}(\mathbf{a}) \neq 0$ (compare Theorem 9.36). If the implicit function theorem is stated in terms of the functions (9.59), the assumption made there on A amounts to

$$
\frac{\partial\left(\mathrm{f}_{1}, \ldots, \mathrm{f}_{\mathrm{n}}\right)}{\partial\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{n}}\right)} \neq 0
$$

# DERIVATIVES OF HIGHER ORDER 

9.39 Definition. Suppose $f$ is a real function defined in an open set $E \subset \mathbb{R}^{n}$, with partial derivatives $D_{1} f, \ldots, D_{n} f$. If the functions $D_{j} f$ are themselves differentiable, then the second-order partial derivatives of $f$ are defined by

$$
D_{i j} f=D_{i} D_{j} f \quad(i, j=1, \ldots, n)
$$

If all these functions $D_{i j} f$ are continuous in $E$, we say that $f$ is of class $\mathscr{C}^{2}$ in $E$, or that $f \in \mathscr{C}^{2}(E)$. A mapping $f$ of $E$ into $\mathbb{R}^{m}$ is said to be of class $\mathscr{C}^{2}$ if each component of $\mathbf{f}$ is of class $\mathscr{C}^{2}$.

It can happen that $D_{i j} f \neq D_{j i} f$ at some point, although both derivatives exist (see Exercise 9.27). However, we shall see below that $D_{i j} f=D_{j i} f$ whenever these derivatives are continuous.

For simplicity (and without loss of generality), we state our next two theorems for real functions of two variables. The first one is a mean value theorem.
9.40 Theorem. Suppose $f$ is defined in an open set $E \subset \mathbb{R}^{2}$ and $D_{1} f$ and $D_{21} f$ exist at every point of E. Suppose $\mathrm{Q} \subset \mathrm{E}$ is a closed rectangle with sides parallel to the coordinate axes, having $(a, b)$ and $(a+h, b+k)$ as opposite vertices $(h \neq 0, k \neq 0)$. Put

$$
\Delta(f, Q)=f(a+h, b+k)-f(a+h, b)-f(a, b+k)+f(a, b)
$$

Then there is a point $(x, y)$ in the interior of $Q$ such that

$$
\Delta(f, Q)=h k\left(D_{21} f\right)(x, y)
$$

Note that analogy between (9.95) and Theorem 5.10; the area of $Q$ is hk.

Proof. Put $u(t)=f(t, b+k)-f(t, b)$. Two applications of Theorem 5.10 show that there is an $x$ between $a$ and $a+h$, and that there is a $y$ between $b$ and $b+k$, such that

$$
\begin{aligned}
\Delta(f, Q) & =u(a+h)-u(a) \\
& =h u^{\prime}(x) \\
& =h\left[\left(D_{1} f\right)(x, b+k)-\left(D_{1} f\right)(x, b)\right] \\
& =h k\left(D_{21} f\right)(x, y)
\end{aligned}
$$

9.41 Theorem. Suppose $f$ is defined in an open set $E \subset \mathbb{R}^{2}$, suppose that $D_{1} f, D_{21} f$, and $\mathrm{D}_{2} \mathrm{f}$ exist at every point of E , and $\mathrm{D}_{21} \mathrm{f}$ is continuous at some point $(\mathrm{a}, \mathrm{b}) \in \mathrm{E}$. Then $\mathrm{D}_{12} \mathrm{f}$ exists at $(\mathrm{a}, \mathrm{b})$ and

$$
\left(D_{12} f\right)(a, b)=\left(D_{21} f\right)(a, b)
$$

Corollary. $\mathrm{D}_{21} \mathrm{f}=\mathrm{D}_{12} \mathrm{f}$ if $\mathrm{f} \in \mathscr{C}^{2}(\mathrm{E})$.
Proof. Put $A=\left(D_{21} f\right)(a, b)$. Choose $\varepsilon>0$. If $Q$ is a rectangle as in Theorem 9.40 and if $h$ and $k$ are sufficiently small, we have

$$
\left|A-\left(D_{21} f\right)(x, y)\right|<\varepsilon
$$

for all $(x, y) \in Q$. Thus

$$
\left|\frac{\Delta(f, Q)}{h k}-A\right|<\varepsilon
$$

by (9.95). Fix $h$ and let $k \rightarrow 0$. Since $D_{2} f$ exists in $E$, the last inequality implies that

$$
\left|\frac{\left(D_{2} f\right)(a+h, b)-\left(D_{2} f\right)(a, b)}{h}-A\right| \leq \varepsilon
$$

Since $\varepsilon$ was arbitrary, and since (9.97) holds for all sufficiently small $h \neq 0$, it follows that $\left(D_{12} f\right)(a, b)=A$. This gives (9.96).

# DIFFERENTIATION OF INTEGRALS 

Suppose $\varphi$ is a function of two variables which can be integrated with respect to one and which can be differentiated with respect to the other. Under what conditions will the result be the same if these two limit processes are carried out in the opposite order? To state the question more precisely: Under what conditions on $\varphi$ can one prove that the equation

$$
\frac{d}{d t} \int_{a}^{b} \varphi(x, t) d x=\int_{a}^{b} \frac{\partial \phi}{\partial t}(x, t) d x
$$

is true? (A counter example is furnished by Exercise 9.28.)

It will be convenient to use the notation

$$
\varphi^{\mathrm{t}}(\mathrm{x})=\varphi(\mathrm{x}, \mathrm{t})
$$

Thus $\varphi^{\mathrm{t}}$ is, for each $t$, a function of one variable.

# 9.42 Theorem. Suppose 

(a) $\varphi(\mathrm{x}, \mathrm{t})$ is defined for $\mathrm{a} \leq \mathrm{x} \leq \mathrm{b}, \mathrm{c} \leq \mathrm{t} \leq \mathrm{d}$;
(b) $\alpha$ is an increasing function on $[\mathrm{a}, \mathrm{b}]$;
(c) $\varphi^{\mathrm{t}} \in \mathscr{R}(\alpha)$ for every $\mathrm{t} \in[\mathrm{c}, \mathrm{d}]$;
(d) $\mathrm{c}<\mathrm{s}<\mathrm{d}$, and to every $\varepsilon>0$ corresponds a $\delta>0$ such that

$$
\left|\left(\mathrm{D}_{2} \varphi\right)(\mathrm{x}, \mathrm{t})-\left(\mathrm{D}_{2} \varphi\right)(\mathrm{x}, \mathrm{~s})\right|<\varepsilon
$$

for all $\mathrm{x} \in[\mathrm{a}, \mathrm{b}]$ and for all $\mathrm{t} \in(\mathrm{s}-\delta, \mathrm{s}+\delta)$.
Define

$$
f(t)=\int_{a}^{b} \varphi(x, t) d \alpha(x) \quad(c \leq t \leq d)
$$

Then $\left(\mathrm{D}_{2} \varphi\right)^{\mathrm{s}} \in \mathscr{R}(\alpha), \mathrm{f}^{\prime}(\mathrm{s})$ exists, and

$$
f^{\prime}(s)=\int_{a}^{b}\left(D_{2} \varphi\right)(x, s) d \alpha(x)
$$

Note that (c) simply asserts the existence of the integrals (9.100) for all $t \in[c, d]$. Note also that (d) certainly holds whenever $\left(D_{2} \varphi\right)$ is continuous on the rectangle on which $\varphi$ is defined.

Proof. Consider the difference quotients

$$
\psi(x, t)=\frac{\varphi(x, t)-\varphi(x, s)}{t-s}
$$

for $0<|t-s|<\delta$. By Theorem 5.10 there corresponds to each $(x, t)$ a number $u$ between $s$ and $t$ such that

$$
\psi(x, t)=\left(D_{2} \varphi\right)(x, u)
$$

Hence (d) implies that

$$
\left|\psi(x, t)-\left(D_{2} \varphi\right)(x, s)\right|<\varepsilon \quad\left(a \leq x \leq b, 0<|t-s|<\delta\right)
$$

Note that

$$
\frac{f(t)-f(s)}{t-s}=\int_{a}^{b} \psi(x, t) d \alpha(x)
$$

By (9.102), $\psi^{\mathrm{t}} \rightarrow\left(\mathrm{D}_{2} \varphi\right)^{\mathrm{s}}$ uniformly on $[\alpha, \mathrm{b}]$ as $\mathrm{t} \rightarrow \mathrm{s}$. Since each $\psi^{\mathrm{t}} \in \mathscr{R}(\alpha)$, the desired conclusion follows from (9.103) and Theorem 7.16.
9.43 Example. One can of course prove analogues of Theorem 9.42 with $(-\infty, \infty)$ in place of $[\alpha, \mathrm{b}]$. Instead of doing this, let us simply look at an example. Define

$$
f(t)=\int_{-\infty}^{\infty} e^{-x^{2}} \cos (x t) d x
$$

and

$$
g(t)=-\int_{-\infty}^{\infty} x e^{-x^{2}} \sin (x t) d x
$$

for $-\infty<\mathrm{t}<\infty$. Both integrals exist (they converge absolutely) since the absolute values of the integrands are at most $\exp \left(-x^{2}\right)$ and $|x| \exp \left(-x^{2}\right)$, respectively.

Note that $g$ is obtained from $f$ by differentiating the integrand with respect to t . We claim that f is differentiable and that

$$
f^{\prime}(t)=g(t) \quad(-\infty<t<\infty)
$$

To prove this, let us first examine the difference quotients of the cosine: if $\beta>0$, then

$$
\frac{\cos (\alpha+\beta)-\cos \alpha}{\beta}+\sin \alpha=\frac{1}{\beta} \int_{\alpha}^{\alpha+\beta}(\sin \alpha-\sin t) d t
$$

Since $|\sin \alpha-\sin t| \leq|t-\alpha|$, the right side of (9.107) is at most $\beta / 2$ in absolute value; the case $\beta<0$ is handled similarly. Thus

$$
\left|\frac{\cos (\alpha+\beta)-\cos \alpha}{\beta}+\sin \alpha\right| \leq|\beta|
$$

for all $\beta$ (if the left side is interpreted to be 0 when $\beta=0$ ).
Now, fix $t$ and $h \neq 0$. Apply (9.108) with $\alpha=\mathrm{xt}, \beta=\mathrm{xh}$; it follows from (9.104) and (9.105) that

$$
\left|\frac{f(t+h)-f(t)}{h}-g(t)\right| \leq|h| \int_{-\infty}^{\infty} x^{2} e^{-x^{2}} d x
$$

When $\mathrm{h} \rightarrow 0$, we thus obtain (9.106).
Let us go a step further: An integration by parts, applied to (9.104), shows that

$$
f(t)=2 \int_{-\infty}^{\infty} x e^{-x^{2}} \frac{\sin (x t)}{t} d x
$$

Thus $\operatorname{tf}(\mathrm{t})=-2 \mathrm{~g}(\mathrm{t})$ and (9.106) implies now that f satisfies the differential equa-

tion

$$
2 f^{\prime}(t)+t f(t)=0
$$

If we solve this differential equation and use the fact that $f(0)=\sqrt{\pi}$ (see Theorem 8.21), we find that

$$
f(t)=\sqrt{\pi} \exp \left(-\frac{t^{2}}{4}\right)
$$

The integral in (9.104) is thus explicitly determined.

# EXERCISES 

9.1. If $S$ is a nonempty subset of a vector space $X$, prove (as asserted in Definition 9.1) that the span of $S$ is a vector space.
9.2. Prove (as asserted in Definition 9.6) that $B A$ is linear if $A$ and $B$ are linear transformations. Prove also that $A^{-1}$ is linear and invertible.
9.3. Assume $A \in L(X, Y)$ and $A \mathbf{x}=\mathbf{0}$ only when $\mathbf{x}=\mathbf{0}$. Prove that $A$ is then 1-1.
9.4. Prove (as asserted in Definition 9.30) that null spaces and ranges of linear transformations are vector spaces.
9.5. Prove that to every $A \in L\left(\mathbb{R}^{n}, \mathbb{R}^{1}\right)$ corresponds a unique $\mathbf{y} \in \mathbb{R}^{n}$ such that $A \mathbf{x}=\mathbf{x} \cdot \mathbf{y}$. Prove also that $\|A\|=|\mathbf{y}|$. Hint: Under certain conditions, equality holds in the Schwarz inequality.
9.6. If $f(0,0)=0$ and

$$
f(x, y)=\frac{x y}{x^{2}+y^{2}} \quad \text { if }(x, y) \neq(0,0)
$$

prove that $\left(D_{1} f\right)(x, y)$ and $\left(D_{2} f\right)(x, y)$ exist at every point of $\mathbb{R}^{2}$, although $f$ is not continuous at $(0,0)$.
9.7. Suppose that $f$ is a real-valued function defined in an open set $E \subset \mathbb{R}^{n}$ and that the partial derivatives $D_{1} f, \ldots, D_{n} f$ are bounded in $E$. Prove that $f$ is continuous in E. Hint: Proceed as in the proof of Theorem 9.21.
9.8. Suppose that $f$ is a differentiable real function in an open set $E \subset \mathbb{R}^{n}$ into $\mathbb{R}^{m}$ and that $f$ has a local maximum at a point $\mathbf{x} \in E$. Prove that $f^{\prime}(\mathbf{x})=0$.
9.9. If $\mathbf{f}$ is a differentiable mapping of a connected open set $E \subset \mathbb{R}^{n}$, and if $\mathbf{f}^{\prime}(\mathbf{x})=0$ for every $\mathbf{x} \in E$, prove that $\mathbf{f}$ is a constant in $E$.
9.10. If $f$ is a real function defined in a convex open set $E \subset \mathbb{R}^{n}$, such that $\left(D_{1} f\right)(\mathbf{x})=0$ for every $\mathbf{x} \in E$, prove that $f(\mathbf{x})$ depends only on $x_{2}, \ldots, x_{n}$.

Show that the convexity of $E$ can be replaced by a weaker condition, but that some condition is required. For example, if $n=2$ and $E$ is shaped like a horseshoe, the statement may be false.
9.11. If $f$ and $g$ are differentiable real functions in $\mathbb{R}^{n}$, prove that

$$
\nabla(f g)=f \nabla g+g \nabla f
$$

and that $\nabla(1 / f)=-f^{-2} \nabla f$ whenever $f \neq 0$.

9.12. Fix two real numbers $a$ and $b, 0<a<b$. Define a mapping $f=\left(f_{1}, f_{2}, f_{3}\right)$ of $\mathbb{R}^{2}$ into $\mathbb{R}^{3}$ by

$$
\begin{aligned}
& f_{1}(s, t)=(b+a \cos s) \cos t \\
& f_{2}(s, t)=(b+a \cos s) \sin t \\
& f_{3}(s, t)=a \sin s
\end{aligned}
$$

Describe the range K of $\mathbf{f}$. (It is a certain compact subset of $\mathbb{R}^{3}$.)
(a) Show that there are exactly 4 points $\mathbf{p} \in \mathrm{K}$ such that

$$
\left(\nabla f_{1}\right)\left(f^{-1}(\mathbf{p})\right)=0
$$

Find these points.
(b) Determine the set of all $\mathbf{q} \in \mathrm{K}$ such that

$$
\left(\nabla f_{3}\right)\left(f^{-1}(\mathbf{q})\right)=0
$$

(c) Show that one of the points $\mathbf{p}$ found in part (a) corresponds to a local maximum of $f_{1}$, one corresponds to a local minimum, and that the other two are neither (they are socalled "saddle points"). Which of the points $\mathbf{q}$ found in part (b) correspond to maxima or minima?
(d) Let $\lambda$ be an irrational real number and define $\mathbf{g}(\mathrm{t})=\mathbf{f}(\mathrm{t}, \lambda \mathrm{t})$. Prove that $\mathbf{g}$ is a 1-1 mapping of $\mathbb{R}^{1}$ onto a dense subset of K . Prove that

$$
\left|\mathbf{g}^{\prime}(\mathrm{t})\right|^{2}=\mathrm{a}^{2}+\lambda^{2}(\mathrm{~b}+\mathrm{a} \cos \mathrm{t})^{2}
$$

9.13. Suppose $\mathbf{f}$ is a differentiable mapping of $\mathbb{R}^{1}$ into $\mathbb{R}^{3}$ such that $|\mathbf{f}(\mathrm{t})|=1$ for every t . Prove that $\mathbf{f}^{\prime}(\mathrm{t}) \cdot \mathbf{f}(\mathrm{t})=0$. Interpret this result geometrically.
9.14. Define $f(0,0)=0$ and

$$
f(x, y)=\frac{x^{3}}{x^{2}+y^{2}} \quad \text { if }(x, y) \neq(0,0)
$$

(a) Prove that $D_{1} f$ and $D_{2} f$ are bounded functions in $\mathbb{R}^{2}$. (Hence $f$ is continuous.)
(b) Let $\mathbf{u}$ be any unit vector in $\mathbb{R}^{2}$. Show that the directional derivative $\left(D_{u} f\right)(0,0)$ exists and that its absolute value is at most 1 .
(c) Let $\gamma$ be a differentiable mapping of $\mathbb{R}^{1}$ into $\mathbb{R}^{2}$ (in other words, $\gamma$ is a differentiable curve in $\mathbb{R}^{2}$ ) with $\gamma(0)=(0,0)$ and $\left|\gamma^{\prime}(0)\right|>0$. Put $g(t)=f(\gamma(t))$ and prove that $g$ is differentiable for every $t \in \mathbb{R}^{1}$. If $\gamma \in \mathscr{C}^{1}$, prove that $g \in \mathscr{C}^{1}$.
(d) In spite of this, prove that $f$ is not differentiable at $(0,0)$. Hint: Formula (9.40) fails.
9.15. Define $f(0,0)=0$ and put

$$
f(x, y)=x^{2}+y^{2}-2 x^{2} y-\frac{4 x^{6} y^{2}}{\left(x^{4}+y^{2}\right)^{2}}
$$

if $(x, y) \neq(0,0)$.
(a) Prove, for all $(x, y) \in \mathbb{R}^{2}$, that

$$
4 x^{4} y^{2} \leq\left(x^{4}+y^{2}\right)^{2}
$$

Conclude that $f$ is continuous.
(b) For $0 \leq \theta \leq 2 \pi,-\infty<\mathrm{t}<\infty$, define

$$
g_{\theta}(t)=f(t \cos \theta, t \sin \theta)
$$

Show that $g_{\theta}(0)=0, g_{\theta}^{\prime}(0)=0, g_{\theta}^{\prime \prime}(0)=2$. Each $g_{\theta}$ therefore has a strict local minimum at $\mathrm{t}=0$. In other words, the restriction of f to each line through $(0,0)$ has a strict local minimum at $(0,0)$.
(c) Show that $(0,0)$ is nevertheless not a local minimum for $f$, since $f\left(x, x^{2}\right)=-x^{4}$.
9.16. Show that the continuity of $\mathbf{f}^{\prime}$ at the point $\mathbf{a}$ is needed in the inverse function theorem, even in the case $n=1$ : If

$$
f(t)=t+2 t^{2} \sin \left(\frac{1}{t}\right)
$$

for $t \neq 0$ and $f(0)=0$, then $f^{\prime}(0)=1, f^{\prime}$ is bounded in $(-1,1)$, but $f$ is not one-to-one in any neighborhood of 0 .
9.17. Let $\mathbf{f}=\left\{f_{1}, f_{2}\right\}$ be the mapping of $\mathbb{R}^{2}$ into $\mathbb{R}^{2}$ given by

$$
f_{1}(x, y)=e^{x} \cos y, \quad f_{2}(x, y)=e^{x} \sin y
$$

(a) What is the range of $\mathbf{f}$ ?
(b) Show that the Jacobian of $\mathbf{f}$ is not zero at any point of $\mathbb{R}^{2}$. Thus every point of $\mathbb{R}^{2}$ has a neighborhood in which $\mathbf{f}$ is one-to-one. Nevertheless, $\mathbf{f}$ is not one-to-one on $\mathbb{R}^{2}$.
(c) Put $\mathbf{a}=(0, \pi / 3), \mathbf{b}=\mathbf{f}(\mathbf{a})$, and let $\mathbf{g}$ be the continuous inverse of $\mathbf{f}$, defined in a neighborhood of $\mathbf{b}$, such that $\mathbf{g}(\mathbf{b})=\mathbf{a}$. Find an explicit formula for $\mathbf{g}$, compute $\mathbf{f}^{\prime}(\mathbf{a})$ and $\mathbf{g}^{\prime}(\mathbf{b})$, and verify the formula (9.52).
(d) What are the images under $\mathbf{f}$ of lines parallel to the coordinate axes?
9.18. Answer analogous questions for the mapping defined by

$$
u=x^{2}-y^{2}, \quad v=2 x y
$$

9.19. Show that the system of equations

$$
\left\{\begin{array}{l}
3 x+y-z+u^{2}=0 \\
x-y+2 z+u=0 \\
2 x+2 y-3 z+2 u=0
\end{array}\right.
$$

can be solved for $x, y, u$ in terms of $z$; for $x, z, u$ in terms of $y$; for $y, z, u$ in terms of $x$; but not for $x, y, z$ in terms of $u$.
9.20. Take $n=m=1$ in the implicit function theorem, and interpret the theorem (as well as its proof) graphically.
9.21. Define $f$ in $\mathbb{R}^{2}$ by

$$
f(x, y)=2 x^{3}-3 x^{2}+2 y^{3}+3 y^{2}
$$

(a) Find the four points in $\mathbb{R}^{2}$ at which the gradient of $f$ is zero. Show that $f$ has exactly one local maximum and one local minimum in $\mathbb{R}^{2}$.
(b) Let $S$ be the set of all $(x, y) \in \mathbb{R}^{2}$ at which $f(x, y)=0$. Find the points of $S$ that have no neighborhoods in which the equation $f(x, y)=0$ can be solved for $y$ in terms of $x$ (or for $x$ in terms of $y$ ). Describe $S$ as precisely as you can.
9.22. Give a similar discussion for

$$
f(x, y)=2 x^{3}+6 x y^{2}-3 x^{2}+3 y^{2}
$$

9.23. Define $f$ in $\mathbb{R}^{3}$ by

$$
f\left(x, y_{1}, y_{2}\right)=x^{2} y_{1}+e^{x}+y_{2}
$$

Show that $f(0,1,-1)=0,\left(D_{1} f\right)(0,1,-1) \neq 0$, and that there exists therefore a differentiable function $g$ in some neighborhood of $(1,-1)$ in $\mathbb{R}^{2}$ such that $g(1,-1)=0$ and

$$
f\left(g\left(y_{1}, y_{2}\right), y_{1}, y_{2}\right)=0
$$

Find $\left(D_{1} g\right)(1,-1)$ and $\left(D_{2} g\right)(1,-1)$.
9.24. For $(x, y) \neq(0,0)$, define $\mathbf{f}=\left(f_{1}, f_{2}\right)$ by

$$
f_{1}(x, y)=\frac{x^{2}-y^{2}}{x^{2}+y^{2}}, \quad f_{2}(x, y)=\frac{x y}{x^{2}+y^{2}}
$$

Compute the rank of $\mathbf{f}^{\prime}(x, y)$ and find the range of $\mathbf{f}$.
9.25. Suppose $A \in L\left(\mathbb{R}^{n}, \mathbb{R}^{m}\right)$; let $r$ be the rank of $A$.
(a) Define $S$ as in the proof of Theorem 9.32. Show that $S A$ is a projection in $\mathbb{R}^{n}$ whose null space is $\mathscr{N}(A)$ and whose range is $\mathscr{R}(S)$. Hint: By (9.68) SASA $=S A$.
(b) Use (a) to show that

$$
\operatorname{dim} \mathscr{N}(A)+\operatorname{dim} \mathscr{R}(A)=n
$$

9.26. Show that the existence (and even the continuity) of $D_{12} f$ does not imply the existence of $D_{1} f$. For example, let $f(x, y)=g(x)$, where $g$ is nowhere differentiable.
9.27. Put $f(0,0)=0$ and

$$
f(x, y)=\frac{x y\left(x^{2}-y^{2}\right)}{x^{2}+y^{2}}
$$

if $(x, y) \neq(0,0)$. Prove that
(a) $f, D_{1} f, D_{2} f$ are continuous in $\mathbb{R}^{2}$;
(b) $D_{12} f$ and $D_{21} f$ exist at every point of $\mathbb{R}^{2}$ and are continuous except at $(0,0)$;
(c) $\left(D_{12} f\right)(0,0)=1$ and $\left(D_{21} f\right)(0,0)=-1$.
9.28. For $t \geq 0$, put

$$
\varphi(x, t)= \begin{cases}x & (0 \leq x \leq \sqrt{t}) \\ -x+2 \sqrt{t} & (\sqrt{t} \leq x \leq 2 \sqrt{t}) \\ 0 & (\text { otherwise })\end{cases}
$$

and put $\varphi(x, t)=-\varphi(x,|t|)$ if $t<0$.
Show that $\varphi$ is continuous on $\mathbb{R}^{2}$ and

$$
\left(D_{2} \varphi\right)(x, 0)=0
$$

for all $x$. Define

$$
f(t)=\int_{-1}^{1} \varphi(x, t) d x
$$

Show that $f(t)=t$ if $|t|<1 / 4$. Hence

$$
f^{\prime}(0) \neq \int_{-1}^{1}\left(D_{2} \varphi\right)(x, 0) d x
$$

9.29. Let $E$ be an open set in $\mathbb{R}^{n}$. The classes $\mathscr{C}^{1}(E)$ and $\mathscr{C}^{2}(E)$ are defined in the text. By induction, $\mathscr{C}^{k}(E)$ can be defined as follows, for all positive integers $k$ : To say that $f \in \mathscr{C}^{k}(E)$ means that the partial derivatives $D_{1} f, \ldots, D_{n} f$ belong to $\mathscr{C}^{k-1}(E)$.

Assume $f \in \mathscr{C}^{k}(E)$ and show (by repeated application of Theorem 9.41) that the kth order derivative

$$
D_{i_{1} i_{2} \ldots i_{k}} f=D_{i_{1}} D_{i_{2}} \cdots D_{i_{k}} f
$$

is unchanged if the subscripts $i_{1}, \ldots, i_{k}$ are permuted.
For instance, if $n \geq 3$, then

$$
D_{1213} f=D_{3112} f
$$

for every $f \in \mathscr{C}^{4}$.

9.30. Let $f \in \mathscr{C}^{m}(E)$, where $E$ is an open subset of $\mathbb{R}^{n}$. Fix $\mathbf{a} \in E$ and suppose $\mathbf{x} \in \mathbb{R}^{n}$ is so close to 0 that the points

$$
\mathbf{p}(\mathrm{t})=\mathbf{a}+\mathrm{tx}
$$

lie in $E$ whenever $0 \leq t \leq 1$. Define

$$
h(t)=f(p(t))
$$

for all $t \in \mathbb{R}^{1}$ for which $\mathbf{p}(t) \in E$.
(a) For $1 \leq k \leq m$, show (by repeated application of the chain rule) that

$$
h^{(k)}(t)=\sum\left(D_{i_{1} \ldots i_{k}} f\right)(p(t)) x_{i_{1}} \cdots x_{i_{k}}
$$

The sum extends over all ordered k-tuples $\left(i_{1}, \ldots, i_{k}\right)$ in which each $i_{j}$ is one of the integers $1, \ldots, n$.
(b) By Taylor's theorem (Theorem 5.15),

$$
h(1)=\sum_{k=0}^{m-1} \frac{h^{(k)}(0)}{k!}+\frac{h^{(m)}(t)}{m!}
$$

for some $t \in(0,1)$. Use this to prove Taylor's theorem in $n$ variables by showing that the formula

$$
f(\mathbf{a}+\mathbf{x})=\sum_{k=0}^{m-1} \frac{1}{k!} \sum\left(D_{i_{1} \ldots i_{k}} f\right)(\mathbf{a}) x_{i_{1}} \cdots x_{i_{k}}+r(\mathbf{x})
$$

represents $f(\mathbf{a}+\mathbf{x})$ as the sum of its so-called "Taylor polynomial of degree $m-1$," plus a remainder that satisfies

$$
\lim _{\mathbf{x} \rightarrow 0} \frac{r(\mathbf{x})}{|\mathbf{x}|^{m-1}}=0
$$

Each of the inner sums extends over all ordered k-tuples $\left(i_{1}, \ldots, i_{k}\right)$, as in part (a); as usual, the zero-order derivative of $f$ is simply $f$, so that the constant term of the Taylor polynomial of $f$ at a is $f(a)$.
(c) Exercise 9.29 shows that repetition occurs in the Taylor polynomial as written in part (b). For instance, $\mathrm{D}_{113}$ occurs three times, as $\mathrm{D}_{113}, \mathrm{D}_{131}, \mathrm{D}_{311}$. The sum of the corresponding three terms can be written in the form

$$
3\left(\mathrm{D}_{1}^{2} \mathrm{D}_{3} \mathrm{f}\right)(\mathbf{a}) \mathrm{x}_{1}^{2} \mathrm{x}_{3}
$$

Prove (by calculating how often each derivative occurs) that the Taylor polynomial in (b) can be written in the form

$$
\sum \frac{\left(\mathrm{D}_{1}^{s_{1}} \cdots \mathrm{D}_{n}^{s_{n}} \mathrm{f}\right)(\mathbf{a})}{\mathrm{s}_{1}!\cdots \mathrm{s}_{n}!} \mathrm{x}_{1}^{s_{1}} \cdots \mathrm{x}_{n}^{s_{n}}
$$

Here the summation extends over all ordered n-tuples $\left(s_{1}, \ldots, s_{n}\right)$ such that each $s_{i}$ is a nonnegative integer and $s_{1}+\cdots+s_{n} \leq m-1$.
9.31. Suppose $f \in \mathscr{C}^{3}$ in some neighborhood of a point $\mathbf{a} \in \mathbb{R}^{2}$, the gradient of $f$ is 0 at a but not all second-order derivatives of $f$ are 0 at a. Show how one can then determine from the Taylor polynomial of $f$ at a (of degree 2) whether $f$ has a local maximum, or a local minimum, or neither, at the point a. Extend this to $\mathbb{R}^{n}$ in place of $\mathbb{R}^{2}$.

# Chapter 10 

## INTEGRATION OF DIFFERENTIAL FORMS

Integration can be studied on many levels. In Chap. 6, the theory was developed for reasonably well-behaved functions on subintervals of the real line. In Chap. 11 we shall encounter a very highly developed theory of integration that can be applied to much larger classes of functions, whose domains are more or less arbitrary sets, not necessarily subsets of $\mathbb{R}^{n}$. The present chapter is devoted to those aspects of integration theory that are closely related to the geometry of euclidean spaces such as the change of variables formula, line integrals, and the machinery of differential forms that is used in the statement and proof of the n -dimensional analogue of the fundamental theorem of calculus, namely Stokes' theorem.

## INTEGRATION

10.1 Definition. Suppose $I^{k}$ is a $k$-cell in $\mathbb{R}^{k}$ consisting of all

$$
\mathbf{x}=\left(x_{1}, \ldots, x_{k}\right)
$$

such that

$$
a_{i} \leq x_{i} \leq b_{i} \quad(i=1, \ldots, k)
$$

$I^{j}$ is the $j$-cell in $\mathbb{R}^{j}$ defined by the first $j$ inequalities (10.1), and $f$ is a real continuous function on $\mathrm{I}^{\mathrm{k}}$.

Put $\mathrm{f}=\mathrm{f}_{\mathrm{k}}$ and define $\mathrm{f}_{\mathrm{k}-1}$ on $\mathrm{I}^{\mathrm{k}-1}$ by

$$
f_{k-1}\left(x_{1}, \ldots, x_{k-1}\right)=\int_{a_{k}}^{b_{k}} f_{k}\left(x_{1}, \ldots, x_{k-1}, x_{k}\right) d x_{k}
$$

The uniform continuity of $f_{k}$ on $I^{k}$ shows that $f_{k-1}$ is continuous on $I^{k-1}$. Hence

we can repeat this process and obtain functions $f_{j}$, continuous on $I^{j}$, such that $f_{j-1}$ is the integral of $f_{j}$ with respect to $x_{j}$ over $\left[a_{j}, b_{j}\right]$. After $k$ steps we arrive at a number $f_{0}$, which we call the integral of $f$ over $I^{k}$; we write it in the form

$$
\int_{I^{k}} f(x) d x \text { or } \int_{I^{k}} f
$$

A priori, this definition of the integral depends on the order in which the k integrations are carried out. However, this dependence is only apparent. To prove this, let us introduce the temporary notation $L(f)$ for the integral (10.2) and $L^{\prime}(f)$ for the result obtained by carrying out the k integrations in some other order.
10.2 Theorem. For every $f \in \mathscr{C}\left(I^{k}\right), L(f)=L^{\prime}(f)$.

Proof. If $h(x)=h_{1}\left(x_{1}\right) \cdots h_{k}\left(x_{k}\right)$, where $h_{j} \in \mathscr{C}\left(\left[a_{j}, b_{j}\right]\right)$, then

$$
L(h)=\prod_{i=1}^{k} \int_{a_{i}}^{b_{i}} h_{i}\left(x_{i}\right) d x_{i}=L^{\prime}(h)
$$

If $\mathscr{A}$ is the set of all finite sums of such functions $h$, it follows that $L(g)=L^{\prime}(g)$ for all $g \in \mathscr{A}$. Also, $\mathscr{A}$ is an algebra of functions on $I^{k}$ to which the Stone-Weierstrass theorem applies.

Put $V=\prod_{i=1}^{k}\left(b_{i}-a_{i}\right)$. If $f \in \mathscr{C}\left(I^{k}\right)$ and $\varepsilon>0$, there exists $g \in \mathscr{A}$ such that $\|f-g\|<\varepsilon / V$, where $\|f\|$ is defined as $\max |f(x)| \quad\left(x \in I^{k}\right)$. Then $|L(f-g)|<\varepsilon$, $\left|L^{\prime}(f-g)\right|<\varepsilon$, and since

$$
L(f)-L^{\prime}(f)=L(f-g)+L^{\prime}(g-f)
$$

we conclude that $\left|L(f)-L^{\prime}(f)\right|<2 \varepsilon$. In this connection, Exercise 10.2 is relevant.
10.3 Definition. The support of a (real or complex) function $f$ on $\mathbb{R}^{k}$ is the closure of the set of all points $\mathbf{x} \in \mathbb{R}^{k}$ at which $f(\mathbf{x}) \neq 0$. If $f$ is a continuous function with compact support, let $I^{k}$ be any k -cell which contains the support of $f$ and define

$$
\int_{\mathbb{R}^{k}} f=\int_{I^{k}} f
$$

The integral so defined is evidently independent of the choice of $I^{k}$, provided only that $I^{k}$ contains the support of $f$.

It is now tempting to extend the definition of the integral over $\mathbb{R}^{k}$ to functions which are limits (in some sense) of continuous functions with compact support. We do not want to discuss the conditions under which this can be done; the proper setting for this question is the Lebesgue integral. We shall merely describe one very simple example which will be used in the proof of Stokes' theorem.

10.4 Example. Let $\mathrm{Q}^{\mathrm{k}}$ be the k -simplex which consists of all points $\mathbf{x}=\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{k}}\right)$ in $\mathbb{R}^{\mathrm{k}}$ for which $\mathrm{x}_{1}+\cdots+\mathrm{x}_{\mathrm{k}} \leq 1$ and $\mathrm{x}_{\mathrm{i}} \geq 0$ for $\mathrm{i}=1, \ldots, \mathrm{k}$. If $\mathrm{k}=3$, for example, $Q^{k}$ is a tetrahedron with vertices at $0, \mathbf{e}_{1}, \mathbf{e}_{2}, \mathbf{e}_{3}$. If $f \in \mathscr{C}\left(Q^{k}\right)$, extend $f$ to a function on $I^{k}$ by setting $f(\mathbf{x})=0$ off $Q^{k}$, and define

$$
\int_{Q^{k}} f=\int_{I^{k}} f
$$

Here $I^{k}$ is the "unit cube" defined by

$$
0 \leq x_{i} \leq 1 \quad(1 \leq i \leq k)
$$

Since $f$ may be discontinuous on $I^{k}$, the existence of the integral on the right of (10.4) needs proof. We also wish to show that this integral is independent of the order in which the k single integrations are carried out.

To do this, suppose $0<\delta<1$, put

$$
\varphi(t)= \begin{cases}1 & (t \leq 1-\delta) \\ \frac{1-t}{\delta} & (1-\delta<t \leq 1) \\ 0 & (1<t)\end{cases}
$$

and define

$$
F(\mathbf{x})=\varphi\left(x_{1}+\cdots+x_{k}\right) f(\mathbf{x}) \quad\left(\mathbf{x} \in I^{k}\right)
$$

Then $F \in \mathscr{C}\left(I^{k}\right)$.
Put $\mathbf{y}=\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{k}-1}\right), \mathbf{x}=\left(\mathbf{y}, \mathrm{x}_{\mathrm{k}}\right)$. For each $\mathbf{y} \in \mathrm{I}^{\mathrm{k}-1}$, the set of all $\mathrm{x}_{\mathrm{k}}$ such that $F\left(y, x_{k}\right) \neq f\left(y, x_{k}\right)$ is either empty or is a segment whose length does not exceed $\delta$. Since $0 \leq \varphi \leq 1$, it follows that

$$
\left|F_{k-1}(\mathbf{y})-f_{k-1}(\mathbf{y})\right| \leq \delta\|f\| \quad\left(\mathbf{y} \in I^{k-1}\right)
$$

where $\|f\|$ has the same meaning as in the proof of Theorem 10.2 and $F_{k-1}, f_{k-1}$ are as in Definition 10.1.

As $\delta \rightarrow 0,(10.7)$ exhibits $f_{k-1}$ as a uniform limit of a sequence of continuous functions. Thus $f_{k-1} \in \mathscr{C}\left(I^{k-1}\right)$ and the further integrations present no problem.

This proves the existence of the integral in (10.4). Moreover, (10.7) shows that

$$
\left|\int_{I^{k}} F(\mathbf{x}) d \mathbf{x}-\int_{I^{k}} f(\mathbf{x}) d \mathbf{x}\right| \leq \delta\|f\|
$$

Note that (10.8) is true regardless of the order in which the k single integrations are carried out. Since $F \in \mathscr{C}\left(I^{k}\right), \int F$ is unaffected by any change in this order. Hence (10.8) shows that the same is true of $\int f$. This completes the proof.

Our next goal is the change of variables formula stated in Theorem 10.9. To

facilitate its proof, we first discuss so-called primitive mappings and partitions of unity. Primitive mappings will enable us to get a clearer picture of the local actions of a $\mathscr{C}^{1}$-mapping with invertible derivative, and partitions of unity are a very useful device that makes it possible to use local information in a global setting.

# PRIMITIVE MAPPINGS 

10.5 Definition. If $\mathbf{G}$ maps an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ into $\mathbb{R}^{\mathrm{n}}$, and if there is an integer $m$ and a real function $g$ with domain $E$ such that

$$
\mathbf{G}(\mathbf{x})=\sum_{i \neq m} x_{i} \mathbf{e}_{i}+g(\mathbf{x}) \mathbf{e}_{m} \quad(\mathbf{x} \in E)
$$

then we call $\mathbf{G}$ primitive.
A primitive mapping is thus one that changes at most one coordinate. Note that (10.9) can also be written in the form

$$
\mathbf{G}(\mathbf{x})=\mathbf{x}+\left[\mathrm{g}(\mathbf{x})-\mathrm{x}_{\mathrm{m}}\right] \mathbf{e}_{\mathrm{m}}
$$

If $g$ is differentiable at some point $\mathbf{a} \in \mathrm{E}$, so is $\mathbf{G}$. The matrix $\left[\alpha_{i j}\right]$ of the operator $\mathbf{G}^{\prime}(\mathbf{a})$ has

$$
\left(D_{1} g\right)(\mathbf{a}), \ldots,\left(D_{m} g\right)(\mathbf{a}), \ldots,\left(D_{n} g\right)(\mathbf{a})
$$

as its mth row. For $\mathrm{j} \neq \mathrm{m}$, we have $\alpha_{\mathrm{ij}}=1$ and $\alpha_{\mathrm{ij}}=0$ if $\mathrm{i} \neq \mathrm{j}$. The Jacobian of $\mathbf{G}$ at $\mathbf{a}$ is thus given by

$$
J_{G}(\mathbf{a})=\operatorname{det}\left[\mathbf{G}^{\prime}(\mathbf{a})\right]=\left(D_{m} g\right)(\mathbf{a})
$$

and we see (by Theorem 9.36) that $\mathbf{G}^{\prime}(\mathbf{a})$ is invertible if and only if $\left(\mathrm{D}_{\mathrm{m}} \mathrm{g}\right)(\mathbf{a}) \neq 0$.
10.6 Definition. A linear operator $B$ on $\mathbb{R}^{n}$ that interchanges some pair of members of the standard basis and leaves the others fixed is called a flip.

For example, the flip $B$ on $\mathbb{R}^{4}$ that interchanges $\mathbf{e}_{2}$ and $\mathbf{e}_{4}$ has the form

$$
B\left(x_{1} \mathbf{e}_{1}+x_{2} \mathbf{e}_{2}+x_{3} \mathbf{e}_{3}+x_{4} \mathbf{e}_{4}\right)=x_{1} \mathbf{e}_{1}+x_{2} \mathbf{e}_{4}+x_{3} \mathbf{e}_{3}+x_{4} \mathbf{e}_{2}
$$

or, equivalently,

$$
B\left(x_{1} \mathbf{e}_{1}+x_{2} \mathbf{e}_{2}+x_{3} \mathbf{e}_{3}+x_{4} \mathbf{e}_{4}\right)=x_{1} \mathbf{e}_{1}+x_{4} \mathbf{e}_{2}+x_{3} \mathbf{e}_{3}+x_{2} \mathbf{e}_{4}
$$

Hence $B$ can also be thought of as interchanging two of the coordinates, rather than two basis vectors.

In the proof that follows, we shall use the projections $P_{0}, \ldots, P_{n}$ in $\mathbb{R}^{n}$, defined by $P_{0} \mathbf{x}=\mathbf{0}$ and

$$
P_{m} \mathbf{x}=x_{1} \mathbf{e}_{1}+\cdots+x_{m} \mathbf{e}_{m}
$$

for $1 \leq \mathrm{m} \leq \mathrm{n}$. Thus $\mathrm{P}_{\mathrm{m}}$ is the projection whose range and null space are spanned by $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{m}\right\}$ and $\left\{\mathbf{e}_{m+1}, \ldots, \mathbf{e}_{n}\right\}$, respectively.
10.7 Theorem. Suppose $\mathbf{F}$ is a $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{n}$ into $\mathbb{R}^{n}, \mathbf{0} \in \mathrm{E}$, $\mathbf{F}(\mathbf{0})=\mathbf{0}$, and $\mathbf{F}^{\prime}(\mathbf{0})$ is invertible. Then there is a neighborhood of $\mathbf{0}$ in $\mathbb{R}^{n}$ in which a representation

$$
\mathbf{F}(\mathbf{x})=\mathrm{B}_{1} \cdots \mathrm{~B}_{n-1} \mathbf{G}_{n} \circ \cdots \circ \mathbf{G}_{1}(\mathbf{x})
$$

is valid.
In (10.16), each $\mathbf{G}_{\mathbf{i}}$ is a primitive $\mathscr{C}^{1}$-mapping in some neighborhood of $\mathbf{0} ; \mathbf{G}_{\mathbf{i}}(\mathbf{0})=\mathbf{0}$, $\mathbf{G}_{\mathbf{i}}^{\prime}(\mathbf{0})$ is invertible, and each $\mathrm{B}_{\mathbf{i}}$ is either a flip or the identity operator.

Briefly, (10.16) represents $\mathbf{F}$ locally as a composition of primitive mappings and flips.

Proof. Put $\mathbf{F}=\mathbf{F}_{1}$. Assume $1 \leq \mathrm{m} \leq \mathrm{n}-1$, and make the following induction hypothesis (which evidently holds for $\mathrm{m}=1$ ):
$\mathrm{V}_{\mathrm{m}}$ is a neighborhood of $\mathbf{0}, \mathbf{F}_{\mathrm{m}} \in \mathscr{C}^{1}\left(\mathrm{~V}_{\mathrm{m}}\right), \mathbf{F}_{\mathrm{m}}(\mathbf{0})=\mathbf{0}, \mathbf{F}_{\mathrm{m}}^{\prime}(\mathbf{0})$ is invertible, and

$$
P_{m-1} F_{m}(\mathbf{x})=P_{m-1} \mathbf{x} \quad\left(\mathbf{x} \in V_{m}\right)
$$

By (10.17), we have

$$
\mathbf{F}_{\mathrm{m}}(\mathbf{x})=\mathrm{P}_{\mathrm{m}-1} \mathbf{x}+\sum_{\mathrm{i}=\mathrm{m}}^{\mathrm{n}} \alpha_{\mathrm{i}}(\mathbf{x}) \mathbf{e}_{\mathrm{i}}
$$

where $\alpha_{m}, \ldots, \alpha_{n}$ are real $\mathscr{C}^{1}$-functions in $V_{m}$. Hence

$$
\mathbf{F}_{\mathrm{m}}^{\prime}(\mathbf{0}) \mathbf{e}_{\mathrm{m}}=\sum_{\mathrm{i}=\mathrm{m}}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{m}} \alpha_{\mathrm{i}}\right)(\mathbf{0}) \mathbf{e}_{\mathrm{i}}
$$

Since $\mathbf{F}^{\prime}(\mathbf{0})$ is invertible, the left side of (10.19) is not $\mathbf{0}$, and therefore there is a k such that $\mathrm{m} \leq \mathrm{k} \leq \mathrm{n}$ and $\left(\mathrm{D}_{\mathrm{m}} \alpha_{\mathrm{k}}\right)(\mathbf{0}) \neq 0$.

Let $B_{m}$ be the flip that interchanges this $m$ and this $k$ (if $k=m, B_{m}$ is the identity) and define

$$
\mathbf{G}_{m}(\mathbf{x})=\mathbf{x}+\left\{\alpha_{k}(\mathbf{x})-\mathrm{x}_{m}\right\} \mathbf{e}_{m} \quad\left(\mathbf{x} \in V_{m}\right)
$$

Then $\mathbf{G}_{m} \in \mathscr{C}^{1}\left(V_{m}\right), \mathbf{G}_{m}$ is primitive, and $\mathbf{G}_{m}^{\prime}(\mathbf{0})$ is invertible, since $\left(\mathrm{D}_{\mathrm{m}} \alpha_{\mathrm{k}}\right)(\mathbf{0}) \neq$ 0 .

The inverse function theorem shows therefore that there is an open set $U_{m}$ with $0 \in U_{m} \subset V_{m}$ such that $G_{m}$ is a 1-1 mapping of $U_{m}$ onto a neighborhood $V_{m+1}$ of 0 , in which $\mathbf{G}_{m}^{-1}$ is continuously differentiable. Define $\mathbf{F}_{m+1}$ by

$$
\mathbf{F}_{m+1}(\mathbf{y})=\mathrm{B}_{m} \mathbf{F}_{m} \circ \mathbf{G}_{m}^{-1}(\mathbf{y}) \quad\left(\mathbf{y} \in V_{m+1}\right)
$$

Then $\mathbf{F}_{m+1} \in \mathscr{C}^{1}\left(\mathrm{~V}_{m+1}\right), \mathbf{F}_{m+1}(\mathbf{0})=\mathbf{0}$, and $\mathbf{F}_{m+1}^{\prime}(\mathbf{0})$ is invertible (by the chain rule). Also, for $\mathbf{x} \in \mathrm{U}_{\mathrm{m}}$,

$$
\begin{aligned}
\mathrm{P}_{\mathrm{m}} \mathbf{F}_{\mathrm{m}+1}\left(\mathbf{G}_{\mathrm{m}}(\mathbf{x})\right) & =\mathrm{P}_{\mathrm{m}} \mathrm{~B}_{\mathrm{m}} \mathbf{F}_{\mathrm{m}}(\mathbf{x}) \\
& =\mathrm{P}_{\mathrm{m}}\left[\mathrm{P}_{\mathrm{m}+1} \mathbf{x}+\alpha_{\mathrm{k}}(\mathbf{x}) \mathbf{e}_{\mathrm{m}}+\cdots\right] \\
& =\mathrm{P}_{\mathrm{m}-1} \mathbf{x}+\alpha_{\mathrm{k}}(\mathbf{x}) \mathbf{e}_{\mathrm{m}} \\
& =\mathrm{P}_{\mathrm{m}} \mathbf{G}_{\mathrm{m}}(\mathbf{x})
\end{aligned}
$$

so that

$$
\mathrm{P}_{\mathrm{m}} \mathbf{F}_{\mathrm{m}+1}(\mathbf{y})=\mathrm{P}_{\mathrm{m}} \mathbf{y} \quad\left(\mathbf{y} \in \mathrm{~V}_{\mathrm{m}+1}\right)
$$

Our induction hypothesis holds therefore with $m+1$ in place of $m$. [In (10.22), we first used (10.21), then (10.18) and the definition of $B_{m}$, then the definition of $P_{m}$, and finally (10.20).]

Since $B_{m} B_{m}=I,(10.21)$, with $\mathbf{y}=\mathbf{G}_{m}(\mathbf{x})$, is equivalent to

$$
\mathbf{F}_{m}(\mathbf{x})=B_{m} \mathbf{F}_{m+1}\left(\mathbf{G}_{m}(\mathbf{x})\right) \quad\left(\mathbf{x} \in \mathrm{U}_{m}\right)
$$

If we apply this with $m=1, \ldots, n-1$, we successively obtain

$$
\begin{aligned}
\mathbf{F}=\mathbf{F}_{1} & =\mathrm{B}_{1} \mathbf{F}_{2} \circ \mathbf{G}_{1} \\
& =\mathrm{B}_{1} \mathrm{~B}_{2} \mathbf{F}_{3} \circ \mathbf{G}_{2} \circ \mathbf{G}_{1}=\cdots \\
& =\mathrm{B}_{1} \cdots \mathrm{~B}_{n-1} \mathbf{F}_{n} \circ \mathbf{G}_{n-1} \circ \cdots \circ \mathbf{G}_{1}
\end{aligned}
$$

in some neighborhood of $\mathbf{0}$. By (10.17), $\mathbf{F}_{n}$ is primitive. This completes the proof.

# PARTITIONS OF UNITY 

10.8 Theorem. Suppose K is a compact subset of $\mathbb{R}^{n}$ and $\left\{\mathrm{V}_{\alpha}\right\}$ is an open cover of K . Then there exist functions $\psi_{1}, \ldots, \psi_{\mathrm{s}} \in \mathscr{C}\left(\mathbb{R}^{\mathrm{n}}\right)$ such that
(a) $0 \leq \psi_{i} \leq 1$ for $1 \leq i \leq s$;
(b) each $\psi_{i}$ has its support in some $V_{\alpha}$, and
(c) $\psi_{1}(\mathbf{x})+\cdots+\psi_{\mathrm{s}}(\mathbf{x})=1$ for every $\mathbf{x} \in \mathrm{K}$.

Because of (c), $\left\{\psi_{i}\right\}$ is called a partition of unity, and (b) is sometimes expressed by saying that $\left\{\psi_{i}\right\}$ is subordinate to the cover $\left\{V_{\alpha}\right\}$.

Corollary. If $\mathrm{f} \in \mathscr{C}\left(\mathbb{R}^{\mathrm{n}}\right)$ and the support of f lies in K , then

$$
\mathrm{f}=\sum_{\mathrm{i}=1}^{\mathrm{s}} \psi_{\mathrm{i}} \mathrm{f}
$$

Each $\psi_{i} \mathrm{f}$ has its support in some $\mathrm{V}_{\alpha}$.

The point of (10.25) is that it furnishes a representation of $f$ as a sum of continuous functions $\psi_{i} f$ with "small" supports.

Proof. Associate with each $\mathbf{x} \in \mathrm{K}$ an index $\alpha(\mathbf{x})$ so that $\mathbf{x} \in V_{\alpha(\mathbf{x})}$. Then there are open balls $B(\mathbf{x})$ and $W(\mathbf{x})$, centered at $\mathbf{x}$, with

$$
\overline{\mathrm{B}(\mathbf{x})} \subset W(\mathbf{x}) \subset \overline{W(\mathbf{x})} \subset V_{\alpha(\mathbf{x})}
$$

Since K is compact, there are points $\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{s}}$ in K such that

$$
\mathrm{K} \subset \mathrm{~B}\left(\mathbf{x}_{1}\right) \cup \cdots \cup \mathrm{B}\left(\mathbf{x}_{\mathrm{s}}\right)
$$

By (10.26), there are functions $\varphi_{1}, \ldots, \varphi_{\mathrm{s}} \in \mathscr{C}\left(\mathbb{R}^{n}\right)$ such that $\varphi_{i}(\mathbf{x})=1$ on $B\left(\mathbf{x}_{i}\right)$, $\varphi_{i}(\mathbf{x})=0$ outside $W\left(\mathbf{x}_{i}\right)$, and $0 \leq \varphi_{i}(\mathbf{x}) \leq 1$ on $\mathbb{R}^{n}$. Define $\psi_{1}=\varphi_{1}$ and

$$
\psi_{i+1}=\left(1-\varphi_{1}\right) \cdots\left(1-\varphi_{i}\right) \varphi_{i+1}
$$

for $i=1, \ldots, s-1$.
Properties (a) and (b) are clear. The relation

$$
\psi_{1}+\cdots+\psi_{i}=1-\left(1-\varphi_{1}\right) \cdots\left(1-\varphi_{i}\right)
$$

is trivial for $i=1$. If (10.29) holds for some $i<s$, addition of (10.28) and (10.29) yields (10.29) with $i+1$ in place of $i$. It follows that

$$
\sum_{i=1}^{s} \psi_{i}(\mathbf{x})=1-\prod_{i=1}^{s}\left[1-\varphi_{i}(\mathbf{x})\right] \quad\left(\mathbf{x} \in \mathbb{R}^{n}\right)
$$

If $\mathbf{x} \in \mathrm{K}$, then $\mathbf{x} \in \mathrm{B}\left(\mathbf{x}_{\mathrm{i}}\right)$ for some $i$, hence $\varphi_{i}(\mathbf{x})=1$, and the product in (10.30) is 0 . This proves (c).

# CHANGE OF VARIABLES 

We can now describe the effect of a change of variables on a multiple integral. For simplicity, we confine ourselves here to continuous functions with compact support, although this is too restrictive for many applications. This is illustrated by Exercises 10.9 to 10.13 .
10.9 Theorem. Suppose T is a 1-1 $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{k}}$ into $\mathbb{R}^{\mathrm{k}}$ such that $\mathrm{J}_{\mathrm{T}}(\mathbf{x}) \neq 0$ for all $\mathbf{x} \in \mathrm{E}$. If f is a continuous function on $\mathbb{R}^{\mathrm{k}}$ whose support is compact and lies in $\mathrm{T}(\mathrm{E})$, then

$$
\int_{\mathbb{R}^{\mathrm{k}}} \mathrm{f}(\mathbf{y}) \mathrm{d} \mathbf{y}=\int_{\mathbb{R}^{\mathrm{k}}} \mathrm{f}(\mathrm{~T}(\mathbf{x}))\left|\mathrm{J}_{\mathrm{T}}(\mathbf{x})\right| \mathrm{d} \mathbf{x}
$$

We recall that $\mathrm{J}_{\mathrm{T}}$ is the Jacobian of T . The assumption $\mathrm{J}_{\mathrm{T}}(\mathbf{x}) \neq 0$ implies, by the inverse function theorem, that $\mathrm{T}^{-1}$ is continuous on $\mathrm{T}(\mathrm{E})$, and this ensures that the integrand on the right side of (10.31) has compact support in E (Theorem 4.14).

The appearance of the absolute value of $\mathrm{J}_{\mathrm{T}}(\mathbf{x})$ in (10.31) may call for a comment. Take the case $\mathrm{k}=1$ and suppose that T is a $1-1 \mathscr{C}^{1}$-mapping of $\mathbb{R}^{1}$ onto $\mathbb{R}^{1}$. Then $\mathrm{J}_{\mathrm{T}}(\mathrm{x})=\mathrm{T}^{\prime}(\mathrm{x})$; if T is increasing, we have

$$
\int_{\mathbb{R}^{1}} f(y) d y=\int_{\mathbb{R}^{1}} f(T(x)) T^{\prime}(x) d x
$$

by Theorems 6.19 and 6.17, for all continuous $f$ with compact support. But if $T$ decreases, then $T^{\prime}(x)<0$; if $f$ is positive in the interior of its support, the left side of (10.32) is positive and the right side is negative. A correct equation is obtained if $T^{\prime}$ is replaced by $\left|T^{\prime}\right|$ in (10.32).

The point is that the integrals we are now considering are integrals of functions over subsets of $\mathbb{R}^{\mathrm{k}}$ and we associate no direction or orientation with these subsets. We shall adopt a different point of view when we come to integration of differential forms over surfaces.

Proof. It follows from the remarks just made that (10.31) is true if T is a primitive $\mathscr{C}^{1}$-mapping (see Definition 10.5), and Theorem 10.2 shows that (10.31) is true if T is a linear mapping which merely interchanges two coordinates.

If the theorem is true for transformations $\mathrm{P}, \mathrm{Q}$, and if $\mathrm{S}(\mathbf{x})=\mathrm{P}(\mathrm{Q}(\mathbf{x}))$, then

$$
\begin{aligned}
\int f(\mathbf{z}) d \mathbf{z} & =\int f(P(\mathbf{y}))\left|\mathrm{J}_{\mathrm{P}}(\mathbf{y})\right| d \mathbf{y} \\
& =\int f(P(Q(\mathbf{x})))\left|\mathrm{J}_{\mathrm{P}}(\mathrm{Q}(\mathbf{x}))\right|\left|\mathrm{J}_{\mathrm{Q}}(\mathbf{x})\right| d \mathbf{x} \\
& =\int f(S(\mathbf{x})) \mid J_{S}(\mathbf{x}) \mid d \mathbf{x}
\end{aligned}
$$

since

$$
\begin{aligned}
J_{P}(Q(\mathbf{x})) J_{Q}(\mathbf{x}) & =\operatorname{det} P^{\prime}(Q(\mathbf{x})) \operatorname{det} Q^{\prime}(\mathbf{x}) \\
& =\operatorname{det}\left[P^{\prime}(Q(\mathbf{x})) Q^{\prime}(\mathbf{x})\right]=\operatorname{det} S^{\prime}(\mathbf{x})=J_{S}(\mathbf{x})
\end{aligned}
$$

by the multiplication theorem for determinants and the chain rule. Thus the theorem is also true for $S$.

Each point $\mathbf{a} \in E$ has a neighborhood $U \subset E$ in which

$$
T(\mathbf{x})=T(\mathbf{a})+B_{1} \cdots B_{k-1} G_{k} \circ G_{k-1} \circ \cdots \circ G_{1}(\mathbf{x}-\mathbf{a})
$$

where $\mathbf{G}_{\mathrm{i}}$ and $\mathrm{B}_{\mathrm{i}}$ are as in Theorem 10.7. Setting $\mathrm{V}=\mathrm{T}(\mathrm{U})$, it follows that (10.31) holds if the support of $f$ lies in $V$. Thus:

Each point $\mathbf{y} \in \mathrm{T}(\mathrm{E})$ lies in an open set $\mathrm{V}_{\mathbf{y}} \subset \mathrm{T}(\mathrm{E})$ such that (10.31) holds for all continuous functions whose support lies in $\mathrm{V}_{\mathbf{y}}$.

Now let f be a continuous function with compact support $\mathrm{K} \subset \mathrm{T}(\mathrm{E})$. Since $\left\{\mathrm{V}_{\mathbf{y}}\right\}$ covers K , the Corollary to Theorem 10.8 shows that $\mathrm{f}=\Sigma \psi_{\mathrm{i}} \mathrm{f}$, where each $\psi_{\mathrm{i}}$ is continuous and each $\psi_{\mathrm{i}}$ has its support in some $\mathrm{V}_{\mathbf{y}}$. Thus (10.31) holds for each $\psi_{\mathrm{i}} \mathrm{f}$, and hence also for their sum f .

# DIFFERENTIAL FORMS 

We shall now develop some of the machinery that is needed for the $n$-dimensional version of the fundamental theorem of calculus which is usually called Stokes' theorem. The original form of Stokes' theorem arose in applications of vector analysis to electromagnetism and was stated in terms of the curl of a vector field. Green's theorem and the divergence theorem are other special cases. These topics are briefly discussed at the end of the chapter.

It is a curious feature of Stokes' theorem that the only thing that is difficult about it is the elaborate structure of the definitions that are needed for its statement. These definitions concern differential forms, their derivatives, boundaries, and orientation. Once these concepts are understood, the statement of the theorem is very brief and succinct, and its proof presents little difficulty.

Up to now we have considered derivatives of functions of several variables only for functions defined in open sets. This was done to avoid difficulties that can occur at boundary points. It will now be convenient, however, to discuss differentiable functions on compact sets. We therefore adopt the following convention:

To say that $\mathbf{f}$ is a $\mathscr{C}^{1}$-mapping (or a $\mathscr{C}^{2}$-mapping) of a compact set $D \subset \mathbb{R}^{\mathrm{k}}$ into $\mathbb{R}^{n}$ means that there is a $\mathscr{C}^{1}$-mapping (or a $\mathscr{C}^{2}$-mapping) $\mathbf{g}$ of an open set $W \subset \mathbb{R}^{\mathrm{k}}$ into $\mathbb{R}^{n}$ such that $D \subset W$ and such that $\mathbf{g}(\mathbf{x})=\mathbf{f}(\mathbf{x})$ for all $\mathbf{x} \in D$.
10.10 Definition. Suppose $E$ is an open set in $\mathbb{R}^{n}$. A $k$-surface in $E$ is a $\mathscr{C}^{1}$-mapping $\Phi$ from a compact set $D \subset \mathbb{R}^{k}$ into $E$. $D$ is called the parameter domain of $\Phi$. Points of $D$ will be denoted by $\mathbf{u}=\left(u_{1}, \ldots, u_{k}\right)$.

We shall confine ourselves to the simple situation in which D is either a k-cell or the k -simplex $\mathrm{Q}^{\mathrm{k}}$ described in Example 10.4. The reason for this is that we shall have to integrate over D , and we have not yet discussed integration over more complicated subsets of $\mathbb{R}^{\mathrm{k}}$. It will be seen that this restriction on D (which will be made tacitly from now on) entails no significant loss of generality in the resulting theory of differential forms.

We stress that k -surfaces in E are defined to be mappings into E , not subsets of E . This agrees with our earlier definition of curves (Definition 6.26). In fact, 1-surfaces are precisely the same as continuously differentiable curves.
10.11 Definition. Suppose $E$ is an open set in $\mathbb{R}^{n}$. A differentiable form of order $k \geq 1$ in E (briefly, a k-form in E ) is a function $\omega$, symbolically represented by the sum

$$
\omega=\sum a_{i_{1}, \ldots, i_{k}}(\mathbf{x}) d x_{i_{1}} \wedge \cdots \wedge d x_{i_{k}}
$$

(the indices $i_{1}, \ldots, i_{k}$ range independently from 1 to $n$ ), which assigns to each ksurface $\Phi$ in E a number $\omega(\Phi)=\int_{\Phi} \omega$, according to the rule

$$
\int_{\Phi} \omega=\int_{D} \sum a_{i_{1}, \ldots, i_{k}}(\Phi(\mathbf{u})) \frac{\partial\left(x_{i_{1}}, \ldots, x_{i_{k}}\right)}{\partial\left(u_{1}, \ldots, u_{k}\right)} d \mathbf{u}
$$

where D is the parameter domain of $\Phi$.
The functions $\alpha_{i_{1}, \ldots, i_{k}}$ are assumed to be real and continuous in E . If $\phi_{1}, \ldots, \phi_{n}$ are the components of $\Phi$, the Jacobian in (10.35) is the one determined by the mapping

$$
\left(u_{1}, \ldots, u_{k}\right) \mapsto\left(\phi_{i_{1}}(\mathbf{u}), \ldots, \phi_{i_{k}}(\mathbf{u})\right)
$$

Note that the right side of (10.35) is an integral over D, as defined in Definition 10.1 (or Example 10.4) and that (10.35) is the definition of the symbol $\int_{\Phi} \omega$.

A k -form $\omega$ is said to be of class $\mathscr{C}^{1}$ or $\mathscr{C}^{2}$ if the functions $a_{i_{1}, \ldots, i_{k}}$ in (10.34) are all of class $\mathscr{C}^{1}$ or $\mathscr{C}^{2}$. A 0 -form in E is defined to be a continuous function in E .

# 10.12 Examples. 

(a) Let $\gamma$ be a 1-surface (a curve of class $\mathscr{C}^{1}$ ) in $\mathbb{R}^{3}$, with parameter domain $[0,1]$. Write $(x, y, z)$ in place of $\left(x_{1}, x_{2}, x_{3}\right)$ and put

$$
\omega=x d y+y d x
$$

Then

$$
\int_{\gamma} \omega=\int_{0}^{1}\left[\gamma_{1}(t) \gamma_{2}^{\prime}(t)+\gamma_{2}(t) \gamma_{1}^{\prime}(t)\right] d t=\gamma_{1}(1) \gamma_{2}(1)-\gamma_{1}(0) \gamma_{2}(0)
$$

Note that in this example $\int_{\gamma} \omega$ depends only on the initial point $\gamma(0)$ and on the end point $\gamma(1)$ of $\gamma$. In particular, $\int_{\gamma} \omega=0$ for every closed curve $\gamma$. (As we shall see later, this is true for every 1-form $\omega$ which is exact.) Integrals of 1 -forms are often called line integrals.
(b) Fix $a>0, b>0$, and define

$$
\gamma(t)=(a \cos t, b \sin t) \quad(0 \leq t \leq 2 \pi)
$$

so that $\gamma$ is a closed curve in $\mathbb{R}^{2}$. (Its range is an ellipse.) Then

$$
\int_{\gamma} x d y=\int_{0}^{2 \pi} a b \cos ^{2} t d t=\pi a b
$$

whereas

$$
\int_{\gamma} y d x=-\int_{0}^{2 \pi} a b \sin ^{2} t d t=-\pi a b
$$

Note that $\int_{\gamma} x d y$ is the area of the region bounded by $\gamma$. This is a special case of Green's theorem.

(c) Let D be the 3-cell defined by

$$
0 \leq r \leq 1, \quad 0 \leq \theta \leq \pi, \quad 0 \leq \varphi \leq 2 \pi
$$

Define $\Phi(r, \theta, \phi)=(x, y, z)$, where

$$
\begin{aligned}
& x=r \sin \theta \cos \varphi \\
& y=r \sin \theta \sin \varphi \\
& z=r \cos \theta
\end{aligned}
$$

Then

$$
J_{\Phi}(r, \theta, \varphi)=\frac{\partial(x, y, z)}{\partial(r, \theta, \varphi)}=r^{2} \sin \theta
$$

Hence

$$
\int_{\Phi} \mathrm{dx} \wedge \mathrm{dy} \wedge \mathrm{dz}=\int_{\mathrm{D}} \mathrm{~J}_{\Phi}=\frac{4 \pi}{3}
$$

Note that $\Phi$ maps D onto the closed unit ball of $\mathbb{R}^{3}$, that the mapping is 1-1 in the interior of D (but certain boundary points are identified by $\Phi$ ), and that the integral (10.36) is equal to the volume of $\Phi(\mathrm{D})$.
10.13 Elementary Properties. Let $\omega, \omega_{1}, \omega_{2}$ be k -forms in E. We write $\omega_{1}=\omega_{2}$ if and only if $\omega_{1}(\Phi)=\omega_{2}(\Phi)$ for every k -surface $\Phi$ in E. In particular, $\omega=0$ means that $\omega(\Phi)=0$ for every k -surface $\Phi$ in E . If c is a real number, then cw is the k -form defined by

$$
\int_{\Phi} c \omega=c \int_{\Phi} \omega
$$

and $\omega=\omega_{1}+\omega_{2}$ means that

$$
\int_{\Phi} \omega=\int_{\Phi} \omega_{1}+\int_{\Phi} \omega_{2}
$$

for every k -surface $\Phi$ in E. As a special case of (10.37), note that $-\omega$ is defined so that

$$
\int_{\Phi}(-\omega)=-\int_{\Phi} \omega
$$

Consider a k-form

$$
\omega=\mathfrak{a}(\mathbf{x}) \mathrm{dx}_{\mathrm{i}_{1}} \wedge \cdots \wedge \mathrm{dx}_{\mathrm{i}_{\mathrm{k}}}
$$

and let $\bar{w}$ be the k -form obtained by interchanging some pair of subscripts in (10.40). If (10.35) and (10.39) are combined with the fact that a determinant changes

sign if two of its rows are interchanged, we see that

$$
\bar{w}=-\omega
$$

As a special case of this, note that the anticommutative relation

$$
d x_{i} \wedge d x_{j}=-d x_{j} \wedge d x_{i}
$$

holds for all $i$ and $j$. In particular,

$$
d x_{i} \wedge d x_{i}=0 \quad(i=1, \ldots, n)
$$

More generally, let us return to (10.40) and assume that $i_{r}=i_{s}$ for some $r \neq s$. If these two subscripts are interchanged, then $\bar{w}=\omega$, hence $\omega=0$ by (10.41). In other words, if $\omega$ is given by (10.40), then $\omega=0$ unless the subscripts $i_{1}, \ldots, i_{k}$ are all distinct.

If $\omega$ is as in (10.34), the summands with repeated subscripts can therefore be omitted without changing $\omega$. It follows that 0 is the only k -form in any open subset of $\mathbb{R}^{n}$ if $k>n$.

The anticommutativity expressed by (10.42) is the reason for the inordinate amount of attention that has to be paid to minus signs when studying differential forms.
10.14 Basic k-forms. If $i_{1}, \ldots, i_{k}$ are integers such that $1 \leq i_{1}<i_{2}<\cdots<i_{k} \leq n$ and if I is the ordered k-tuple $\left(i_{1}, \ldots, i_{k}\right)$, then we call I an increasing k-index and we use the brief notation

$$
d x_{I}=d x_{i_{1}} \wedge \cdots \wedge d x_{i_{k}}
$$

These forms $d x_{I}$ are the so-called basic k-forms in $\mathbb{R}^{n}$.
It is not hard to verify that there are precisely $n!/ k!(n-k)$ ! basic k-forms in $\mathbb{R}^{n}$; we shall make no use of this, however.

Much more important is the fact that every k -form can be represented in terms of basic k -forms. To see this, note that every k-tuple $\left(j_{1}, \ldots, j_{k}\right)$ of distinct integers can be converted to an increasing k -index J by a finite number of interchanges of pairs; each of these amounts to a multiplication by -1 as we saw in Sec. 10.13. Hence

$$
d x_{j_{1}} \wedge \cdots \wedge d x_{j_{k}}=\varepsilon\left(j_{1}, \ldots, j_{k}\right) d x_{J}
$$

where $\varepsilon\left(j_{1}, \ldots, j_{k}\right)$ is 1 or -1 depending on the number of interchanges that are needed. In fact, it is easy to see that

$$
\varepsilon\left(j_{1}, \ldots, j_{k}\right)=s\left(j_{1}, \ldots, j_{k}\right)
$$

where $s$ is as in Definition 9.33.

For example,

$$
d x_{1} \wedge d x_{5} \wedge d x_{3} \wedge d x_{2}=-d x_{1} \wedge d x_{2} \wedge d x_{3} \wedge d x_{5}
$$

and

$$
d x_{4} \wedge d x_{2} \wedge d x_{3}=d x_{2} \wedge d x_{3} \wedge d x_{4}
$$

If every k-tuple in (10.34) is converted to an increasing k-index, then we obtain the so-called standard presentation of $\omega$ :

$$
\omega=\sum_{I} b_{I}(\mathbf{x}) d x_{I}
$$

The summation in (10.47) ranges over all increasing indices I. [Of course, every increasing k -index arises from many (from $\mathrm{k}!$, to be precise) k -tuples. Each $\mathrm{b}_{I}$ in (10.47) may thus be a sum of several of the coefficients that occur in (10.34).]

For example

$$
x_{1} d x_{2} \wedge d x_{1}-x_{2} d x_{3} \wedge d x_{2}+x_{3} d x_{2} \wedge d x_{3}+d x_{1} \wedge d x_{2}
$$

is a 2 -form in $\mathbb{R}^{3}$ whose standard presentation is

$$
\left(1-x_{1}\right) d x_{1} \wedge d x_{2}+\left(x_{2}+x_{3}\right) d x_{2} \wedge d x_{3}
$$

The following uniqueness theorem is one of the main reasons for the introduction of the standard presentation of a k -form.
10.15 Theorem. Suppose

$$
\omega=\sum_{I} b_{I}(\mathbf{x}) d x_{I}
$$

is the standard presentation of a k -form $\omega$ in an open subset $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$. If $\omega=0$ in E , then $b_{I}(\mathbf{x})=0$ for every increasing k -index I and for every $\mathbf{x} \in \mathrm{E}$.

Note that the analogous statement would be false for sums such as (10.34) since, for example,

$$
d x_{1} \wedge d x_{2}+d x_{2} \wedge d x_{1}=0
$$

Proof. Assume, to reach a contradiction, that $b_{J}(\mathbf{v})>0$ for some $v \in E$ and for some increasing k -index $\mathrm{J}=\left(\mathrm{j}_{1}, \ldots, \mathrm{j}_{\mathrm{k}}\right)$. Since $\mathrm{b}_{\mathrm{J}}$ is continuous, there exists $\mathrm{h}>0$ such that $b_{J}(\mathbf{x})>0$ for all $\mathbf{x} \in \mathbb{R}^{\mathrm{n}}$ whose coordinates satisfy $\left|x_{i}-v_{i}\right| \leq h$. Let D be the k -cell in $\mathbb{R}^{\mathrm{k}}$ such that $\mathbf{u} \in \mathrm{D}$ if and only if $\left|u_{\tau}\right| \leq \mathrm{h}$ for $\tau=1, \ldots, \mathrm{k}$. Define

$$
\Phi(\mathbf{u})=\mathbf{v}+\sum_{\tau=1}^{\mathrm{k}} \mathbf{u}_{\tau} \mathbf{e}_{\mathrm{j}}, \quad(\mathbf{u} \in \mathrm{D})
$$

Then $\Phi$ is a k -surface in E , with parameter domain D , and $b_{J}(\Phi(\mathbf{u}))>0$ for every $\mathbf{u} \in \mathrm{D}$.

We claim that

$$
\int_{\Phi} \omega=\int_{\mathrm{D}} \mathrm{~b}_{\mathrm{J}}(\Phi(\mathbf{u})) \mathrm{d} \mathbf{u}
$$

Since the right side of (10.50) is positive, it follows that $\omega(\Phi) \neq 0$. Hence (10.50) gives our contradiction.

To prove (10.50), apply (10.35) to the presentation (10.48). More specifically, compute the Jacobians that occur in (10.35). By (10.49),

$$
\frac{\partial\left(x_{j_{1}}, \ldots, x_{j_{k}}\right)}{\partial\left(u_{1}, \ldots, u_{k}\right)}=1
$$

For any other increasing k -index $\mathrm{I} \neq \mathrm{J}$, the Jacobian is 0 since it is the determinant of a matrix with at least one row of zeroes.

# 10.16 Products of Basic k-forms. Suppose 

$$
I=\left(i_{1}, \ldots, i_{p}\right), \quad J=\left(j_{1}, \ldots, j_{q}\right)
$$

where $1 \leq i_{1}<\cdots<i_{p} \leq n$ and $1 \leq j_{1}<\cdots<j_{q} \leq n$. Then product of the corresponding basic forms $d x_{I}$ and $d x_{J}$ in $\mathbb{R}^{n}$ is a $(p+q)$-form in $\mathbb{R}^{n}$, denoted by the symbol $d x_{I} \wedge d x_{J}$ and defined by

$$
d x_{I} \wedge d x_{J}=d x_{i_{1}} \wedge \cdots \wedge d x_{i_{p}} \wedge d x_{j_{1}} \wedge \cdots \wedge d x_{j_{q}}
$$

If I and J have an element in common, then the discussion in Sec. 10.13 shows that $d x_{I} \wedge d x_{J}=0$. If $I$ and $J$ have no element in common, let us write $[I, J]$ for the increasing $(p+q)$-index which is obtained by arranging the members of $I \cup J$ in increasing order. Then $d x_{[I, J]}$ is a basic $(p+q)$-form. We claim that

$$
d x_{I} \wedge d x_{J}=(-1)^{\alpha} d x_{[I, J]}
$$

where $\alpha$ is the number of differences $j_{t}-i_{s}$ that are negative. (The number of positive differences is thus $\mathrm{pq}-\alpha$.)

To prove (10.53), perform the following operations on the numbers

$$
i_{1}, \ldots, i_{p}, j_{1}, \ldots, j_{q}
$$

Move $i_{p}$ to the right, step by step, until its right neighbor is larger than $i_{p}$. The number of steps is the number of subscripts $t$ such that $i_{p}<j_{t}$. (Note that 0 steps are distinct possibility.) Then do the same for $i_{p-1}, \ldots, i_{1}$. The total number of steps taken is $\alpha$. The final arrangement reached is $[I, J]$. Each step, when applied to the right side of (10.52), multiplies $d x_{I} \wedge d x_{J}$ by -1 . Hence (10.53) holds. Note that the right side of (10.53) is the standard presentation of $d x_{I} \wedge d x_{J}$.

Next, let $\mathrm{K}=\left(\mathrm{k}_{1}, \ldots, \mathrm{k}_{\mathrm{r}}\right)$ be an increasing r -index in $\{1, \ldots, \mathrm{n}\}$. We shall use

(10.53) to prove that

$$
\left(\mathrm{dx}_{\mathrm{I}} \wedge \mathrm{dx}_{\mathrm{J}}\right) \wedge \mathrm{dx}_{\mathrm{K}}=\mathrm{dx}_{\mathrm{I}} \wedge\left(\mathrm{dx}_{\mathrm{J}} \wedge \mathrm{dx}_{\mathrm{K}}\right)
$$

If any of the two sets $\mathrm{I}, \mathrm{J}, \mathrm{K}$ have an element in common, then each side of (10.55) is 0 , hence they are equal. So, let us assume that $\mathrm{I}, \mathrm{J}, \mathrm{K}$ are pairwise disjoint. Let $[I, J, K]$ denote the increasing $(p+q+r)$-index obtained from their union. Associate $\beta$ with the ordered pair $(J, K)$ and $\gamma$ with the ordered pair $(I, K)$ in the way that $\alpha$ was associated with $(I, J)$ in (10.53). The left side of (10.55) is then

$$
(-1)^{\alpha} \mathrm{dx}_{[I, J]} \wedge \mathrm{dx}_{\mathrm{K}}=(-1)^{\alpha}(-1)^{\beta+\gamma} \mathrm{dx}_{[I, J, K]}
$$

by two applications of (10.53), and the right side of (10.55) is

$$
(-1)^{\beta} \mathrm{dx}_{\mathrm{I}} \wedge \mathrm{dx}_{[\mathrm{J}, \mathrm{~K}]}=(-1)^{\beta}(-1)^{\alpha+\gamma} \mathrm{dx}_{[I, J, K]}
$$

Hence (10.55) is correct.
10.17 Multiplication. Suppose $\omega$ and $\lambda$ are p - and q -forms, respectively, in some open set $E \subset \mathbb{R}^{n}$, with standard presentations

$$
\omega=\sum_{I} b_{I}(\mathbf{x}) d x_{I}, \quad \lambda=\sum_{J} c_{J}(\mathbf{x}) d x_{J}
$$

where I and J range over all increasing p -indices and over all increasing q -indices taken from the set $\{1, \ldots, n\}$. Their product, denoted by the symbol $\omega \wedge \lambda$, is defined to be

$$
\omega \wedge \lambda=\sum_{I, J} b_{I}(\mathbf{x}) c_{J}(\mathbf{x}) d x_{I} \wedge d x_{J}
$$

In this sum, I and J range independently over their possible values, and $d x_{I} \wedge d x_{J}$ is as in Sec. 10.16. Thus $\omega \wedge \lambda$ is a $(p+q)$-form in $E$.

It is quite easy to see (we leave the details as an exercise) that the distributive laws

$$
\left(\omega_{1}+\omega_{2}\right)+\lambda=\left(\omega_{1} \wedge \lambda\right)+\left(\omega_{2} \wedge \lambda\right)
$$

and

$$
\omega \wedge\left(\lambda_{1} \wedge \lambda_{2}\right)=\left(\omega \wedge \lambda_{1}\right)+\left(\omega \wedge \lambda_{2}\right)
$$

hold, with respect to the addition defined in Sec. 10.13. If these distributive laws are combined with (10.55), we obtain the associative law

$$
(\omega \wedge \lambda) \wedge \sigma=\omega \wedge(\lambda \wedge \sigma)
$$

for arbitrary forms $\omega, \lambda, \sigma$ in $E$.
In this discussion it was tacitly assumed that $p \geq 1$ and $q \geq 1$. The product of

a 0 -form f with the p-form $\omega$ given by (10.56) is simply defined to be the p-form

$$
\mathrm{f} \omega=\omega \mathrm{f}=\sum_{\mathrm{I}} \mathrm{f}(\mathbf{x}) \mathrm{b}_{\mathrm{I}}(\mathbf{x}) \mathrm{dx}_{\mathrm{I}}
$$

It is customary to write $\mathrm{f} \omega$, rather than $\mathrm{f} \wedge \omega$, when f is a 0 -form.
We shall now define a differentiation operator d which associates a ( $k+1$ )-form $\mathrm{d} \omega$ to each k -form $\omega$ of class $\mathscr{C}^{1}$ in some open set $\mathrm{E} \subset \mathbb{R}^{n}$.
10.18 Definition (Differentiation). A 0 -form of class $\mathscr{C}^{1}$ in E is just a real function $\mathrm{f} \in \mathscr{C}^{1}(\mathrm{E})$ and we define

$$
\mathrm{df}=\sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{i}} \mathrm{f}\right)(\mathbf{x}) \mathrm{dx}_{\mathrm{i}}
$$

If $\omega=\Sigma \mathrm{b}_{\mathrm{I}}(\mathbf{x}) \mathrm{dx}_{\mathrm{I}}$ is the standard presentation of a k -form $\omega$ and $\mathrm{b}_{\mathrm{I}} \in \mathscr{C}^{1}(\mathrm{E})$ for each increasing k -index I , then we define

$$
\mathrm{d} \omega=\sum_{\mathrm{I}}\left(\mathrm{db}_{\mathrm{I}}\right) \wedge \mathrm{dx}_{\mathrm{I}}
$$

10.19 Example. Suppose E is open in $\mathbb{R}^{n}, \mathrm{f} \in \mathscr{C}^{1}(\mathrm{E})$, and $\gamma$ is a continuously differentiable curve in E with domain $[0,1]$. By (10.59) and (10.35),

$$
\int_{\gamma} \mathrm{df}=\int_{0}^{1} \sum_{\mathrm{i}=1}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{i}} \mathrm{f}\right)(\gamma(\mathrm{t})) \gamma_{\mathrm{i}}^{\prime}(\mathrm{t}) \mathrm{dt}
$$

By the chain rule, the last integrand is $(\mathrm{f} \circ \gamma)^{\prime}(\mathrm{t})$. Hence

$$
\int_{\gamma} \mathrm{df}=\mathrm{f}(\gamma(1))-\mathrm{f}(\gamma(0))
$$

and we see that $\int_{\gamma} \mathrm{df}$ is the same for all $\gamma$ with the same initial point and the same end point, as in (a) of Example 10.12.

Comparison with Example 10.12(b) shows therefore that the 1-form $x d y$ is not the derivative of any 0 -form f . This could also be deduced from part (b) of the following theorem, since

$$
\mathrm{d}(\mathrm{xdy})=\mathrm{dx} \wedge \mathrm{dy} \neq 0
$$

# 10.20 Theorem. 

(a) If $\omega$ and $\lambda$ are k - and m -forms, respectively, of class $\mathscr{C}^{1}$ in E , then

$$
\mathrm{d}(\omega \wedge \lambda)=(\mathrm{d} \omega) \wedge \lambda+(-1)^{\mathrm{k}} \omega \wedge \mathrm{~d} \lambda
$$

(b) If $\omega$ is of class $\mathscr{C}^{2}$ in E , then $\mathrm{d}^{2} \omega=0$.

Here $\mathrm{d}^{2} \omega$ means, of course, $\mathrm{d}(\mathrm{d} \omega)$.
Proof. Because of (10.57) and (10.60), (a) follows if (10.63) is proved for the special case

$$
\omega=\mathrm{fdx}_{\mathrm{I}}, \quad \lambda=\mathrm{gdx}_{\mathrm{J}}
$$

where $f, g \in \mathscr{C}^{1}(E), d x_{I}$ is a basic $k$-form, and $d x_{J}$ is a basic $m$-form. [If $k$ or $m$ are both 0 , simply omit $d x_{I}$ or $d x_{J}$ in (10.64); the proof that follows is unaffected by this.] Then

$$
\omega \wedge \lambda=\mathrm{fgdx}_{\mathrm{I}} \wedge \mathrm{dx}_{\mathrm{J}}
$$

Let us assume that I and J have no element in common. [In the other case, each of the three terms in (10.63) is 0 .] Then, using (10.53),

$$
\mathrm{d}(\omega \wedge \lambda)=\mathrm{d}\left(\mathrm{fgdx}_{\mathrm{I}} \wedge \mathrm{dx}_{\mathrm{J}}\right)=(-1)^{\alpha} \mathrm{d}\left(\mathrm{fgdx}_{[\mathrm{I}, \mathrm{~J}]}\right)
$$

By (10.59), $\mathrm{d}(\mathrm{fg})=\mathrm{fdg}+\mathrm{gdf}$. Hence (10.60) gives

$$
\begin{aligned}
\mathrm{d}(\omega \wedge \lambda) & =(-1)^{\alpha}(\mathrm{fdg}+\mathrm{gdf}) \wedge \mathrm{dx}_{[\mathrm{I}, \mathrm{~J}]} \\
& =(\mathrm{gdf}+\mathrm{fdg}) \wedge \mathrm{dx}_{\mathrm{I}} \wedge \mathrm{dx}_{\mathrm{J}}
\end{aligned}
$$

Since dg is a 1-form and $\mathrm{dx}_{\mathrm{I}}$ is a k -form, we have

$$
\mathrm{dg} \wedge \mathrm{dx}_{\mathrm{I}}=(-1)^{\mathrm{k}} \mathrm{dx}_{\mathrm{I}} \wedge \mathrm{dg}
$$

by (10.42). Hence

$$
\begin{aligned}
\mathrm{d}(\omega \wedge \lambda) & =\left(\mathrm{df} \wedge \mathrm{dx}_{\mathrm{I}}\right) \wedge\left(\mathrm{gdx}_{\mathrm{J}}\right)+(-1)^{\mathrm{k}}\left(\mathrm{fdx}_{\mathrm{I}}\right) \wedge\left(\mathrm{dg} \wedge \mathrm{dx}_{\mathrm{J}}\right) \\
& =(\mathrm{d} \omega) \wedge \lambda+(-1)^{\mathrm{k}} \omega \wedge \mathrm{~d} \lambda
\end{aligned}
$$

which proves (a). Note that the associative law (10.58) was used freely.
Let us prove (b) first for a 0 -form $\mathrm{f} \in \mathscr{C}^{2}$ :

$$
\begin{aligned}
\mathrm{d}^{2} \mathrm{f} & =\mathrm{d}\left(\sum_{\mathrm{j}=1}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}\right)(\mathbf{x}) \mathrm{dx}_{\mathrm{j}}\right) \\
& =\sum_{\mathrm{j}=1}^{\mathrm{n}} \mathrm{~d}\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}\right) \wedge \mathrm{dx}_{\mathrm{j}} \\
& =\sum_{\mathrm{i}, \mathrm{j}=1}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{ij}} \mathrm{f}\right)(\mathbf{x}) \mathrm{dx}_{\mathrm{i}} \wedge \mathrm{dx}_{\mathrm{j}}
\end{aligned}
$$

Since $D_{i j} f=D_{j i} f$ (Theorem 9.41) and $d x_{i} \wedge d x_{j}=-d x_{j} \wedge d x_{i}$, we see that $d^{2} f=$ 0 .

If $\omega=\mathrm{fdx}_{\mathrm{I}}$ as in (10.64), then $\mathrm{d} \omega=(\mathrm{df}) \wedge \mathrm{dx}_{\mathrm{I}}$. By (10.60), $\mathrm{d}\left(\mathrm{dx}_{\mathrm{I}}\right)=0$. Hence

(10.63) shows that

$$
\mathrm{d}^{2} \omega=\left(\mathrm{d}^{2} \mathrm{f}\right) \wedge \mathrm{dx}_{\mathrm{I}}=0
$$

10.21 Change of Variables. Suppose $E$ is an open set in $\mathbb{R}^{n}, T$ is a $\mathscr{C}^{1}$-mapping of $E$ into an open set $V \subset \mathbb{R}^{m}$, and $\omega$ is a $k$-form in $V$ whose standard presentation is

$$
\omega=\sum_{I} b_{I}(\mathbf{y}) d y_{I}
$$

(We use $\mathbf{y}$ for points of $V, \mathbf{x}$ for points of $E$.)
Let $t_{1}, \ldots, t_{m}$ be the components of $T$ : If

$$
\mathbf{y}=\left(y_{1}, \ldots, y_{m}\right)=T(\mathbf{x})
$$

then $y_{i}=t_{i}(\mathbf{x})$. As in (10.59),

$$
d t_{i}=\sum_{j=1}^{n}\left(D_{j} t_{i}\right)(x) d x_{j} \quad(1 \leq i \leq m)
$$

Thus each $d t_{i}$ is a 1-form in $E$.
The mapping $T$ transforms $\omega$ into a $k$-form $\omega_{T}$ in $E$, whose definition is

$$
\omega_{\mathrm{T}}=\sum_{\mathrm{I}} \mathrm{~b}_{\mathrm{I}}(\mathrm{~T}(\mathbf{x})) \mathrm{dt}_{\mathrm{i}_{1}} \wedge \cdots \wedge \mathrm{dt}_{\mathrm{i}_{\mathrm{k}}}
$$

In each summand of (10.67), $\mathrm{I}=\left(\mathrm{i}_{1}, \ldots, \mathrm{i}_{\mathrm{k}}\right)$ is an increasing k -index.
Our next theorem shows that addition, multiplication, and differentiation of forms are defined in such a way that they commute with changes of variables.
10.22 Theorem. With E and T as in Sec. 10.21, let $\omega$ and $\lambda$ be k - and m -forms in V , respectively. Then
(a) $(\omega+\lambda)_{T}=\omega_{T}+\lambda_{T}$ if $k=m$;
(b) $(\omega \wedge \lambda)_{T}=\omega_{T} \wedge \lambda_{T}$
(c) $\mathrm{d}\left(\omega_{\mathrm{T}}\right)=(\mathrm{d} \omega)_{T}$ if $\omega$ is of class $\mathscr{C}^{1}$ and T is of class $\mathscr{C}^{2}$.

Proof. Part (a) follows immediately from the definitions. Part (b) is almost as obvious, once we realize that

$$
\left(\mathrm{d} y_{i_{1}} \wedge \cdots \wedge \mathrm{~d} y_{i_{r}}\right)_{T}=\mathrm{dt}_{i_{1}} \wedge \cdots \wedge \mathrm{dt}_{i_{r}}
$$

regardless of whether $\left(i_{1}, \ldots, i_{r}\right)$ is increasing or not; (10.68) holds because the same number of minus signs are needed on each side of (10.68) to produce increasing rearrangements.

We turn to the proof of (c). If $f$ is a 0 -form of class $\mathscr{C}^{1}$ in $V$, then

$$
f_{T}(\mathbf{x})=f(T(\mathbf{x})), \quad \mathrm{df}=\sum_{i}\left(D_{i} f\right)(\mathbf{y}) \mathrm{d} y_{i}
$$

By the chain rule, it follows that

$$
\begin{aligned}
\mathrm{d}\left(\mathrm{f}_{\mathrm{T}}\right) & =\sum_{\mathrm{j}}\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{T}}\right)(\mathbf{x}) \mathrm{dx}_{\mathrm{j}} \\
& =\sum_{\mathrm{j}} \sum_{\mathrm{i}}\left(\mathrm{D}_{\mathrm{i}} \mathrm{f}\right)\left(\mathrm{T}(\mathbf{x})\right)\left(\mathrm{D}_{\mathrm{j}} \mathrm{t}_{\mathrm{i}}\right)(\mathbf{x}) \mathrm{dx}_{\mathrm{j}} \\
& =\sum_{\mathrm{i}}\left(\mathrm{D}_{\mathrm{i}} \mathrm{f}\right)\left(\mathrm{T}(\mathbf{x})\right) \mathrm{dt}_{\mathrm{i}} \\
& =(\mathrm{df})_{\mathrm{T}} .
\end{aligned}
$$

If $\mathrm{d} y_{\mathrm{I}}=\mathrm{d} y_{\mathrm{i}_{1}} \wedge \cdots \wedge \mathrm{~d} y_{\mathrm{i}_{\mathrm{k}}}$, then $\left(\mathrm{d} y_{\mathrm{I}}\right)_{\mathrm{T}}=\mathrm{dt}_{\mathrm{i}_{1}} \wedge \cdots \wedge \mathrm{dt}_{\mathrm{i}_{\mathrm{k}}}$ and Theorem 10.20 shows that

$$
\mathrm{d}\left(\left(\mathrm{~d} y_{\mathrm{I}}\right)_{\mathrm{T}}\right)=0
$$

(This is where the assumption $\mathrm{T} \in \mathscr{C}^{2}$ is used.)
Assume now that $\omega=\mathrm{f} \mathrm{d} y_{\mathrm{I}}$. Then

$$
\omega_{\mathrm{T}}=\mathrm{f}_{\mathrm{T}}(\mathbf{x})\left(\mathrm{d} y_{\mathrm{I}}\right)_{\mathrm{T}}
$$

and the preceding calculations lead to

$$
\begin{aligned}
\mathrm{d}\left(\omega_{\mathrm{T}}\right) & =\mathrm{d}\left(\mathrm{f}_{\mathrm{T}}\right) \wedge\left(\mathrm{d} y_{\mathrm{I}}\right)_{\mathrm{T}}=(\mathrm{df})_{\mathrm{T}} \wedge\left(\mathrm{~d} y_{\mathrm{I}}\right)_{\mathrm{T}} \\
& =\left((\mathrm{df}) \wedge \mathrm{d} y_{\mathrm{I}}\right)_{\mathrm{T}}=(\mathrm{d} \omega)_{\mathrm{T}}
\end{aligned}
$$

The first equality holds by (10.63) and (10.70), the second by (10.69), the third by part (b), and the last by the definition of $\mathrm{d} \omega$. The general case of (c) follows from the special case just proved, if we apply (a). This completes the proof.

Our next objective is Theorem 10.25. This will follow directly from two other important transformation properties of differential forms, which we state first.
10.23 Theorem. Suppose T is a $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ into an open set $\mathrm{V} \subset \mathbb{R}^{\mathrm{m}}, \mathrm{S}$ is a $\mathscr{C}^{1}$-mapping of V into an open set $\mathrm{W} \subset \mathbb{R}^{\mathrm{p}}$, and $\omega$ is a k -form in W , so that $\omega_{\mathrm{S}}$ is a k -form in V and both $\left(\omega_{\mathrm{S}}\right)_{\mathrm{T}}$ and $\omega_{\mathrm{ST}}$ are k -forms in E , where ST is defined by $(\mathrm{ST})(\mathbf{x})=\mathrm{S}(\mathrm{T}(\mathbf{x}))$. Then

$$
\left(\omega_{\mathrm{S}}\right)_{\mathrm{T}}=\omega_{\mathrm{ST}}
$$

Proof. If $\omega$ and $\lambda$ are forms in $W$, Theorem 10.22 shows that

$$
\left((\omega \wedge \lambda)_{\mathrm{S}}\right)_{\mathrm{T}}=\left(\omega_{\mathrm{S}} \wedge \lambda_{\mathrm{S}}\right)_{\mathrm{T}}=\left(\omega_{\mathrm{S}}\right)_{\mathrm{T}} \wedge\left(\lambda_{\mathrm{S}}\right)_{\mathrm{T}}
$$

and

$$
(\omega \wedge \lambda)_{\mathrm{ST}}=\omega_{\mathrm{ST}} \wedge \lambda_{\mathrm{ST}}
$$

Thus if (10.71) holds for $\omega$ and for $\lambda$, it follows that (10.71) also holds for $\omega \wedge$

$\lambda$. Since every form can be built up from 0 -forms and 1 -forms by addition and multiplication, and since (10.71) is trivial for 0 -forms, it is enough to prove (10.71) in the case $\omega=\mathrm{d} z_{\mathrm{q}}, \mathrm{q}=1, \ldots, \mathrm{p}$. (We denote the points of $\mathrm{E}, \mathrm{V}, \mathrm{W}$ by $\mathbf{x}, \mathbf{y}, \mathbf{z}$, respectively.)

Let $t_{1}, \ldots, t_{m}$ be the components of $T$, let $s_{1}, \ldots, s_{p}$ be the components of $S$, and let $r_{1}, \ldots, r_{p}$ be the components of ST. If $\omega=\mathrm{d} z_{\mathrm{q}}$, then

$$
\omega_{S}=\mathrm{ds}_{\mathrm{q}}=\sum_{\mathrm{j}}\left(\mathrm{D}_{\mathrm{j}} \mathrm{~s}_{\mathrm{q}}\right)(\mathbf{y}) \mathrm{dy}_{\mathrm{j}}
$$

so that the chain rule implies

$$
\begin{aligned}
\left(\omega_{S}\right)_{T} & =\sum_{j}\left(D_{j} s_{q}\right)(T(\mathbf{x})) d t_{j} \\
& =\sum_{j}\left(D_{j} s_{q}\right)(T(\mathbf{x})) \sum_{i}\left(D_{i} t_{j}\right)(\mathbf{x}) d x_{i} \\
& =\sum_{i}\left(D_{i} r_{q}\right)(\mathbf{x}) d x_{i}=d r_{q}=\omega_{S T}
\end{aligned}
$$

10.24 Theorem. Suppose $\omega$ is a k -form in an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}, \Phi$ is a k -surface in E with parameter domain $\mathrm{D} \subset \mathbb{R}^{\mathrm{k}}$, and $\Delta$ is the k -surface in $\mathbb{R}^{\mathrm{k}}$ with parameter domain D defined by $\Delta(\mathbf{u})=\mathbf{u}(\mathbf{u} \in \mathrm{D})$. Then

$$
\int_{\Phi} \omega=\int_{\Delta} \omega_{\Phi}
$$

Proof. We need only consider the case

$$
\omega=a(\mathbf{x}) d x_{i_{1}} \wedge \cdots \wedge d x_{i_{k}}
$$

If $\phi_{1}, \ldots, \phi_{n}$ are the components of $\Phi$, then

$$
\omega_{\Phi}=a(\Phi(\mathbf{u})) \mathrm{d} \phi_{i_{1}} \wedge \cdots \wedge \mathrm{~d} \phi_{i_{k}}
$$

The theorem will follow if we can show that

$$
\mathrm{d} \phi_{\mathrm{i}_{1}} \wedge \cdots \wedge \mathrm{~d} \phi_{\mathrm{i}_{\mathrm{k}}}=\mathrm{J}(\mathbf{u}) \mathrm{du}_{1} \wedge \cdots \wedge \mathrm{du}_{\mathrm{k}}
$$

where

$$
J(\mathbf{u})=\frac{\partial\left(x_{i_{1}}, \ldots, x_{i_{k}}\right)}{\partial\left(u_{1}, \ldots, u_{k}\right)}
$$

since (10.72) implies

$$
\begin{aligned}
\int_{\Phi} \omega & =\int_{\mathrm{D}} \mathfrak{a}(\Phi(\mathbf{u})) \mathrm{J}(\mathbf{u}) \mathrm{d} \mathbf{u} \\
& =\int_{\Delta} \mathfrak{a}(\Phi(\mathbf{u})) \mathrm{J}(\mathbf{u}) \mathrm{du}_{1} \wedge \cdots \wedge \mathrm{du}_{\mathrm{k}}=\int_{\Delta} \omega_{\Phi}
\end{aligned}
$$

Let $[A]$ be the $\mathrm{k} \times \mathrm{k}$ matrix with entries

$$
\alpha(p, q)=\left(D_{q} \phi_{i_{p}}\right)(\mathbf{u}) \quad(p, q=1, \ldots, k)
$$

Then

$$
\mathrm{d} \phi_{i_{p}}=\sum_{q} \alpha(p, q) d u_{q}
$$

so that

$$
\mathrm{d} \phi_{i_{1}} \wedge \cdots \wedge \mathrm{~d} \phi_{i_{\mathrm{k}}}=\sum \alpha\left(1, \mathrm{q}_{1}\right) \cdots \alpha\left(\mathrm{k}, \mathrm{q}_{\mathrm{k}}\right) \mathrm{du}_{\mathrm{q}_{1}} \wedge \cdots \wedge \mathrm{du}_{\mathrm{q}_{\mathrm{k}}}
$$

In this last sum, $\mathrm{q}_{1}, \ldots, \mathrm{q}_{\mathrm{k}}$ range independently over $1, \ldots, \mathrm{k}$. The anticommutative relation (10.42) implies that

$$
d u_{q_{1}} \wedge \cdots \wedge d u_{q_{k}}=s\left(q_{1}, \ldots, q_{k}\right) d u_{1} \wedge \cdots \wedge d u_{k}
$$

where $s$ is as in Definition 9.33; applying this definition, we see that

$$
\mathrm{d} \phi_{i_{1}} \wedge \cdots \wedge \mathrm{~d} \phi_{i_{\mathrm{k}}}=\operatorname{det}[A] \mathrm{du}_{1} \wedge \cdots \wedge \mathrm{du}_{\mathrm{k}}
$$

since $J(\mathbf{u})=\operatorname{det}[A]$, (10.72) is proved.
The final result of this section combines the two preceding theorems.
10.25 Theorem. Suppose T is a $\mathscr{C}^{1}$-mapping of an open set $\mathrm{E} \subset \mathbb{R}^{n}$ into an open set $\mathrm{V} \subset \mathbb{R}^{m}, \Phi$ is a k-surface in E , and $\omega$ is a k -form in V . Then

$$
\int_{\mathrm{T} \Phi} \omega=\int_{\Phi} \omega_{\mathrm{T}}
$$

Proof. Let D be the parameter domain of $\Phi$ (hence also of $\mathrm{T} \Phi$ ) and define $\Delta$ as in Theorem 10.24. Then

$$
\int_{\mathrm{T} \Phi} \omega=\int_{\Delta} \omega_{\mathrm{T} \Phi}=\int_{\Delta}\left(\omega_{\mathrm{T}}\right)_{\Phi}=\int_{\Phi} \omega_{\mathrm{T}}
$$

The first of these equalities is Theorem 10.24 applied to $\mathrm{T} \Phi$ in place of $\Phi$. The second follows from Theorem 10.23. The third is Theorem 10.24 with $\omega_{\mathrm{T}}$ in place of $\omega$.

# SIMPLEXES AND CHAINS 

10.26 Affine Simplexes. A mapping $\mathbf{f}$ that carries a vector space $X$ into a vector space $Y$ is said to be affine if $\mathbf{f}-\mathbf{f}(\mathbf{0})$ is linear. In other words, the requirement is that

$$
\mathbf{f}(\mathbf{x})=\mathbf{f}(\mathbf{0})+A \mathbf{x}
$$

for some $A \in L(X, Y)$.
An affine mapping of $\mathbb{R}^{\mathrm{k}}$ into $\mathbb{R}^{\mathrm{n}}$ is thus determined if we know $\mathbf{f}(\mathbf{0})$ and $\mathbf{f}\left(\mathbf{e}_{i}\right)$ for $1 \leq \mathrm{i} \leq \mathrm{k}$; as usual, $\left\{\mathbf{e}_{1}, \ldots, \mathbf{e}_{\mathrm{k}}\right\}$ is the standard basis of $\mathbb{R}^{\mathrm{k}}$.

We define the standard simplex $\mathrm{Q}^{\mathrm{k}}$ to be the set of all $\mathbf{u} \in \mathbb{R}^{\mathrm{k}}$ of the form

$$
\mathbf{u}=\sum_{i=1}^{k} \alpha_{i} \mathbf{e}_{i}
$$

such that $\alpha_{i} \geq 0$ for $i=1, \ldots, k$ and $\Sigma \alpha_{i} \leq 1$.
Assume now that $\mathbf{p}_{0}, \mathbf{p}_{1}, \ldots, \mathbf{p}_{\mathrm{k}}$ are points of $\mathbb{R}^{\mathrm{n}}$. The oriented affine k -simplex

$$
\sigma=\left[\mathbf{p}_{0}, \mathbf{p}_{1}, \ldots, \mathbf{p}_{\mathrm{k}}\right]
$$

is defined to be the k -surface in $\mathbb{R}^{n}$ with parameter domain $Q^{k}$ which is given by the affine mapping

$$
\sigma\left(\alpha_{1} \mathbf{e}_{1}+\cdots+\alpha_{k} \mathbf{e}_{k}\right)=\mathbf{p}_{0}+\sum_{i=1}^{k} \alpha_{i}\left(\mathbf{p}_{i}-\mathbf{p}_{0}\right)
$$

Note that $\sigma$ is characterized by

$$
\sigma(\mathbf{0})=\mathbf{p}_{0}, \quad \sigma\left(\mathbf{e}_{i}\right)=\mathbf{p}_{i} \quad(\text { for } 1 \leq i \leq k)
$$

and that

$$
\sigma(\mathbf{u})=\mathbf{p}_{0}+A \mathbf{u} \quad\left(\mathbf{u} \in \mathrm{Q}^{\mathrm{k}}\right)
$$

where $A \in L\left(\mathbb{R}^{\mathrm{k}}, \mathbb{R}^{\mathrm{n}}\right)$ and $A \mathbf{e}_{i}=\mathbf{p}_{i}-\mathbf{p}_{0}$ for $1 \leq i \leq k$.
We call $\sigma$ oriented to emphasize that the ordering of the vertices $\mathbf{p}_{0}, \ldots, \mathbf{p}_{\mathrm{k}}$ is taken into account. If

$$
\bar{\sigma}=\left\{\mathbf{p}_{i_{0}}, \mathbf{p}_{i}, \ldots, \mathbf{p}_{i_{k}}\right\}
$$

where $\left\{i_{0}, i_{1}, \ldots, i_{k}\right\}$ is a permutation of the ordered set $\{0,1, \ldots, k\}$, we adopt the notation.

$$
\bar{\sigma}=s\left(i_{0}, i_{1}, \ldots, i_{k}\right) \sigma
$$

where $s$ is the function defined on Definition 9.33. Thus $\bar{\sigma}= \pm \sigma$, depending on

whether $s=1$ or $s=-1$. Strictly speaking, having adopted (10.75) and (10.76) as the definition of $\sigma$, we should not write $\bar{\sigma}=\sigma$ unless $i_{0}=0, \ldots, i_{k}=k$, even if $s\left(i_{0}, \ldots, i_{k}\right)=1$; what we have here is an equivalence relation, not an equality. However, for our purposes, the notation is justified by Theorem 10.27.

If $\bar{\sigma}=\varepsilon \sigma$ (using the above convention) and if $\varepsilon=1$, we say that $\bar{\sigma}$ and $\sigma$ have the same orientation; if $\varepsilon=-1, \bar{\sigma}$ and $\sigma$ are said to have opposite orientations. Note that we have not defined what we mean by the "orientation of a simplex." What we have defined is a relation between pairs of simplexes having the same set of vertices, the relation being that of "having the same orientation."

There is, however, one situation where the orientation of a simplex can be defined in a natural way. This happens with $n=k$ and when the vectors $\mathbf{p}_{i}-\mathbf{p}_{0}$ $(1 \leq i \leq k)$ are independent. In that case, the linear transformation of $A$ that appears in (10.78) is invertible, and its determinant (with is the same as the Jacobian of $\sigma$ ) is not 0 . Then $\sigma$ is said to be positively (or negatively) oriented if $\operatorname{det} A$ is positive (or negative). In particular, the simplex $\left[0, \mathbf{e}_{1}, \ldots, \mathbf{e}_{k}\right]$ in $\mathbb{R}^{k}$, given by the identity mapping, has positive orientation.

So far we have assumed that $\mathrm{k} \geq 1$. An oriented 0 -simplex is defined to be a point with a sign attached. We write $\sigma=+\mathbf{p}_{0}$ or $\sigma=-\mathbf{p}_{0}$. If $\sigma=\varepsilon \mathbf{p}_{0}(\varepsilon= \pm 1)$ and if $f$ is a 0 -form (i.e., a real function), we defined

$$
\int_{\sigma} f=\varepsilon f\left(p_{0}\right)
$$

10.27 Theorem. If $\sigma$ is an oriented rectilinear k-simplex in an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ and if $\bar{\sigma}=\varepsilon \sigma$, then

$$
\int_{\bar{\sigma}} \omega=\varepsilon \int_{\sigma} \omega
$$

for every k -form $\omega$ in E .
Proof. For $\mathrm{k}=0,(10.81)$ follows from the preceding definition. So we assume $\mathrm{k} \geq 1$ and assume that $\sigma$ is given by (10.75).

Suppose $1 \leq \mathrm{j} \leq \mathrm{k}$ and suppose $\bar{\sigma}$ is obtained from $\sigma$ by interchanging $\mathbf{p}_{0}$ and $\mathbf{p}_{\mathrm{j}}$. Then $\varepsilon=-1$ and

$$
\bar{\sigma}(\mathbf{u})=\mathbf{p}_{\mathrm{j}}+\mathrm{Bu} \quad\left(\mathbf{u} \in \mathrm{Q}^{\mathrm{k}}\right)
$$

where $B$ is the linear mapping of $\mathbb{R}^{k}$ into $\mathbb{R}^{n}$ defined by $B \mathbf{e}_{j}=\mathbf{p}_{0}-\mathbf{p}_{j}, B \mathbf{e}_{i}=$ $\mathbf{p}_{i}-\mathbf{p}_{j}$ if $i \neq j$. If we write $A \mathbf{e}_{i}=\mathbf{x}_{i}(1 \leq i \leq k)$, where $A$ is given by (10.78), the column vectors of $B$ (that is, the vectors $B \mathbf{e}_{i}$ ) are

$$
\mathbf{x}_{1}-\mathbf{x}_{\mathrm{j}}, \ldots, \mathbf{x}_{\mathrm{j}-1}-\mathbf{x}_{\mathrm{j}},-\mathbf{x}_{\mathrm{j}}, \mathbf{x}_{\mathrm{j}+1}-\mathbf{x}_{\mathrm{j}}, \ldots, \mathbf{x}_{\mathrm{k}}-\mathbf{x}_{\mathrm{j}}
$$

If we subtract the jth column from each of the others, none of the determinants in (10.35) are affected, and we obtain columns $\mathbf{x}_{1}, \ldots, \mathbf{x}_{\mathrm{j}-1},-\mathbf{x}_{\mathrm{j}}, \mathbf{x}_{\mathrm{j}+1}, \ldots, \mathbf{x}_{\mathrm{k}}$. These differ from those of $A$ only in the sign of the $j$ th column. Hence (10.81) holds for

this case.
Suppose next that $0<i<j \leq k$ and that $\bar{\sigma}$ is obtained from $\sigma$ by interchanging $\mathbf{p}_{i}$ and $\mathbf{p}_{j}$. Then $\bar{\sigma}(\mathbf{u})=\mathbf{p}_{0}+\mathrm{C} \mathbf{u}$, where C has the same columns as A , except that the ith and jth columns have been interchanged. This again implies that (10.81) holds, since $\varepsilon=-1$.

The general case follows, since every permutation of $\{0,1, \ldots, \mathrm{k}\}$ is a composition of the special cases we have just dealt with.
10.28 Affine Chains. An affine k -chain $\Gamma$ in an open set $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ is a collection of finitely many oriented affine k -simplexes $\sigma_{1}, \ldots, \sigma_{\mathrm{r}}$ in E . These need not be distinct; a simplex may thus occur in $\Gamma$ with a certain multiplicity.

If $\Gamma$ is as above, and if $\omega$ is a k -form in E , we define

$$
\int_{\Gamma} \omega=\sum_{i=1}^{r} \int_{\sigma_{i}} \omega
$$

We may view a k -surface $\Phi$ in E as a function whose domain is the collection of all k -forms in E and which assigns the number $\int_{\Phi} \omega$ to $\omega$. Since real valued functions can be added (as in Definition 4.3), this suggests the use of the notation

$$
\Gamma=\sigma_{1}+\cdots+\sigma_{\mathrm{r}}
$$

or, more compactly,

$$
\Gamma=\sum_{i=1}^{r} \sigma_{i}
$$

to state the fact that (10.82) holds for every k -form $\omega$ in E .
To avoid misunderstanding, we point out explicitly that the notations introduced by (10.83) and (10.80) have to be handled with care. The point is that every oriented affine k -simplex $\sigma$ in $\mathbb{R}^{\mathrm{n}}$ is a function in two ways, with different domains and different ranges, and that therefore two entirely different operators of addition are possible. Originally, $\sigma$ was defined as an $\mathbb{R}^{\mathrm{n}}$-valued function with domain $\mathrm{Q}^{\mathrm{k}}$; accordingly, $\sigma_{1}+\sigma_{2}$ could be interpreted to be the function $\sigma$ that assigns the vector $\sigma_{1}(\mathbf{u})+\sigma_{2}(\mathbf{u})$ to every $\mathbf{u} \in \mathrm{Q}^{\mathrm{k}}$; note that $\sigma$ is then again an oriented affine k -simplex in $\mathbb{R}^{\mathrm{n}}$ ! This is not what is meant by (10.83).

For example, if $\sigma_{2}=-\sigma_{1}$ as in (10.80) (that is to say, if $\sigma_{1}$ and $\sigma_{2}$ have the same set of vertices but are oppositely oriented) and if $\Gamma=\sigma_{1}+\sigma_{2}$, then $\int_{\Gamma} \omega=0$ for all $\omega$, and we may express this by writing $\Gamma=0$ or $\sigma_{1}+\sigma_{2}=0$. This does not mean that $\sigma_{1}(\mathbf{u})+\sigma_{2}(\mathbf{u})$ is the null vector in $\mathbb{R}^{\mathrm{n}}$.
10.29 Definition (Boundaries). For $\mathrm{k} \geq 1$, the boundary of the oriented affine k simplex

$$
\sigma=\left[\mathbf{p}_{0}, \mathbf{p}_{1}, \ldots, \mathbf{p}_{\mathrm{k}}\right]
$$

is defined to be the affine $(k-1)$-chain

$$
\partial \sigma=\sum_{j=0}^{k}(-1)^{j}\left[\mathbf{p}_{0}, \ldots, \mathbf{p}_{j-1}, \mathbf{p}_{j+1}, \ldots, \mathbf{p}_{k}\right]
$$

For example, if $\sigma=\left[\mathbf{p}_{0}, \mathbf{p}_{1}, \mathbf{p}_{2}\right]$, then

$$
\partial \sigma=\left[\mathbf{p}_{1}, \mathbf{p}_{2}\right]-\left[\mathbf{p}_{0}, \mathbf{p}_{2}\right]+\left[\mathbf{p}_{0}, \mathbf{p}_{1}\right]=\left[\mathbf{p}_{0}, \mathbf{p}_{1}\right]+\left[\mathbf{p}_{1}, \mathbf{p}_{2}\right]+\left[\mathbf{p}_{2}, \mathbf{p}_{0}\right]
$$

which coincides with the usual notion of the oriented boundary of a triangle.
For $1 \leq \mathrm{j} \leq \mathrm{k}$, observe that the simplex $\sigma_{j}=\left[\mathbf{p}_{0}, \cdots, \mathbf{p}_{j-1}, \mathbf{p}_{j+1}, \ldots, \mathbf{p}_{k}\right]$ which occurs in (10.85) has $Q^{k-1}$ as its parameter domain and that it is defined by

$$
\sigma_{j}(\mathbf{u})=\mathbf{p}_{0}+B \mathbf{u} \quad\left(\mathbf{u} \in Q^{k-1}\right)
$$

where $B$ is the linear mapping from $\mathbb{R}^{k-1}$ to $\mathbb{R}^{n}$ determined by

$$
\mathrm{Be}_{\mathrm{i}}= \begin{cases}\mathbf{p}_{\mathrm{i}}-\mathbf{p}_{0} & (\text { if } 1 \leq \mathrm{i} \leq \mathrm{j}-1) \\ \mathbf{p}_{\mathrm{i}+1}-\mathbf{p}_{0} & (\text { if } \mathrm{j} \leq \mathrm{i} \leq \mathrm{k}-1)\end{cases}
$$

The simplex

$$
\sigma_{0}=\left[\mathbf{p}_{1}, \mathbf{p}_{2}, \ldots, \mathbf{p}_{k}\right]
$$

which also occurs in (10.85), is given by the mapping

$$
\sigma_{0}(\mathbf{u})=\mathbf{p}_{1}+B \mathbf{u}
$$

where $\mathrm{Be}_{\mathrm{i}}=\mathbf{p}_{\mathrm{i}+1}-\mathbf{p}_{1}$ for $1 \leq \mathrm{i} \leq \mathrm{k}-1$.
10.30 Differentiable Simplexes and Chains. Let $T$ be a $\mathscr{C}^{2}$-mapping of an open set $E \subset \mathbb{R}^{n}$ into an open set $V \subset \mathbb{R}^{m} ; T$ need not be one-to-one. If $\sigma$ is an oriented affine k -simplex in $E$, then the composite mapping $\Phi=T \circ \sigma$ (which we shall sometimes write in the simpler form $T \sigma$ ) is a k-surface in $V$, with parameter domain $Q^{k}$. We call $\Phi$ an oriented k-simplex of class $\mathscr{C}^{2}$.

A finite collection $\Psi$ of oriented k -simplexes $\Phi_{1}, \ldots, \Phi_{\mathrm{r}}$ of class $\mathscr{C}^{2}$ in $V$ is called a k-chain of class $\mathscr{C}^{2}$ in $V$. If $\omega$ is a k -form in $V$, we define

$$
\int_{\Psi} \omega=\sum_{i=1}^{r} \int_{\Phi_{i}} \omega
$$

and use the corresponding notation $\Psi=\Sigma \Phi_{i}$.
If $\Gamma=\Sigma \sigma_{i}$ is an affine chain and if $\Phi_{i}=T \circ \sigma_{i}$, we also write $\Psi=T \circ \Gamma$, or

$$
T\left(\sum \sigma_{i}\right)=\sum T \sigma_{i}
$$

The boundary $\partial \Phi$ of the oriented k -simplex $\Phi=T \circ \sigma$ is defined to be the

$(k-1)$-chain

$$
\partial \Phi=\mathrm{T}(\partial \sigma)
$$

In justification of (10.89), observe that if T is affine, then $\Phi=\mathrm{T} \circ \sigma$ is an oriented affine k -simplex, in which case (10.89) is not a matter of definition, but is seen to be a consequence of (10.85). Thus (10.89) generalizes this special case.

It is immediate that $\partial \Phi$ is of class $\mathscr{C}^{2}$ if this is true of $\Phi$.
Finally, we define the boundary $\partial \Psi$ of the k -chain $\Psi=\Sigma \Phi_{\mathrm{i}}$ to be the $(\mathrm{k}-1)$ chain

$$
\partial \Psi=\sum \partial \Phi_{\mathrm{i}}
$$

10.31 Positively Oriented Boundaries. So far we have associated boundaries to chains, not to subsets of $\mathbb{R}^{n}$. This notion of boundary is exactly the one that is most suitable for the statement and proof of Stokes' theorem. However, in applications, especially in $\mathbb{R}^{2}$ or $\mathbb{R}^{3}$, it is customary and convenient to talk about "oriented boundaries" of certain sets as well. We shall now describe this briefly.

Let $Q^{n}$ be the standard simplex in $\mathbb{R}^{n}$, let $\sigma_{0}$ be the identity mapping with domain $Q^{n}$. As we saw in Theorem 10.26, $\sigma_{0}$ may be regarded as a positively oriented n -simplex in $\mathbb{R}^{n}$. Its boundary $\partial \sigma_{0}$ is an affine $(n-1)$-chain. This chain is called the positively oriented boundary of the set $Q^{n}$.

For example, the positively oriented boundary of $Q^{3}$ is

$$
\left[\mathbf{e}_{1}, \mathbf{e}_{2}, \mathbf{e}_{3}\right]-\left[\mathbf{0}, \mathbf{e}_{2}, \mathbf{e}_{3}\right]+\left[\mathbf{0}, \mathbf{e}_{1}, \mathbf{e}_{3}\right]-\left[\mathbf{0}, \mathbf{e}_{1}, \mathbf{e}_{2}\right]
$$

Now let $T$ be a 1-1 mapping of $Q^{n}$ into $\mathbb{R}^{n}$, of class $\mathscr{C}^{2}$, whose Jacobian is positive (at least in the interior of $Q^{n}$ ). Let $E=T\left(Q^{n}\right)$. By the inverse function theorem, $E$ is the closure of an open subset of $\mathbb{R}^{n}$. We define the positively oriented boundary of the set $E$ to be the $(n-1)$-chain

$$
\partial \mathrm{T}=\mathrm{T}\left(\partial \sigma_{0}\right)
$$

and we maybe denote this $(n-1)$-chain by $\partial \mathrm{E}$.
An obvious question occurs here: if $\mathrm{E}=\mathrm{T}_{1}\left(\mathrm{Q}^{n}\right)=\mathrm{T}_{2}\left(\mathrm{Q}^{n}\right)$, and if both $\mathrm{T}_{1}$ and $T_{2}$ have positive Jacobians, is it true that $\partial T_{1}=\partial T_{2}$ ? That is to say, does the equality

$$
\int_{\partial T_{1}} \omega=\int_{\partial T_{2}} \omega
$$

hold for every $(n-1)$-form $\omega$ ? The answer is yes, but we shall omit the proof. (To see an example, compare the end of this section with Exercise 10.17.)

One can go further. Let

$$
\Omega=\mathrm{E}_{1} \cup \cdots \cup \mathrm{E}_{\mathrm{r}}
$$

where $E_{i}=T_{i}\left(Q^{n}\right)$, each $T_{i}$ has the properties that $T$ had above, and the interiors

of the sets $E_{i}$ are pairwise disjoint. Then the $(n-1)$-chain

$$
\partial T_{1}+\cdots+\partial T_{r}=\partial \Omega
$$

is called the positively oriented boundary of $\Omega$.
For example, the unit square $I^{2}$ in $\mathbb{R}^{2}$ is the union of $\sigma_{1}\left(Q^{2}\right)$ and $\sigma_{2}\left(Q^{2}\right)$, where

$$
\sigma_{1}(\mathbf{u})=\mathbf{u}, \quad \sigma_{2}(\mathbf{u})=\mathbf{e}_{1}+\mathbf{e}_{2}-\mathbf{u}
$$

Both $\sigma_{1}$ and $\sigma_{2}$ have Jacobian $1>0$. Since

$$
\sigma_{1}=\left[\mathbf{0}, \mathbf{e}_{1}, \mathbf{e}_{2}\right], \quad \sigma_{2}=\left[\mathbf{e}_{1}+\mathbf{e}_{2}, \mathbf{e}_{2}, \mathbf{e}_{1}\right]
$$

we have

$$
\begin{aligned}
& \partial \sigma_{1}=\left[\mathbf{e}_{1}, \mathbf{e}_{2}\right]-\left[\mathbf{0}, \mathbf{e}_{2}\right]+\left[\mathbf{0}, \mathbf{e}_{1}\right] \\
& \partial \sigma_{2}=\left[\mathbf{e}_{2}, \mathbf{e}_{1}\right]-\left[\mathbf{e}_{1}+\mathbf{e}_{2}, \mathbf{e}_{1}\right]+\left[\mathbf{e}_{1}+\mathbf{e}_{2}, \mathbf{e}_{2}\right]
\end{aligned}
$$

the sum of these two boundaries is

$$
\partial I^{2}=\left[0, \mathbf{e}_{1}\right]+\left[\mathbf{e}_{1}, \mathbf{e}_{1}+\mathbf{e}_{2}\right]+\left[\mathbf{e}_{1}+\mathbf{e}_{2}, \mathbf{e}_{2}\right]+\left[\mathbf{e}_{2}, 0\right]
$$

the positively oriented boundary of $I^{2}$. Note that $\left[\mathbf{e}_{1}, \mathbf{e}_{2}\right]$ canceled $\left[\mathbf{e}_{2}, \mathbf{e}_{1}\right]$.
If $\Phi$ is a 2 -surface in $\mathbb{R}^{m}$ with parameter domain $I^{2}$, then $\Phi$ (regarded as a function on 2 -forms) is the same as the 2 -chain

$$
\Phi \circ \sigma_{1}+\Phi \circ \sigma_{2}
$$

Thus

$$
\begin{aligned}
\partial \Phi & =\partial\left(\Phi \circ \sigma_{1}\right)+\partial\left(\Phi \circ \sigma_{2}\right) \\
& =\Phi\left(\partial \sigma_{1}\right)+\Phi\left(\partial \sigma_{2}\right)=\Phi\left(\partial I^{2}\right)
\end{aligned}
$$

In other words, if the parameter domain of $\Phi$ is the unit square $I^{2}$, we need not refer back to the simplex $Q^{2}$, but can obtain $\partial \Phi$ directly from $\partial I^{2}$.

Other examples may be found in Exercises 10.17 to 10.19 .
10.32 Example. For $0 \leq \mathrm{u} \leq \pi, 0 \leq v \leq 2 \pi$, define

$$
\Sigma(u, v)=(\sin u \cos v, \sin u \sin v, \cos u)
$$

Then $\Sigma$ is a 2 -surface in $\mathbb{R}^{3}$ whose parameter domain is a rectangle $D \subset \mathbb{R}^{2}$, and whose range is the unit square in $\mathbb{R}^{3}$. Its boundary is

$$
\partial \Sigma=\Sigma(\partial D)=\gamma_{1}+\gamma_{2}+\gamma_{3}+\gamma_{4}
$$

where

$$
\begin{aligned}
& \gamma_{1}(u)=\Sigma(u, 0)=(\sin u, 0, \cos u) \\
& \gamma_{2}(v)=\Sigma(\pi, v)=(0,0,-1) \\
& \gamma_{3}(u)=\Sigma(\pi-u, 2 \pi)=(\sin u, 0,-\cos u) \\
& \gamma_{4}(v)=\Sigma(0,2 \pi-v)=(0,0,1)
\end{aligned}
$$

with $[0, \pi]$ and $[0,2 \pi]$ as parameter intervals for $u$ and $v$, respectively.
Since $\gamma_{2}$ and $\gamma_{4}$ are constant, their derivatives are 0 , hence the integral of any 1-form over $\gamma_{2}$ or $\gamma_{4}$ is 0 . [See Example 10.12(a).] Since $\gamma_{3}(u)=\gamma_{1}(\pi-u)$, direct application of (10.35) shows that

$$
\int_{\gamma_{3}} \omega=-\int_{\gamma_{1}} \omega
$$

for every 1-form $\omega$. Thus $\int_{\partial \Sigma} \omega=0$ and we conclude that $\partial \Sigma=0$.
(In geographic terminology, $\partial \Sigma$ starts at the north pole N , runs to the south pole $S$ along a meridian, pauses at $S$, returns to $N$ along the same meridian, and finally pauses at N . The two passages along the meridian are in opposite directions. The corresponding two line integrals therefore cancel each other. In Exercise 10.32 there is also one curve which occurs twice in the boundary, but without cancellation.)

# STOKES' THEOREM 

10.33 Theorem. If $\Psi$ is a k-chain of class $\mathscr{C}^{2}$ in an open set $\mathrm{V} \subset \mathbb{R}^{m}$ and if $\omega$ is a (k-1)-form of class $\mathscr{C}^{1}$ in V , then

$$
\int_{\Psi} \mathrm{d} \omega=\int_{\partial \Psi} \omega
$$

The case $\mathrm{k}=\mathrm{m}=1$ is nothing but the fundamental theorem of calculus (with an additional differentiability assumption). The case $\mathrm{k}=\mathrm{m}=2$ is Green's theorem, and $\mathrm{k}=\mathrm{m}=3$ gives the so-called "divergence theorem" of Gauss. The case $\mathrm{k}=2, \mathrm{~m}=3$ is the one originally discovered by Stokes. (Spivak's book [Spi65] describes some of the historical background.) These special cases will be discussed further at the end of the present chapter.

Proof. It is enough to prove that

$$
\int_{\Phi} \mathrm{d} \omega=\int_{\partial \Phi} \omega
$$

for every oriented k -simplex $\Phi$ of class $\mathscr{C}^{2}$ in V . For if (10.92) is proved and if $\Psi=\Sigma \Phi_{i}$, then (10.87) and (10.89) imply (10.91).

Fix such a $\Phi$ and put

$$
\sigma=\left[0, \mathbf{e}_{1}, \ldots, \mathbf{e}_{\mathrm{k}}\right]
$$

Thus $\sigma$ is the oriented affine k -simplex with parameter domain $Q^{\mathrm{k}}$ which is defined by the identity mapping. Since $\Phi$ is also defined on $Q^{\mathrm{k}}$ (see Sec. 10.30) and $\Phi \in \mathscr{C}^{2}$, there is an open set $E \subset \mathbb{R}^{k}$ which contains $Q^{k}$ and there is a $\mathscr{C}^{2}$-mapping T of E into V such that $\Phi=\mathrm{T} \circ \sigma$. By Theorems 10.25 and 10.22(c), the left side of (10.92) is equal to

$$
\int_{\mathrm{T} \sigma} \mathrm{~d} \omega=\int_{\sigma}(\mathrm{d} \omega)_{\mathrm{T}}=\int_{\sigma} \mathrm{d}\left(\omega_{\mathrm{T}}\right)
$$

Another application of Theorem 10.25 shows, by (10.89), that the right side of (10.92) is

$$
\int_{\partial(\mathrm{T} \sigma)} \omega=\int_{\mathrm{T}(\partial \sigma)} \omega=\int_{\partial \sigma} \omega_{\mathrm{T}}
$$

Since $\omega_{\mathrm{T}}$ is a $(\mathrm{k}-1)$-form in E , we see that in order to prove (10.92) we merely have to show that

$$
\int_{\sigma} \mathrm{d} \lambda=\int_{\partial \sigma} \lambda
$$

for the special simplex (10.93) and for every $(\mathrm{k}-1)$-form $\lambda$ of class $\mathscr{C}^{1}$ in E .
If $\mathrm{k}=1$, the definition of an oriented 0 -simplex shows that (10.94) merely asserts that

$$
\int_{0}^{1} f^{\prime}(u) d u=f(1)-f(0)
$$

for every continuously differentiable function $f$ on $[0,1]$, which is true by the fundamental theorem of calculus (Theorem 6.21).

From now on we assume that $\mathrm{k}>1$. Fix an integer $\mathrm{r}(1 \leq \mathrm{r} \leq \mathrm{k})$ and choose $\mathrm{f} \in \mathscr{C}^{1}(\mathrm{E})$. It is then enough to prove (10.94) for the case

$$
\lambda=\mathrm{f}(\mathrm{x}) \mathrm{dx}_{1} \wedge \cdots \wedge \mathrm{dx}_{\mathrm{r}-1} \wedge \mathrm{dx}_{\mathrm{r}+1} \wedge \cdots \wedge \mathrm{dx}_{\mathrm{k}}
$$

since every $(\mathrm{k}-1)$-form is a sum of these special ones, for $\mathrm{r}=1, \ldots, \mathrm{k}$.
By (10.85), the boundary of the simplex (10.93) is

$$
\partial \sigma=\left[\mathbf{e}_{1}, \ldots, \mathbf{e}_{\mathrm{k}}\right]+\sum_{\mathrm{i}=1}^{\mathrm{k}}(-1)^{\mathrm{i}} \tau_{\mathrm{i}}
$$

where

$$
\tau_{i}=\left[0, \mathbf{e}_{1}, \ldots, \mathbf{e}_{i-1}, \mathbf{e}_{i+1}, \ldots, \mathbf{e}_{k}\right]
$$

for $i=1, \ldots, k$. Put

$$
\tau_{0}=\left[\mathbf{e}_{r}, \mathbf{e}_{1}, \ldots, \mathbf{e}_{r-1}, \mathbf{e}_{r+1}, \ldots \mathbf{e}_{k}\right]
$$

Note that $\tau_{0}$ is obtained from $\left[\mathbf{e}_{1}, \ldots, \mathbf{e}_{k}\right]$ by $r-1$ successive interchanges of $\mathbf{e}_{r}$ and its left neighbors. Thus

$$
\partial \sigma=(-1)^{r-1} \tau_{0}+\sum_{i=1}^{k}(-1)^{i} \tau_{i}
$$

Each $\tau_{i}$ has $Q^{k-1}$ as its parameter domain.
If $\mathbf{x}=\tau_{0}(\mathbf{u})$ and $\mathbf{u} \in Q^{k-1}$, then

$$
x_{j}= \begin{cases}u_{j} & (1 \leq j<r) \\ 1-\left(u_{1}+\cdots+u_{k-1}\right) & (j=r) \\ u_{j-1} & (r<j \leq k)\end{cases}
$$

If $1 \leq \mathrm{i} \leq \mathrm{k}, \mathbf{u} \in \mathrm{Q}^{\mathrm{k}-1}$, and $\mathrm{x}=\tau_{\mathrm{i}}(\mathbf{u})$, then

$$
x_{j}= \begin{cases}u_{j} & (1 \leq j<i) \\ 0 & (j=i) \\ u_{j-1} & (i<j \leq k)\end{cases}
$$

For $0 \leq \mathrm{i} \leq \mathrm{k}$, let $\mathrm{J}_{\mathrm{i}}$ be the Jacobian of the mapping

$$
\left(u_{1}, \ldots, u_{k-1}\right) \mapsto\left(x_{1}, \ldots, x_{r-1}, x_{r+1}, \ldots, x_{k}\right)
$$

induced by $\tau_{i}$. When $i=0$ and when $i=r,(10.98)$ and (10.99) show that (10.100) is the identity mapping. Thus $\mathrm{J}_{0}=1, \mathrm{~J}_{\mathrm{r}}=1$. For the other i , the fact that $\mathrm{x}_{\mathrm{i}}=0$ in (10.99) shows that $\mathrm{J}_{\mathrm{i}}$ has a row of zeroes, hence $\mathrm{J}_{\mathrm{i}}=0$. Thus

$$
\int_{\tau_{i}} \lambda=0 \quad(i \neq 0, i \neq r)
$$

by (10.35) and (10.96). Consequently, (10.97) gives

$$
\begin{aligned}
\int_{\partial \sigma} \lambda & =(-1)^{r-1} \int_{\tau_{0}} \lambda+(-1)^{r} \int_{\tau_{r}} \lambda \\
& =(-1)^{r-1} \int_{Q^{k-1}}\left[f\left(\tau_{0}(\mathbf{u})\right)-f\left(\tau_{r}(\mathbf{u})\right) d \mathbf{u}\right.
\end{aligned}
$$

On the other hand,

$$
\begin{aligned}
\mathrm{d} \lambda & =\left(\mathrm{D}_{\mathrm{r}} \mathrm{f}\right)(\mathbf{x}) \mathrm{dx}_{\mathrm{r}} \wedge \mathrm{dx}_{1} \wedge \cdots \wedge \mathrm{dx}_{\mathrm{r}-1} \wedge \mathrm{dx}_{\mathrm{r}+1} \wedge \cdots \wedge \mathrm{dx}_{\mathrm{k}} \\
& =(-1)^{\mathrm{r}-1}\left(\mathrm{D}_{\mathrm{r}} \mathrm{f}\right)(\mathbf{x}) \mathrm{dx}_{1} \wedge \cdots \wedge \mathrm{dx}_{\mathrm{k}}
\end{aligned}
$$

so that

$$
\int_{\sigma} \mathrm{d} \lambda=(-1)^{\mathrm{r}-1} \int_{\mathrm{Q}^{\mathrm{k}}}\left(\mathrm{D}_{\mathrm{r}} \mathrm{f}\right)(\mathbf{x}) \mathrm{d} \mathbf{x}
$$

To evaluate (10.103), first integrate with respect to $x_{r}$ over the interval

$$
\left[0,1-\left(x_{1}+\cdots+x_{r-1}+x_{r+1}+\cdots+x_{k}\right)\right]
$$

put $\left(x_{1}, \ldots, x_{r-1}, x_{r+1}, \ldots, x_{k}\right)=\left(u_{1}, \ldots, u_{k-1}\right)$, and see with the aid of (10.98) that the integral over $Q^{k}$ in (10.103) is equal to the integral over $Q^{k-1}$ in (10.102). Thus (10.94) holds, and the proof is complete.

# CLOSED FORMS AND EXACT FORMS 

10.34 Definition. Let $\omega$ be a k -form in an open set $\mathrm{E} \subset \mathbb{R}^{n}$. If there is a $(\mathrm{k}-1)$ form $\lambda$ in E such that $\omega=\mathrm{d} \lambda$, then $\omega$ is said to be exact in E . If $\omega$ is of class $\mathscr{C}^{1}$ and $\mathrm{d} \omega=0$, then $\omega$ is said to be closed.

Theorem 10.20(b) shows that every exact form of class $\mathscr{C}^{1}$ is closed. In certain sets E , for example in convex ones, the converse is true; this is the content of Theorem 10.39 (usually known as Poincare's lemma) and Theorem 10.40. However, Examples 10.36 and 10.37 will exhibit closed forms that are not exact.

### 10.35 Remarks.

(a) Whether a given k -form $\omega$ is or is not closed can be verified by simply differentiating the coefficients in the standard presentation of $\omega$. For example, a 1-form

$$
\omega=\sum_{i=1}^{n} f_{i}(\mathbf{x}) d x_{i}
$$

with $f_{i} \in \mathscr{C}^{1}(E)$ for some open set $E \subset \mathbb{R}^{n}$, is closed if and only if the equations

$$
\left(\mathrm{D}_{\mathrm{j}} \mathrm{f}_{\mathrm{i}}\right)(\mathbf{x})=\left(\mathrm{D}_{\mathrm{i}} \mathrm{f}_{\mathrm{j}}\right)(\mathbf{x})
$$

hold for all $i, j$ in $\{1, \ldots, n\}$ and for all $x \in E$. Note that (10.105) is a "pointwise" condition; it does not involve any global properties that depend on the shape of $E$.

On the other hand, to show that $\omega$ is exact in $E$, one has to prove the existence of a form $\lambda$, defined in $E$, such that $d \lambda=\omega$. This amounts to solving a system of partial differential equations, not just locally, but in all of E. For example, to show that (10.104) is exact in a set E, one has to find a function (or 0 -form) $g \in \mathscr{C}^{1}(E)$ such that

$$
\left(D_{i} g\right)(x)=f_{i}(x) \quad(x \in E, 1 \leq i \leq n)
$$

Of course, (10.105) is a necessary condition for the solvability of (10.106).
(b) Let $\omega$ be an exact k -form in E . Then there is a ( $\mathrm{k}-1$ )-form $\lambda$ in E with $\mathrm{d} \lambda=\omega$, and Stokes' theorem asserts that

$$
\int_{\Psi} \omega=\int_{\Psi} \mathrm{d} \lambda=\int_{\partial \Psi} \lambda
$$

for every k -chain $\Psi$ of class $\mathscr{C}^{2}$ in E .
If $\Psi_{1}$ and $\Psi_{2}$ are such chains, and if they have the same boundaries, it follows that

$$
\int_{\Psi_{1}} \omega=\int_{\Psi_{2}} \omega
$$

In particular, the integral of an exact k -form in E is 0 over every k -chain whose boundary is 0 . As an important special case of this, note that integrals of exact 1 -forms in E are 0 over closed (differentiable) curves in E.
(c) Let $\omega$ be a closed k -form in E . Then $\mathrm{d} \omega=0$, and Stokes' theorem asserts that

$$
\int_{\partial \Psi} \omega=\int_{\Psi} \mathrm{d} \omega=0
$$

for every $(\mathrm{k}+1)$-chain $\Psi$ of class $\mathscr{C}^{2}$ in E . In other words, integrals of closed k -forms in E are 0 over k -chains that are boundaries of $(\mathrm{k}+1)$-chains in E .
(d) Let $\Psi$ be a $(\mathrm{k}+1)$-chain in E and let $\lambda$ be a $(\mathrm{k}-1)$-form in E , both of class $\mathscr{C}^{2}$. Since $\mathrm{d}^{2} \lambda=0$, two applications of Stokes' theorem show that

$$
\int_{\partial \partial \Psi} \lambda=\int_{\partial \Psi} \mathrm{d} \lambda=\int_{\Psi} \mathrm{d}^{2} \lambda=0
$$

We conclude that $\partial^{2} \Psi=0$. In other words, the boundary of a boundary is 0 . See Exercise 10.16 for a more direct proof of this.
10.36 Example. Let $\mathrm{E}=\mathbb{R}^{2}-\{0\}$, the plane with the origin removed. The 1-form

$$
\eta=\frac{x d y-y d x}{x^{2}+y^{2}}
$$

is closed in $\mathbb{R}^{2}-\{0\}$. This is easily verified by differentiation. Fix $r>0$ and define

$$
\gamma(t)=(r \cos t, r \sin t) \quad(0 \leq t \leq 2 \pi)
$$

Then $\gamma$ is a curve (an "oriented 1-simplex") in $\mathbb{R}^{2}-\{0\}$. Since $\gamma(0)=\gamma(2 \pi)$, we have

$$
\partial \gamma=0
$$

Direct computation shows that

$$
\int_{\gamma} \eta=2 \pi \neq 0
$$

The discussion in Remark 10.35(b) and (c) shows that we can draw two conclusions from (10.113):

- First, $\eta$ is not exact in $\mathbb{R}^{2}-\{0\}$, for otherwise (10.112) would force the integral (10.113) to be 0 .
- Second, $\gamma$ is not the boundary of any 2-chain $\mathbb{R}^{2}-\{0\}$ (of class $\mathscr{C}^{2}$ ), for otherwise the fact that $\eta$ is closed would force the integral (10.113) to be 0 .
10.37 Example. Let $\mathrm{E}=\mathbb{R}^{3}-\{0\}$, 3 -space with the origin removed. Define

$$
\zeta=\frac{x d y \wedge d z+y d z \wedge d x+z d x \wedge d y}{\left(x^{2}+y^{2}+z^{2}\right)^{3 / 2}}
$$

where we have written $(x, y, z)$ in place of $\left(x_{1}, x_{2}, x_{3}\right)$. Differentiation shows that $d \zeta=0$, so that $\zeta$ is a closed 2 -form in $\mathbb{R}^{3}-\{0\}$.

Let $\Sigma$ be the 2 -chain $\mathbb{R}^{3}-\{0\}$ that was constructed in Example 10.32; recall that $\Sigma$ is a parametrization of the unit sphere in $\mathbb{R}^{3}$. Using the rectangle $D$ of Example 10.32 as a parameter domain, it is easy to compute that

$$
\int_{\Sigma} \zeta=\int_{D} \sin u d u d v=4 \pi \neq 0
$$

As in the preceding example, we can now conclude that $\zeta$ is not exact in $\mathbb{R}^{3}-\{0\}$ (since $\partial \Sigma=0$, as was shown in Example 10.32) and that the sphere $\Sigma$ is not the boundary of any 3-chain in $\mathbb{R}^{3}-\{0\}$ (of class $\mathscr{C}^{2}$ ), although $\partial \Sigma=0$.

The following result will be used in the proof of Theorem 10.39:
10.38 Theorem. Suppose E is a convex open set in $\mathbb{R}^{n}, \mathrm{f} \in \mathscr{C}^{1}(\mathrm{E}), \mathrm{p}$ is an integer, $1 \leq \mathrm{p} \leq \mathrm{n}$, and

$$
\left(D_{j} f\right)(x)=0 \quad(p<j \leq n, x \in E)
$$

Then there exists an $\mathrm{F} \in \mathscr{C}^{1}(\mathrm{E})$ such that

$$
\left(D_{p} F\right)(x)=f(x), \quad\left(D_{j} F\right)(x)=0 \quad(p<j \leq n, x \in E)
$$

Proof. Write $\mathbf{x}=\left(\mathbf{x}^{\prime}, \mathrm{x}_{\mathrm{p}}, \mathbf{x}^{\prime \prime}\right)$, where

$$
\mathbf{x}^{\prime}=\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{p}-1}\right), \quad \mathbf{x}^{\prime \prime}=\left(\mathrm{x}_{\mathrm{p}+1}, \ldots, \mathrm{x}_{\mathrm{n}}\right)
$$

(When $\mathrm{p}=1, \mathbf{x}^{\prime}$ is absent; when $\mathrm{p}=\mathrm{n}, \mathbf{x}^{\prime \prime}$ is absent.) Let V be the set of all $\left(\mathbf{x}^{\prime}, \mathrm{x}_{\mathrm{p}}\right) \in \mathbb{R}^{\mathrm{p}}$ such that $\left(\mathbf{x}^{\prime}, \mathrm{x}_{\mathrm{p}}, \mathbf{x}^{\prime \prime}\right) \in \mathrm{E}$ for some $\mathbf{x}^{\prime \prime}$. Being a projection of $\mathrm{E}, \mathrm{V}$ is a convex open set in $\mathbb{R}^{\mathrm{p}}$. Since E is convex and (10.116) holds, $\mathrm{f}(\mathbf{x})$ does not depend

on $\mathbf{x}^{\prime \prime}$. Hence there is a function $\varphi$, with domain $V$, such that

$$
f(x)=\varphi\left(x^{\prime}, x_{p}\right)
$$

for all $\mathbf{x} \in \mathrm{E}$.
If $\mathrm{p}=1, \mathrm{~V}$ is a segment in $\mathbb{R}^{1}$ (possibly unbounded). Pick $\mathrm{c} \in \mathrm{V}$ and define

$$
F(x)=\int_{c}^{x_{1}} \varphi(t) d t \quad(x \in E)
$$

If $\mathrm{p}>1$, let U be the set of all $\mathbf{x}^{\prime} \in \mathbb{R}^{\mathrm{p}-1}$ such that $\left(\mathbf{x}^{\prime}, \mathrm{x}_{\mathrm{p}}\right) \in \mathrm{V}$ for some $\mathrm{x}_{\mathrm{p}}$. Then $U$ is a convex open set in $\mathbb{R}^{p-1}$ and there is a function $\alpha \in \mathscr{C}^{1}(U)$ such that $\left(\mathbf{x}^{\prime}, \alpha\left(\mathbf{x}^{\prime}\right)\right) \in V$ for every $\mathbf{x}^{\prime} \in \mathrm{U}$; in other words, the graph of $\alpha$ lies in V (Exercise 10.29). Define

$$
F(x)=\int_{\alpha\left(x^{\prime}\right)}^{\mathrm{x}_{\mathrm{p}}} \varphi\left(\mathbf{x}^{\prime}, \mathrm{t}\right) \mathrm{dt} \quad(\mathbf{x} \in \mathrm{E})
$$

In either case, F satisfies (10.117).
10.39 Theorem. If $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ is convex and open, if $\mathrm{k} \geq 1$, if $\omega$ is a k -form of class $\mathscr{C}^{1}$ in E , and if $\partial \omega=0$, then there is a $(\mathrm{k}-1)$-form $\lambda$ in E such that $\omega=\mathrm{d} \lambda$.

Briefly, closed forms are exact in convex sets.
Proof. For $\mathrm{p}=1, \ldots, \mathrm{n}$, let $\mathrm{Y}_{\mathrm{p}}$ denote the set of all k -forms $\omega$ of class $\mathscr{C}^{1}$ in E whose standard presentation

$$
\omega=\sum_{I} f_{I}(\mathbf{x}) d x_{I}
$$

does not involve $d x_{p+1}, \ldots, d x_{n}$. In other words, if $I=\left(i_{1}, \ldots, i_{k}\right)$, then $\left\{i_{1}, \ldots, i_{k}\right\} \subset\{1, \ldots, p\}$ if $f_{I}(\mathbf{x}) \neq 0$ for some $\mathbf{x} \in \mathrm{E}$. We shall proceed by induction on p .

Assume first that $\omega \in Y_{1}$. Then $\omega=f(x) d x_{1}$. Since $d \omega=0,\left(D_{j} f\right)(x)=0$ for $1<j \leq n, x \in E$. By Theorem 10.38 there is an $F \in \mathscr{C}^{1}(E)$ such that $D_{1} F=f$ and $D_{j} F=0$ for $1<j \leq n$. Thus

$$
d F=\left(D_{1} F\right)(x) d x_{1}=f(x) d x_{1}=\omega
$$

Now we take $\mathrm{p}>1$ and make the following induction hypothesis: Every closed k -form that belongs to $\mathrm{Y}_{\mathrm{p}-1}$ is exact in E .

Choose $\omega \in \mathrm{Y}_{\mathrm{p}}$ so that $\mathrm{d} \omega=0$. By (10.118),

$$
\sum_{I} \sum_{j=1}^{n}\left(D_{j} f_{I}\right)(x) d x_{j} \wedge d x_{I}=d \omega=0
$$

Consider a fixed $j$ with $p<j \leq n$. Each $I$ that occurs in (10.118) lies in $\{1, \ldots, p\}$. If $I_{1}, I_{2}$ are two of these k -indices, and if $I_{1} \neq I_{2}$, then the $(k+1)$-indices $\left(I_{1}, j\right),\left(I_{2}, j\right)$

are distinct. Thus there is no cancellation, and we conclude that (10.119) that every coefficient in (10.118) satisfies

$$
\left(D_{j} f_{I}\right)(x)=0 \quad(x \in E, p<j \leq n)
$$

We now gather those terms in (10.118) that contain $d x_{p}$ and rewrite $\omega$ in the form

$$
\omega=\alpha+\sum_{I_{0}} f_{I}(x) d x_{I_{0}} \wedge d x_{p}
$$

where $\alpha \in Y_{p-1}$, each $I_{0}$ is an increasing $(k-1)$-index in $\{1, \ldots, p-1\}$, and $I=$ $\left(I_{0}, p\right)$. By (10.120), Theorem 10.38 furnishes functions $F_{I} \in \mathscr{C}^{1}(E)$ such that

$$
D_{p} F_{I}=f_{I}, \quad D_{j} F_{I}=0 \quad(p<j \leq n)
$$

Put

$$
\beta=\sum_{I_{0}} F_{I}(x) d x_{I_{0}}
$$

and define $\gamma=\omega-(-1)^{k-1} \mathrm{~d} \beta$. Since $\beta$ is a $(k-1)$-form, it follows that

$$
\begin{aligned}
\gamma & =\omega-\sum_{I_{0}} \sum_{j=1}^{p}\left(D_{j} F_{I}\right)(x) d x_{I_{0}} \wedge d x_{j} \\
& =\alpha-\sum_{I_{0}} \sum_{j=1}^{p-1}\left(D_{j} F_{I}\right)(x) d x_{I_{0}} \wedge d x_{j}
\end{aligned}
$$

which is clearly in $Y_{p-1}$. Since $d \omega=0$ and $d^{2} \beta=0$, we have $d \gamma=0$. Our induction hypothesis shows therefore that $\gamma=\mathrm{d} \mu$ for some $(k-1)$-form $\mu$ in $E$. If $\lambda=\mu+(-1)^{k-1} \beta$, we conclude that $\omega=\mathrm{d} \lambda$. By induction, this completes the proof.
10.40 Theorem. Fix $\mathrm{k}, 1 \leq \mathrm{k} \leq \mathrm{n}$. Let $\mathrm{E} \subset \mathbb{R}^{\mathrm{n}}$ be an open set in which every closed k -form is exact. Let T be a 1-1 $\mathscr{C}^{2}$-mapping of E onto an open set $\mathrm{U} \subset \mathbb{R}^{\mathrm{n}}$ whose inverse S is also of class $\mathscr{C}^{2}$. Then every closed k -form in U is exact in U .

Note that every convex open set $E$ satisfies the present hypothesis by Theorem 10.39. The relation between $E$ and $U$ may be expressed by saying that they are $\mathscr{C}^{2}$-equivalent.

Thus every closed form is exact in any set which is $\mathscr{C}^{2}$ equivalent to a convex open set.
Proof. Let $\omega$ be a k -form in U with $\mathrm{d} \omega=0$. By Theorem $10.22(\mathrm{c}), \omega_{\mathrm{T}}$ is a k -form in $E$ for which $d\left(\omega_{T}\right)=0$. Hence $\omega_{T}=d \lambda$ for some $(k-1)$-form $\lambda$ in $E$. By

Theorem 10.23, and another application of Theorem 10.22(c),

$$
\omega=\left(\omega_{\mathrm{T}}\right)_{\mathrm{S}}=(\mathrm{d} \lambda)_{\mathrm{S}}=\mathrm{d}\left(\lambda_{\mathrm{S}}\right)
$$

Since $\lambda_{\mathrm{S}}$ is a $(\mathrm{k}-1)$-form in $\mathrm{U}, \omega$ is exact in U .
10.41 Remark. In applications, cells (see Definition 2.17) are often more convenient parameter domains than simplexes. If our whole development had been based on cells rather than simplexes, the computation that occurs in the proof of Stokes' theorem would be even simpler. (It is done that way in Spivak's book [Spi65].) The reason for preferring simplexes is that the definition of the boundary of an oriented simplex seems easier and more natural than is the case for a cell. (See Exercise 10.19.) Also, the partitioning of sets into simplexes (called "triangulation") plays an important role in topology and there are strong connections between certain aspects of topology, on the one hand, and differential forms, on the other. These are hinted at in Remark 10.35. The book by Singer and Thorpe [ST67] contains a good introduction to this topic.

Since every cell can be triangulated, we may regard it as a chain. For dimension 2, this was done in Example 10.32; for dimension 3, see Exercise 10.18.

Poincare's lemma (Theorem 10.39) can be proved in several ways. See, for example, page 94 in Spivak's book [Spi65], or page 280 in Fleming's [Fle65]. Two simple proofs for certain special cases are indicated in Exercise 10.24 and Exercise 10.27 .

# VECTOR ANALYSIS 

We conclude this chapter with a few applications of the preceding material to theorems concerning vector analysis in $\mathbb{R}^{3}$. These are special cases of theorems about differential forms, but are usually stated in different terminology. We are thus faced with the job of translating from one language to another.
10.42 Vector Fields. Let $\mathbf{F}=F_{1} \mathbf{e}_{1}+F_{2} \mathbf{e}_{2}+F_{3} \mathbf{e}_{3}$ be a continuous mapping of an open set $E \subset \mathbb{R}^{3}$ into $\mathbb{R}^{3}$. Since $\mathbf{F}$ associates a vector to each point of $E, \mathbf{F}$ is sometimes called a vector field, especially in physics. With every such $\mathbf{F}$ is associated a 1 -form

$$
\lambda_{\mathbf{F}}=F_{1} d x+F_{2} d y+F_{3} d z
$$

and a 2-form

$$
\omega_{\mathbf{F}}=F_{1} d y \wedge d z+F_{2} d z \wedge d x+F_{3} d x \wedge d y
$$

Here, and in the rest of this chapter, we use the customary notation $(x, y, z)$ in place of $\left(x_{1}, x_{2}, x_{3}\right)$.

It is clear, conversely, that every 1-form in $E$ is $\lambda_{F}$ for some vector field $F$ in $E$, and that every 2 -form $\omega$ is $\omega_{\mathbf{F}}$ for some $\mathbf{F}$. In $\mathbb{R}^{3}$, the study of 1-forms and 2-forms is thus coextensive with the study of vector fields.

If $u \in \mathscr{C}^{1}(E)$ is a real function, then its gradient

$$
\nabla u=\left(D_{1} u\right) e_{1}+\left(D_{2} u\right) e_{2}+\left(D_{3} u\right) e_{3}
$$

is an example of a vector field in E.
Suppose now that $\mathbf{F}$ is a vector field in E , of class $\mathscr{C}^{1}$. Its curl $\nabla \times \mathbf{F}$ is the vector field defined in $E$ by

$$
\nabla \times \mathbf{F}=\left(\mathrm{D}_{2} \mathrm{~F}_{3}-\mathrm{D}_{3} \mathrm{~F}_{2}\right) \mathbf{e}_{1}+\left(\mathrm{D}_{3} \mathrm{~F}_{1}-\mathrm{D}_{1} \mathrm{~F}_{3}\right) \mathbf{e}_{2}+\left(\mathrm{D}_{1} \mathrm{~F}_{2}-\mathrm{D}_{2} \mathrm{~F}_{1}\right) \mathbf{e}_{3}
$$

and its divergence is the real function $\nabla \cdot \mathbf{F}$ defined in $E$ by

$$
\nabla \cdot \mathbf{F}=\mathrm{D}_{1} \mathrm{~F}_{1}+\mathrm{D}_{2} \mathrm{~F}_{2}+\mathrm{D}_{3} \mathrm{~F}_{3}
$$

These quantities have various physical interpretations. We refer to the book by O.D. Kellogg [Kel40] for more details.

Here are some relations between gradients, curls, and divergences.
10.43 Theorem. Suppose E is an open set in $\mathbb{R}^{3}, u \in \mathscr{C}^{2}(\mathrm{E})$, and G is a vector field in E of class $\mathscr{C}^{2}$.
(a) If $\mathbf{F}=\nabla u$, then $\nabla \times \mathbf{F}=\mathbf{0}$.
(b) If $\mathbf{F}=\nabla \times \mathbf{G}$, then $\nabla \cdot \mathbf{F}=0$.

Furthermore, if E is $\mathscr{C}^{2}$-equivalent to a convex set, then (a) and (b) have converses, in which we assume that $\mathbf{F}$ is a vector field in E of class $\mathscr{C}^{1}$ :
(a') If $\nabla \times \mathbf{F}=0$, then $\mathbf{F}=\nabla u$ for some $u \in \mathscr{C}^{2}(E)$.
(b') If $\nabla \cdot \mathbf{F}=0$, then $\mathbf{F}=\nabla \times \mathbf{G}$ for some vector field $\mathbf{G}$ in E of class $\mathscr{C}^{n}$.
Proof. If we compare the definitions of $\nabla u, \nabla \times \mathbf{F}$, and $\nabla \cdot \mathbf{F}$ with the differential forms $\lambda_{\mathbf{F}}$ and $\omega_{\mathbf{F}}$ given by (10.124) and (10.125), we obtain the following four statements:

$$
\begin{array}{rlrl}
\mathbf{F} & =\nabla u & \text { if and only if } & \lambda_{\mathbf{F}}=\mathrm{du} \\
\nabla \times \mathbf{F} & =\mathbf{0} & \text { if and only if } & \mathrm{d} \lambda_{\mathbf{F}}=0 \\
\mathbf{F} & =\nabla \times \mathbf{G} & \text { if and only if } & \omega_{\mathbf{F}}=\mathrm{d} \lambda_{\mathbf{G}} \\
\nabla \cdot \mathbf{F} & =0 & \text { if and only if } & \mathrm{d} \omega_{\mathbf{F}}=0
\end{array}
$$

Now if $\mathbf{F}=\nabla u$, then $\lambda_{\mathbf{F}}=\mathrm{du}$, hence $\mathrm{d} \lambda_{\mathbf{F}}=\mathrm{d}^{2} \mathrm{u}=0$ (Theorem 10.20), which means that $\nabla \times \mathbf{F}=0$. Thus (a) is proved. As regards ( $\mathrm{a}^{\prime}$ ), the hypothesis amounts to saying that $\mathrm{d} \lambda_{\mathbf{F}}=0$ in E . By Theorem $10.40, \lambda_{\mathbf{F}}=\mathrm{du}$ for some 0 -form u . Hence $\mathbf{F}=\nabla u$.

The proofs of (b) and ( $\mathrm{b}^{\prime}$ ) follow exactly the same pattern.
10.44 Volume Elements. The k-form

$$
d x_{1} \wedge \cdots \wedge d x_{k}
$$

is called the volume element in $\mathbb{R}^{\mathrm{k}}$. It is often denoted by dV (or by $\mathrm{dV}_{\mathrm{k}}$ if it seems desirable to indicated the dimension explicitly), and the notation

$$
\int_{\Phi} f(x) d x_{1} \wedge \cdots \wedge d x_{k}=\int_{\Phi} f d V
$$

is used when $\Phi$ is a positively oriented k -surface in $\mathbb{R}^{\mathrm{k}}$ and f is a continuous function on the range of $\Phi$.

The reason for using this terminology is very simple: If D is a parameter domain in $\mathbb{R}^{\mathrm{k}}$ and if $\Phi$ is a $1-1 \mathscr{C}^{1}$-mapping of D into $\mathbb{R}^{\mathrm{k}}$ with positive Jacobian $\mathrm{J}_{\Phi}$, then the left side of $(10.126)$ is

$$
\int_{D} f(\Phi(\mathbf{u})) J_{\Phi}(\mathbf{u}) d \mathbf{u}=\int_{\Phi(D)} f(\mathbf{x}) d \mathbf{x}
$$

by (10.35) and Theorem 10.9 .
In particular, when $\mathrm{f}=1,(10.126)$ defines the volume of $\Phi$. We already saw a special case of this in (10.36).

The usual notation for $\mathrm{dV}_{2}$ is dA .
10.45 Theorem (Green's Theorem). Suppose E is an open set in $\mathbb{R}^{2}, \alpha \in \mathscr{C}^{1}(\mathrm{E})$, $\beta \in \mathscr{C}^{1}(\mathrm{E})$, and $\Omega$ is a closed subset of E with positively oriented boundary $\mathrm{d} \Omega$, as described in Sec. 10.31. Then

$$
\int_{\mathrm{d} \Omega}(\alpha \mathrm{dx}+\beta \mathrm{dy})=\int_{\Omega}\left(\frac{\partial \beta}{\partial \mathrm{x}}-\frac{\partial \alpha}{\partial \mathrm{y}}\right) \mathrm{dA}
$$

Proof. Put $\lambda=\alpha \mathrm{dx}+\beta \mathrm{dy}$. Then

$$
\begin{aligned}
\mathrm{d} \lambda & =\left(\mathrm{D}_{2} \alpha\right) \mathrm{dy} \wedge \mathrm{dx}+\left(\mathrm{D}_{1} \beta\right) \mathrm{dx} \wedge \mathrm{dy} \\
& =\left(\mathrm{D}_{1} \beta-\mathrm{D}_{2} \alpha\right) \mathrm{dA}
\end{aligned}
$$

and (10.127) is the same as

$$
\int_{\partial \Omega} \lambda=\int_{\Omega} \mathrm{d} \lambda
$$

which is true by Theorem 10.33 .
With $\alpha(x, y)=-y$ and $\beta(x, y)=x,(10.127)$ becomes

$$
\frac{1}{2} \int_{\partial \Omega}(x d y-y d x)=A(\Omega)
$$

the area of $\Omega$.
With $\alpha=0, \beta=x$, a similar formula is obtained. Example 10.12(b) contains a special case of this.
10.46 Area Elements in $\mathbb{R}^{3}$. Let $\Phi$ be a 2 -surface in $\mathbb{R}^{3}$ of class $\mathscr{C}^{1}$ and with parameter domain $\mathrm{D} \subset \mathbb{R}^{2}$. Associate with each point $(u, v) \in D$ the vector

$$
\mathbf{N}(u, v)=\frac{\partial(y, z)}{\partial(u, v)} \mathbf{e}_{1}+\frac{\partial(z, x)}{\partial(u, v)} \mathbf{e}_{2}+\frac{\partial(x, y)}{\partial(u, v)} \mathbf{e}_{3}
$$

The Jacobians in (10.129) correspond to the equation

$$
(x, y, z)=\Phi(u, v)
$$

If $f$ is a continuous function on $\Phi(D)$, the area integral of $f$ over $\Phi$ is defined to be

$$
\int_{\Phi} f d A=\int_{D} f(\Phi(u, v))|\mathbf{N}(u, v)| d u d v
$$

In particular, when $f=1$, we obtain the area of $\Phi$, namely

$$
A(\Phi)=\int_{D}|\mathbf{N}(u, v)| d u d v
$$

The following discussion will show that (10.131) and its special case (10.132) are reasonable definitions. It will also describe the geometric features of the vector N.

Write $\Phi=\varphi_{1} \mathbf{e}_{1}+\varphi_{2} \mathbf{e}_{2}+\varphi_{3} \mathbf{e}_{3}$, fix a point $\mathbf{p}_{0}=\left(u_{0}, v_{0}\right) \in D$, put $\mathbf{N}=\mathbf{N}\left(\mathbf{p}_{0}\right)$, put

$$
\alpha_{i}=\left(D_{1} \varphi_{i}\right)\left(\mathbf{p}_{0}\right), \quad \beta_{i}=\left(D_{2} \varphi_{i}\right)\left(\mathbf{p}_{0}\right) \quad(i=1,2,3)
$$

and let $T \in L\left(\mathbb{R}^{2}, \mathbb{R}^{3}\right)$ be the linear transformation given by

$$
T(u, v)=\sum_{i=1}^{3}\left(\alpha_{i} u+\beta_{i} v\right) e_{i}
$$

Note that $T=\Phi^{\prime}\left(\mathbf{p}_{0}\right)$, in accordance with Definition 9.11.
Let us now assume the rank of $T$ is 2 . (If it is 1 or 0 , then $N=0$, and the tangent plane mentioned below degenerates to a line or to a point.) The range of the affine mapping

$$
(u, v) \mapsto \Phi\left(\mathbf{p}_{0}\right)+T(u, v)
$$

is then a plane $\Pi$ called the tangent plane to $\Phi$ at $\mathbf{p}_{0}$. [One would like to call $\Pi$ the tangent plane at $\Phi\left(\mathbf{p}_{0}\right)$, rather then at $\mathbf{p}_{0}$; if $\Phi$ is not one-to-one, this runs into difficulties.]

If we use (10.133) in (10.129), we obtain

$$
\mathbf{N}=\left(\alpha_{2} \beta_{3}-\alpha_{3} \beta_{2}\right) \mathbf{e}_{1}+\left(\alpha_{3} \beta_{1}-\alpha_{1} \beta_{3}\right) \mathbf{e}_{2}+\left(\alpha_{1} \beta_{2}-\alpha_{2} \beta_{1}\right) \mathbf{e}_{3}
$$

and (10.134) shows that

$$
\mathrm{Te}_{1}=\sum_{\mathrm{i}=1}^{3} \alpha_{\mathrm{i}} \mathbf{e}_{\mathrm{i}}, \quad \mathrm{Te}_{2}=\sum_{\mathrm{i}=1}^{3} \beta_{\mathrm{i}} \mathbf{e}_{\mathrm{i}}
$$

A straightforward computation now leads to

$$
\mathbf{N} \cdot\left(\mathrm{Te}_{1}\right)=0=\mathbf{N} \cdot\left(\mathrm{Te}_{2}\right)
$$

Hence $\mathbf{N}$ is perpendicular to $\Pi$. It is therefore called the normal to $\Phi$ at $\mathbf{p}_{0}$.
A second property of $\mathbf{N}$, also verified by a direct computation based on (10.135) and (10.136), is that the determinant of the linear transformation of $\mathbb{R}^{3}$ that takes $\left(\mathbf{e}_{1}, \mathbf{e}_{2}, \mathbf{e}_{3}\right)$ to $\left(\mathrm{Te}_{1}, \mathrm{Te}_{2}, \mathbf{N}\right)$ is $|\mathbf{N}|^{2}>0$ (Exercise 10.30). The 3-simplex

$$
\left[0, \mathrm{Te}_{1}, \mathrm{Te}_{2}, \mathbf{N}\right]
$$

is thus positively oriented.
The third property of $\mathbf{N}$ that we shall use is a consequence of the first two: The above-mentioned determinant, whose value is $|\mathbf{N}|^{2}$, is the volume of the parallelepiped with edges $\left[0, \mathrm{Te}_{1}\right],\left[0, \mathrm{Te}_{2}\right],|0, \mathbf{N}|$. By (10.137), $|\mathbf{0}, \mathbf{N}|$ is perpendicular to the other two edges. The area of the parallelogram with vertices

$$
\mathbf{0}, \mathrm{Te}_{1}, \mathrm{Te}_{2}, \mathrm{~T}\left(\mathbf{e}_{1}+\mathbf{e}_{2}\right)
$$

is therefore $|\mathbf{N}|$.
This parallelogram is the image under T of the unit square in $\mathbb{R}^{2}$. If E is any rectangle in $\mathrm{R}^{2}$, it follows (by the linearity of T ) that the area of the parallelogram $\mathrm{T}(\mathrm{E})$ is

$$
\mathrm{A}(\mathrm{~T}(\mathrm{E}))=|\mathbf{N}| \mathrm{A}(\mathrm{E})=\int_{\mathrm{E}}\left|\mathbf{N}\left(\mathrm{u}_{0}, v_{0}\right)\right| \mathrm{du} d v
$$

We conclude that (10.132) is correct when $\Phi$ is affine. To justify the definition (10.132) in the general case, divide D into small rectangles, pick a point $\left(u_{0}, v_{0}\right)$ in each, and replace $\Phi$ in each rectangle by the corresponding tangent plane. The sum of the areas of the resulting parallelograms, obtained via (10.140), is then an approximation to $\mathrm{A}(\Phi)$. Finally, one can justify (10.131) from (10.132) by approximating $f$ by step functions.
10.47 Example. Let $0<\mathrm{a}<\mathrm{b}$ be fixed. Let K be the 3 -cell determined by

$$
0 \leq \mathrm{t} \leq \mathrm{a}, \quad 0 \leq \mathrm{u} \leq 2 \pi, \quad 0 \leq v \leq 2 \pi
$$

The equations

$$
\begin{aligned}
& x=\mathrm{t} \cos \mathrm{u} \\
& y=(\mathrm{b}+\mathrm{t} \sin \mathrm{u}) \cos v \\
& z=(\mathrm{b}+\mathrm{t} \sin \mathrm{u}) \sin v
\end{aligned}
$$

describe a mapping $\Phi$ of $\mathbb{R}^{3}$ into $\mathbb{R}^{3}$ which is $1-1$ in the interior of $K$, such that $\Psi(K)$ is a solid torus. Its Jacobian is

$$
J_{\Psi}=\frac{\partial(x, y, z)}{\partial(t, u, v)}=t(b+t \sin u)
$$

which is positive on K , except on the face $\mathrm{t}=0$. If we integrate $\mathrm{J}_{\Psi}$ over K , we obtain

$$
\operatorname{vol}(\Psi(\mathrm{K}))=2 \pi^{2} \mathrm{a}^{2} \mathrm{~b}^{2}
$$

as the volume of our solid torus.
Now consider the 2-chain $\Phi=\partial \Psi$. (See Exercise 10.19.) $\Psi$ maps the faces $\mathrm{u}=0$ and $\mathrm{u}=2 \pi$ of K onto the same cylindrical strip, but with the opposite orientations. $\Psi$ maps the faces $v=0$ and $v=2 \pi$ onto the same circular disc, but with opposite orientations. $\Psi$ maps the face $\mathrm{t}=0$ onto a circle, which contributes 0 to the 2 -chain $\partial \Psi$. (The relevant Jacobians are 0 .) Thus $\Phi$ is simply the 2 -surface obtained by setting $\mathrm{t}=\mathrm{a}$ in (10.141), with parameter domain D the square defined by $0 \leq \mathrm{u} \leq 2 \pi, 0 \leq v \leq 2 \pi$.

According to (10.129) and (10.141), the normal to $\Phi$ at $(u, v) \in D$ is thus the vector

$$
\mathbf{N}(u, v)=a(b+a \sin u) \mathbf{n}(u, v)
$$

where

$$
\mathbf{n}(u, v)=(\cos u) \mathbf{e}_{1}+(\sin u \cos v) \mathbf{e}_{2}+(\sin u \sin v) \mathbf{e}_{3}
$$

Since $|\mathbf{n}(u, v)|=1$, we have $|\mathbf{N}(u, v)|=a(b+a \sin u)$, and if we integrate this over D, (10.131) gives

$$
A(\Phi)=4 \pi^{2} a b
$$

as the surface area of our torus.
If we think of $\mathbf{N}=\mathbf{N}(u, v)$ as a directed line segment pointing from $\Phi(u, v)$ to $\Phi(u, v)+\mathbf{N}(u, v)$, then $\mathbf{N}$ points outward, that is to say, away from $\Psi(K)$. This is so because $\mathrm{J}_{\Psi}>0$ when $\mathrm{t}=\mathrm{a}$.

For example, take $u=v=\pi / 2, \mathrm{t}=\mathrm{a}$. This gives the largest value of $z$ on $\Psi(K)$, and $\mathbf{N}=a(b+a) \mathbf{e}_{3}$ points "upward" for this choice of $(u, v)$.
10.48 Integrals of 1-forms in $\mathbb{R}^{3}$. Let $\gamma$ be a $\mathscr{C}^{1}$ curve in an open set $\mathrm{E} \subset \mathbb{R}^{3}$ with parameter interval $[0,1]$, let $\mathbf{F}$ be a vector field in E as in Sec. 10.42, and define $\lambda_{\mathbf{F}}$ by (10.124). For any $u \in[0,1]$,

$$
\gamma^{\prime}(u)=\gamma_{1}^{\prime}(u) \mathbf{e}_{1}+\gamma_{2}^{\prime}(u) \mathbf{e}_{2}+\gamma_{3}^{\prime}(u) \mathbf{e}_{3}
$$

is called the tangent vector to $\gamma$ at $u$. We define $\mathbf{t}=\mathbf{t}(u)$ to be the unit vector in the direction of $\gamma^{\prime}(u)$. Thus

$$
\gamma^{\prime}(u)=\left|\gamma^{\prime}(u)\right| \mathbf{t}(u)
$$

[If $\gamma^{\prime}(u)=0$ for some $u$, put $\mathbf{t}(u)=\mathbf{e}_{1}$; any other choice would do just as well.] By (10.35),

$$
\begin{aligned}
\int_{\gamma} \lambda_{\mathbf{F}} & =\sum_{\mathrm{i}=1}^{3} \int_{0}^{1} \mathrm{~F}_{\mathrm{i}}(\gamma(\mathrm{u})) \gamma_{\mathrm{i}}^{\prime}(\mathrm{u}) \mathrm{du} \\
& =\int_{0}^{1} \mathbf{F}(\gamma(\mathrm{u})) \cdot \gamma^{\prime}(\mathrm{u}) \mathrm{du} \\
& =\int_{0}^{1} \mathbf{F}(\gamma(\mathrm{u})) \cdot \mathbf{t}(\mathrm{u})\left|\gamma^{\prime}(\mathrm{u})\right| \mathrm{du}
\end{aligned}
$$

Theorem 6.27 makes it reasonable to call $\left|\gamma^{\prime}(u)\right|$ the element of arc length along $\gamma$. A customary notation for it is ds, and (10.142) is rewritten in the form

$$
\int_{\gamma} \lambda_{\mathbf{F}}=\int_{\gamma}(\mathbf{F} \cdot \mathbf{t}) \mathrm{ds}
$$

Since $\mathbf{t}$ is a unit tangent vector to $\gamma, \mathbf{F} \cdot \mathbf{t}$ is called the tangential component of $\mathbf{F}$ along $\gamma$.

The right side of (10.143) should be regarded as just an abbreviation for the last integral in (10.142). The point is that $\mathbf{F}$ is defined on the range of $\gamma$, but $\mathbf{t}$ is defined on $[0,1]$; thus $\mathbf{F} \cdot \mathbf{t}$ has to be properly interpreted. Of course, when $\gamma$ is one-to-one, then $\mathbf{t}(u)$ can be replaced by $\mathbf{t}(\gamma(u))$ and this difficulty disappears.
10.49 Integrals of 2-forms in $\mathbb{R}^{3}$. Let $\Phi$ be a 2-surface in an open set $\mathrm{E} \subset \mathbb{R}^{3}$, of class $\mathscr{C}^{1}$, and with parameter domain $\mathrm{D} \subset \mathbb{R}^{2}$. Let $\mathbf{F}$ be a vector field in E and define $\omega_{\mathbf{F}}$ by (10.125). As in the preceding section, we shall obtain a different representation of the integral of $\omega_{\mathbf{F}}$ over $\Phi$. By (10.35) and (10.129),

$$
\begin{aligned}
\int_{\Phi} \omega_{\mathbf{F}} & =\int_{\Phi}\left(\mathrm{F}_{1} \mathrm{~d} y \wedge \mathrm{~d} z+\mathrm{F}_{2} \mathrm{~d} z \wedge \mathrm{~d} x+\mathrm{F}_{3} \mathrm{~d} x \wedge \mathrm{~d} y\right) \\
& =\int_{\mathrm{D}}\left\{\left(\mathrm{~F}_{1} \circ \Phi\right) \frac{\partial(y, z)}{\partial(u, v)}+\left(\mathrm{F}_{2} \circ \Phi\right) \frac{\partial(z, x)}{\partial(u, v)}+\left(\mathrm{F}_{3} \circ \Phi\right) \frac{\partial(x, y)}{\partial(u, v)}\right\} \mathrm{du} d v \\
& =\int_{\mathrm{D}} \mathbf{F}(\Phi(u, v)) \cdot \mathbf{N}(u, v) \mathrm{du} d v
\end{aligned}
$$

Now let $\mathbf{n}=\mathbf{n}(u, v)$ be the unit vector in the direction of $\mathbf{N}(u, v)$. [If $\mathbf{N}(u, v)=\mathbf{0}$ for some $(u, v) \in D$, take $\mathbf{n}(u, v)=\mathbf{e}_{1}$.] Then $\mathbf{N}=|\mathbf{N}| \mathbf{n}$, and therefore the last integral becomes

$$
\int_{\mathrm{D}} \mathbf{F}(\Phi(u, v)) \cdot \mathbf{n}(u, v)|\mathbf{N}(u, v)| \mathrm{du} d v
$$

By (10.131), we can finally write this in the form

$$
\int_{\Phi} \omega_{\mathbf{F}}=\int_{\Phi}(\mathbf{F} \cdot \mathbf{n}) \mathrm{dA}
$$

With regard to the meaning of $\mathbf{F} \cdot \mathbf{n}$, the remark made at the end of Sec. 10.48 applies here as well.

We can now state the original form of Stokes' theorem.
10.50 Theorem (Stokes' Formula). If $\mathbf{F}$ is a vector field of class $\mathscr{C}^{1}$ in an open set $\mathrm{E} \subset \mathbb{R}^{3}$, and if $\Phi$ is a 2-surface of class $\mathscr{C}^{2}$ in E , then

$$
\int_{\Phi}(\nabla \times \mathbf{F}) \cdot \mathbf{n} \mathrm{dA}=\int_{\partial \Phi}(\mathbf{F} \cdot \mathbf{t}) \mathrm{ds}
$$

Proof. Put $\mathbf{H}=\nabla \times \mathbf{F}$. Then, as in the proof of Theorem 10.43, we have

$$
\omega_{\mathbf{H}}=\mathrm{d} \lambda_{\mathbf{F}}
$$

Hence

$$
\begin{aligned}
\int_{\Phi}(\nabla \times \mathbf{F}) \cdot \mathbf{n} \mathrm{dA} & =\int_{\Phi}(\mathbf{H} \cdot \mathbf{n}) \mathrm{dA}=\int_{\Phi} \omega_{\mathbf{H}} \\
& =\int_{\Phi} \mathrm{d} \lambda_{\mathbf{F}}=\int_{\partial \Phi} \lambda_{\mathbf{F}}=\int_{\partial \Phi}(\mathbf{F} \cdot \mathbf{t}) \mathrm{ds}
\end{aligned}
$$

Here we used the definition of $\mathbf{H}$, then (10.144) with $\mathbf{H}$ in place of $\mathbf{F}$, then (10.146), then-the main step—Theorem 10.33, and finally (10.143), extended in the obvious way from curves to 1 -chains.
10.51 Theorem (The Divergence Theorem). If $\mathbf{F}$ is a vector field of class $\mathscr{C}^{1}$ in an open set $\mathrm{E} \subset \mathbb{R}^{3}$, and if $\Omega$ is a closed subset of E with positively oriented boundary $\partial \Omega$ (as described in Sec. 10.31 then

$$
\int_{\Omega}(\nabla \cdot \mathbf{F}) \mathrm{dV}=\int_{\partial \Omega}(\mathbf{F} \cdot \mathbf{n}) \mathrm{dA}
$$

Proof. By (10.125),

$$
\mathrm{d} \omega_{\mathbf{F}}=(\nabla \cdot \mathbf{F}) \mathrm{dx} \wedge \mathrm{dy} \wedge \mathrm{~d} z=(\nabla \cdot \mathbf{F}) \mathrm{dV}
$$

Hence

$$
\int_{\Omega}(\nabla \cdot \mathbf{F}) \mathrm{dV}=\int_{\Omega} \mathrm{d} \omega_{\mathbf{F}}=\int_{\partial \Omega} \omega_{\mathbf{F}}=\int_{\partial \Omega}(\mathbf{F} \cdot \mathbf{n}) \mathrm{dA}
$$

by Theorem 10.33, applied to the 2-form $\omega_{\mathbf{F}}$ and (10.144).

# EXERCISES 

10.1. Let $H$ be a compact convex set in $\mathbb{R}^{k}$ with nonempty interior. Let $f \in \mathscr{C}(H)$, put $f(\mathbf{x})=0$ in the complement of $H$, and define $\int_{H} f$ as in Definition 10.3. Prove that $\int_{H} f$ is independent of the order in which the k integrations are carried out.

Hint: Approximate f by functions that are continuous on $\mathbb{R}^{k}$ and whose supports are in H, as was done in Example 10.4.
10.2. For $\mathfrak{i}=1,2,3, \ldots$, let $\varphi_{i} \in \mathscr{C}\left(\mathbb{R}^{1}\right)$ have support in $\left(2^{-\mathrm{i}}, 2^{1-\mathrm{i}}\right)$ and satisfy $\int \varphi_{i}=1$. Put

$$
f(x, y)=\sum_{i=1}^{\infty}\left\{\varphi_{i}(x)-\varphi_{i+1}(x)\right\} \varphi_{i}(y)
$$

Then $f$ has compact support in $\mathbb{R}^{2}, f$ is continuous except at $(0,0)$, and

$$
\int \mathrm{d} y \int \mathrm{f}(\mathrm{x}, \mathrm{y}) \mathrm{dx}=0 \quad \text { but } \quad \int \mathrm{dx} \int \mathrm{f}(\mathrm{x}, \mathrm{y}) \mathrm{dy}=1
$$

Observe that $f$ is unbounded in every neighborhood of $(0,0)$.
10.3.
(a) If $\mathbf{F}$ is as in Theorem 10.7, put $A=\mathbf{F}^{\prime}(\mathbf{0}), \mathbf{F}_{1}(\mathbf{x})=A^{-1} \mathbf{F}(\mathbf{x})$. Then $\mathbf{F}_{1}^{\prime}(\mathbf{0})=\mathrm{I}$. Show that

$$
\mathbf{F}_{1}(\mathbf{x})=\mathbf{G}_{n} \circ \mathbf{G}_{n-1} \circ \cdots \circ \mathbf{G}_{1}(\mathbf{x})
$$

in some neighborhood of $\mathbf{0}$, for certain primitive mappings $\mathbf{G}_{1}, \ldots, \mathbf{G}_{n}$. This gives another version of Theorem 10.7:
(b) Prove that the mapping $(x, y) \mapsto(y, x)$ of $\mathbb{R}^{2}$ onto $\mathbb{R}^{2}$ is not the composition of any two primitive mappings, in any neighborhood of the origin. (This shows that the flips $B_{i}$ cannot be omitted from the statement of Theorem 10.7.)
10.4. For $(x, y) \in \mathbb{R}^{2}$, define

$$
\mathbf{F}(x, y)=\left(e^{x} \cos y-1, e^{x} \sin y\right)
$$

Prove that $\mathbf{F}=\mathbf{G}_{2} \circ \mathbf{G}_{1}$, where

$$
\begin{aligned}
& \mathbf{G}_{1}(x, y)=\left(e^{x} \cos y-1, y\right) \\
& \mathbf{G}_{2}(u, v)=(u,(1+u) \tan v)
\end{aligned}
$$

are primitive in some neighborhood of $(0,0)$.
Compute the Jacobians of $\mathbf{G}_{1}, \mathbf{G}_{2}, \mathbf{F}$ at $(0,0)$. Define

$$
\mathbf{H}_{2}(x, y)=\left(x e^{x} \sin y\right)
$$

and find

$$
\mathbf{H}_{1}(u, v)=(h(u, v), v)
$$

so that $\mathbf{F}=\mathbf{H}_{1} \circ \mathbf{H}_{2}$ in some neighborhood of $(0,0)$.
10.5. Formulate and prove an analogue of Theorem 10.8, in which K is a compact subset of an arbitrary metric space. (Replace the functions $\varphi_{i}$ that occur in the proof of Theorem 10.8 by functions of the type constructed in Exercise 4.22.)
10.6. Strengthen the conclusion of Theorem 10.8 by showing that the functions $\psi_{i}$ can be made differentiable, and even infinitely differentiable. (Use Exercise 8.1 in the construction of the auxiliary functions $\varphi_{i}$.)

10.7.
(a) Show that the simplex $Q^{k}$ is the smallest convex subset of $\mathbb{R}^{k}$ that contains $0, \mathbf{e}_{1}, \ldots, \mathbf{e}_{k}$.
(b) Show that affine mappings take convex sets to convex sets.
10.8. Let $H$ be the parallelogram in $\mathbb{R}^{2}$ whose vertices are $(1,1),(3,2),(4,5),(2,4)$. Find the affine map $T$ which sends $(0,0)$ to $(1,1),(1,0)$ to $(3,2),(0,1)$ to $(2,4)$. Show that $J_{T}=5$. Use $T$ to convert the integral

$$
\alpha=\int_{H} e^{x-y} d x d y
$$

to an integral over $I^{2}$ and thus compute $\alpha$.
10.9. Define $(x, y)=T(r, \theta)$ on the rectangle

$$
0 \leq r \leq a, \quad 0 \leq \theta \leq 2 \pi
$$

by the equations

$$
x=r \cos \theta, \quad y=r \sin \theta
$$

Show that $T$ maps this rectangle onto the closed disc $D$ with center at $(0,0)$ and radius $a$, that $T$ is one-to-one in the interior of the rectangle, and that $J_{T}(r, \theta)=r$. If $f \in \mathscr{C}(D)$, prove the formula for integration in polar coordinates:

$$
\int_{D} f(x, y) d x d y=\int_{0}^{a} \int_{0}^{2 \pi} f(T(r, \theta)) r d r d \theta
$$

Hint: Let $D_{0}$ be the interior of $D$, minus the interval from $(0,0)$ to $(0, a)$. As it stands, Theorem 10.9 applies to continuous functions $f$ whose support lies in $D_{0}$. To remove this restriction, proceed as in Example 10.4.
10.10. Let $a \rightarrow \infty$ in Exercise 10.9 and prove that

$$
\int_{\mathbb{R}^{2}} f(x, y) d x d y=\int_{0}^{\infty} \int_{0}^{2 \pi} f(T(r, \theta)) r d r d \theta
$$

for continuous functions $f$ that decrease sufficiently rapidly as $|x|+|y| \rightarrow \infty$. (Find a more precise formulation.) Apply this to

$$
f(x, y)=\exp \left(-x^{2}-y^{2}\right)
$$

to derive formula (8.101).
10.11. Define $(u, v)=T(s, t)$ on the strip

$$
0<s<\infty, \quad 0<t<1
$$

by setting $u=s-s t, v=$ st. Show that $T$ is a 1-1 mapping of the strip onto the positive quadrant $Q$ in $\mathbb{R}^{2}$. Show that $J_{T}(s, t)=s$.

For $x>0, y>0$, integrate

$$
u^{x-1} e^{-u} v^{y-1} e^{-v}
$$

over $Q$, use Theorem 10.9 to convert the integral to one over the strip, and derive formula (8.96) in this way.
(For this application, Theorem 10.9 has to be extended so as to cover certain improper integrals. Provide this extension.)
10.12. Let $I^{k}$ be the set of all $\mathbf{u}=\left(u_{1}, \ldots, u_{k}\right) \in \mathbb{R}^{k}$ with $0 \leq u_{i} \leq 1$ for all $i$; let $Q^{k}$ be the set of all $\mathbf{x}=\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{k}}\right) \in \mathbb{R}^{\mathrm{k}}$ with $\mathrm{x}_{\mathrm{i}} \geq 0, \Sigma \mathrm{x}_{\mathrm{i}} \leq 1$. ( $\mathrm{I}^{\mathrm{k}}$ is the unit cube; $\mathrm{Q}^{\mathrm{k}}$ is the standard

simplex in $\mathbb{R}^{\mathrm{k}}$.) Define $\mathbf{x}=\mathrm{T}(\mathbf{u})$ by

$$
\begin{aligned}
& \mathrm{x}_{1}=\mathrm{u}_{1} \\
& \mathrm{x}_{2}=\left(1-\mathrm{u}_{1}\right) \mathrm{u}_{2} \\
& \vdots \\
& \mathrm{x}_{\mathrm{k}}=\left(1-\mathrm{u}_{1}\right) \cdots\left(1-\mathrm{u}_{\mathrm{k}-1}\right) \mathrm{u}_{\mathrm{k}}
\end{aligned}
$$

Show that

$$
\sum_{i=1}^{k} x_{i}=1-\prod_{i=1}^{k}\left(1-u_{i}\right)
$$

Show that $T$ maps $I^{k}$ onto $Q^{k}$, that $T$ is $1-1$ in the interior of $I^{k}$, and that its inverse $S$ is defined in the interior of $Q^{k}$ by $u_{1}=x_{1}$ and

$$
u_{i}=\frac{x_{i}}{1-x_{1}-\cdots-x_{i-1}}
$$

for $i=2, \ldots, k$. Show that

$$
J_{T}(\mathbf{u})=\left(1-u_{1}\right)^{k-1}\left(1-u_{2}\right)^{k-2} \cdots\left(1-u_{k-1}\right)
$$

and

$$
J_{S}(\mathbf{x})=\left[\left(1-x_{1}\right)\left(1-x_{1}-x_{2}\right) \cdots\left(1-x_{1}-\cdots-x_{k-1}\right)\right]^{-1}
$$

10.13. Let $r_{1}, \ldots, r_{k}$ be nonnegative integers and prove that

$$
\int_{Q^{k}} x_{1}^{r_{1}} \cdots x_{k}^{r_{k}} d x=\frac{r_{1}!\cdots r_{k!}}{\left(k+r_{1}+\cdots+r_{k}\right)!}
$$

Hint: Use Exercise 10.12, Theorems 10.9 and 8.20. Note that the special case $r_{1}=\cdots=r_{k}=0$ shows that the volume of $Q^{k}$ is $1 / k$ !.
10.14. Prove formula (10.46)
10.15. If $\omega$ and $\lambda$ are $k$ - and $m$-forms, respectively, prove that

$$
\omega \wedge \lambda=(-1)^{\mathrm{km}} \lambda \wedge \omega
$$

10.16. If $k \geq 2$ and $\sigma=\left|\mathbf{p}_{0}, \mathbf{p}_{1}, \ldots, \mathbf{p}_{k}\right|$ is an oriented affine $k$-simplex, prove that $\partial^{2} \sigma=0$, directly from the definition of the boundary operator $\partial$. Deduce from this that $\partial^{2} \Psi=0$ for every chain $\Psi$.

Hint: For orientation, do it first for $k=2, k=3$. In general, if $i<j$, let $\sigma_{i j}$ be the $(k-2)$ simplex obtained by deleting $\mathbf{p}_{i}$ and $\mathbf{p}_{j}$ from $\sigma$. Show that each $\sigma_{i j}$ occurs twice in $\partial^{2} \sigma$ with opposite sign.
10.17. Put $J^{2}=\tau_{1}+\tau_{2}$, where

$$
\tau_{1}=\left[0, \mathbf{e}_{1}, \mathbf{e}_{1}+\mathbf{e}_{2}\right], \quad \tau_{2}=-\left[0, \mathbf{e}_{2}, \mathbf{e}_{2}+\mathbf{e}_{1}\right]
$$

Explain why it is reasonable to call $J^{2}$ the positively oriented unit square in $\mathbb{R}^{2}$. Show that $\partial J^{2}$ is the sum of 4 oriented affine 1 -simplexes. Find these. What is $\partial\left(\tau_{1}-\tau_{2}\right)$ ?
10.18. Consider the oriented affine 3 -simplex

$$
\sigma_{1}=\left[0, \mathbf{e}_{1}, \mathbf{e}_{1}+\mathbf{e}_{2}, \mathbf{e}_{1}+\mathbf{e}_{2}+\mathbf{e}_{3}\right]
$$

in $\mathbb{R}^{3}$. Show that $\sigma_{1}$ (regarded as a linear transformation) has determinant 1 . Thus $\sigma_{1}$ is positively oriented.

Let $\sigma_{2}, \ldots, \sigma_{6}$ be five other oriented 3-simplexes, obtained as follows: There are five permutations $\left\{i_{1}, i_{2}, i_{3}\right\}$ of $(1,2,3)$, distinct from $(1,2,3)$. Associate with each $\left\{i_{1}, i_{2}, i_{3}\right\}$ the simplex

$$
s\left(i_{1}, i_{2}, i_{3}\right)\left[0, \mathbf{e}_{i_{1}}, \mathbf{e}_{i_{1}}+\mathbf{e}_{i_{2}}, \mathbf{e}_{i_{1}}+\mathbf{e}_{i_{2}}+\mathbf{e}_{i_{3}}\right]
$$

where $s$ is the sign that occurs in the definition of the determinant. (This is how $\tau_{2}$ was obtained from $\tau_{1}$ in Exercise 10.17.) Show that $\sigma_{2}, \ldots, \sigma_{6}$ are positively oriented.

Put $\mathrm{J}^{3}=\sigma_{1}+\cdots+\sigma_{6}$. Then $\mathrm{J}^{3}$ may be called the positively oriented unit cube in $\mathbb{R}^{3}$. Show that $\partial \mathrm{J}^{3}$ is the sum of 12 oriented affine 2 -simplexes. (These 12 triangles cover the surface of the unit cube $\mathrm{I}^{3}$.)

Show that $\mathbf{x}=\left(\mathrm{x}_{1}, \mathrm{x}_{2}, \mathrm{x}_{3}\right)$ is in the range of $\sigma_{1}$ if and only if $0 \leq \mathrm{x}_{3} \leq \mathrm{x}_{2} \leq \mathrm{x}_{1} \leq 1$. Show that the ranges of $\sigma_{1}, \ldots, \sigma_{6}$ have disjoint interiors and that their union covers $\mathrm{I}^{3}$. (Compare with Exercise 10.13; note that $3!=6$.)
10.19. Let $\mathrm{J}^{2}$ and $\mathrm{J}^{3}$ be as in Exercise 10.17 and 10.18. Define

$$
\begin{array}{ll}
\mathrm{B}_{01}(u, v)=(0, u, v), & \mathrm{B}_{11}(u, v)=(1, u, v) \\
\mathrm{B}_{02}(u, v)=(u, 0, v), & \mathrm{B}_{12}(u, v)=(u, 1, v) \\
\mathrm{B}_{03}(u, v)=(u, v, 0), & \mathrm{B}_{13}(u, v)=(u, v, 1)
\end{array}
$$

These are affine, and map $\mathbb{R}^{2}$ into $\mathbb{R}^{3}$.
Put $\beta_{r i}=B_{r i}\left(J^{2}\right)$, for $r=0,1, i=1,2,3$. Each $\beta_{r i}$ is an affine-oriented 2-chain. (See Sec. 10.30.) Verify that

$$
\partial \mathrm{J}^{3}=\sum_{i=1}^{3}(-1)^{i}\left(\beta_{0 i}-\beta_{1 i}\right)
$$

in agreement with Exercise 10.18.
10.20. State conditions under which the formula

$$
\int_{\Phi} f \mathrm{~d} w=\int_{\partial \Phi} f w-\int_{\Phi}(\mathrm{df}) \wedge w
$$

is valid, and show that it generalizes the formula for integration by parts.
Hint: $\mathrm{d}(\mathrm{f} w)=(\mathrm{df}) \wedge w+\mathrm{f} \mathrm{d} w$.
10.21. As in Example 10.36, consider the 1-form

$$
\eta=\frac{x d y-y d x}{x^{2}+y^{2}}
$$

in $\mathbb{R}^{2}-\{0\}$.
(a) Carry out the computation that leads to formula (10.113) and prove that $d \eta=0$.
(b) Let $\gamma(t)=(r \cos t, r \sin t)$, for some $r>0$, and let $\Gamma$ be a $\mathscr{C}^{2}$-curve in $\mathbb{R}^{2}-\{0\}$, with parameter interval $[0,2 \pi]$, with $\Gamma(0)=\Gamma(2 \pi)$, such that the intervals $[\gamma(t), \Gamma(t)]$ do not contain 0 for any $t \in[0,2 \pi]$. Prove that

$$
\int_{\Gamma} \eta=2 \pi
$$

Hint: For $0 \leq \mathrm{t} \leq 2 \pi, 0 \leq \mathrm{u} \leq 1$, define

$$
\Phi(\mathrm{t}, \mathrm{u})=(1-\mathrm{u}) \Gamma(\mathrm{t})+\mathrm{u} \gamma(\mathrm{t})
$$

Then $\Phi$ is a 2-surface in $\mathbb{R}^{2}-\{0\}$ whose parameter domain is the indicated rectangle. Because of cancellations (as in Example 10.32),

$$
\partial \Phi=\Gamma-\gamma
$$

Use Stokes' theorem to deduce that

$$
\int_{\Gamma} \eta=\int_{\gamma} \eta
$$

because $\mathrm{d} \eta=0$.
(c) Take $\Gamma(t)=(a \cos t, b \sin t)$ where $a>0, b>0$ are fixed. Use part (b) to show that

$$
\int_{0}^{2 \pi} \frac{a b}{a^{2} \cos ^{2} t+b^{2} \sin ^{2} t} d t=2 \pi
$$

(d) Show that

$$
\eta=d\left(\arctan \frac{y}{x}\right)
$$

in any convex open set in which $x \neq 0$, and that

$$
\eta=d\left(-\arctan \frac{x}{y}\right)
$$

in any convex open set in which $y \neq 0$.
Explain why this justifies the notation $\eta=d \theta$, in spite of the fact that $\eta$ is not exact in $\mathbb{R}^{2}-(0)$.
(e) Show that (b) can be derived from (d).
(f) If $\Gamma$ is any closed $\mathscr{C}^{1}$-curve in $\mathbb{R}^{2}-\{0\}$, prove that

$$
\frac{1}{2 \pi} \int_{\Gamma} \eta=\operatorname{Ind}(\Gamma)
$$

(See Exercise 8.23 for the definition of the index of a curve.)
10.22. As in Example 10.37, define $\zeta$ in $\mathbb{R}^{3}-\{0\}$

$$
\zeta=\frac{x d y \wedge d z+y d z \wedge d x+z d x \wedge d y}{r^{3}}
$$

where $r=\left(x^{2}+y^{2}+z^{2}\right)^{1 / 2}$, let $D$ be the rectangle given by $0 \leq u \leq \pi, 0 \leq v \leq 2 \pi$, and let $\Sigma$ be the 2 -surface in $\mathbb{R}^{3}$, with parameter domain $D$, given by

$$
x=\sin u \cos v, \quad y=\sin u \sin v, \quad z=\cos u
$$

(a) Prove that $d \zeta=0$ in $\mathbb{R}^{3}-\{0\}$.
(b) Let $S$ denote the restriction of $\Sigma$ to a parameter domain $E \subset D$. Prove that

$$
\int_{S} \zeta=\int_{E} \sin u d u d v=A(S)
$$

where A denotes area, as in Theorem 10.43. Note that this contains (10.115) as a special case.
(c) Suppose $g, h_{1}, h_{2}, h_{3}$, are $\mathscr{C}^{2}$-functions on $[0,1], g>0$. Let $(x, y, z)=\Phi(s, t)$ define a 2 -surface $\Phi$, with parameter domain $I^{2}$, by

$$
x=g(t) h_{1}(s), \quad y=g(t) h_{2}(s), \quad z=g(t) h_{3}(s)
$$

Prove that

$$
\int_{\Phi} \zeta=0
$$

directly from (10.35).
Note the shape of range $\Phi$ : For fixed $s, \Phi(s, t)$ runs over an interval on a line through 0 . The range of $\Phi$ thus lies in a "cone" with vertex at the origin.

(d) Let $E$ be a closed rectangle in $D$ with edges parallel to those of $D$. Suppose $f \in \mathscr{C}^{2}(D)$, $\mathrm{f}>0$. Let $\Omega$ be the 2 -surface with a parameter domain E , defined by

$$
\Omega(u, v)=\mathrm{f}(u, v) \Sigma(u, v)
$$

Define $S$ as in (b) and prove that

$$
\int_{\Omega} \zeta=\int_{S} \zeta=A(S)
$$

(Since $S$ is the "radial projection" of $\Omega$ into the unit sphere, this result makes it reasonable to call $\int_{\Omega} \zeta$ the "solid angle" subtended by the range of $\Omega$ at the origin.)

Hint: Consider the 3 -surface $\Psi$ given by

$$
\Psi(t, u, v)=[1-t+\operatorname{tf}(u, v)] \Sigma(u, v)
$$

where $(u, v) \in E, 0 \leq t \leq 1$. For fixed $v$, the mapping $(t, u) \rightarrow \Psi(t, u, v)$ is a 2 -surface $\Phi$ to which (c) can be applied to show that $\int_{\Phi} \zeta=0$. The same thing holds when $u$ is fixed. By (a) and Stokes' theorem,

$$
\int_{\partial \Psi} \zeta=\int_{\Psi} \mathrm{d} \zeta=0
$$

(e) Put $\lambda=-(z / r) \eta$, where

$$
\eta=\frac{x d y-y d x}{x^{2}+y^{2}}
$$

as in Exercise 10.21. Then $\lambda$ is a 1 -form in the open set $V \subset \mathbb{R}^{3}$ in which $x^{2}+y^{2}>0$. Show that $\zeta$ is exact in $V$ by showing that

$$
\zeta=\mathrm{d} \lambda
$$

(f) Derive (d) from (e), without using (c).

Hint: To begin with, assume $0<u<\pi$ on E. By (e),

$$
\int_{\Omega} \zeta=\int_{\partial \Omega} \lambda \quad \text { and } \quad \int_{S} \zeta=\int_{\partial S} \lambda
$$

Show that the two integrals of $\lambda$ are equal, by using part (d) of Exercise 10.21, and by noting that $z / r$ is the same as $\Sigma(u, v)$ as at $\Omega(u, v)$.
(g) Is $\zeta$ exact in the complement of every line through the origin?
10.23. Fix $n$. Define $r_{k}=\left(x_{1}^{2}+\cdots+x_{k}^{2}\right)^{1 / 2}$ for $1 \leq k \leq n$, let $E_{k}$ be the set of all $x \in \mathbb{R}^{n}$ at which $r_{k}>0$ and let $\omega_{k}$ be the $(k-1)$-form defined in $E_{k}$ by

$$
\omega_{k}=\left(r_{k}\right)^{-k} \sum_{i=1}^{k}(-1)^{i-1} x_{i} d x_{1} \wedge \cdots \wedge d x_{i-1} \wedge d x_{i+1} \wedge \cdots \wedge d x_{k}
$$

Note that $\omega_{2}=\eta, \omega_{3}=\zeta$, in the terminology of Exercise 10.21 and 10.22. Note also that

$$
E_{1} \subset E_{2} \subset \cdots \subset E_{n}=\mathbb{R}^{n}-(0)
$$

(a) Prove that $d \omega_{k}=0$ in $E_{k}$.
(b) For $k=2, \ldots, n$, prove that $\omega_{k}$ is exact in $E_{k-1}$ by showing that

$$
\omega_{k}=d\left(f_{k} \omega_{k-1}\right)=\left(d f_{k}\right) \wedge \omega_{k-1}
$$

where $f_{k}(x)=(-1)^{k} g_{k}\left(x_{k} / r_{k}\right)$ and

$$
g_{k}(t)=\int_{-1}^{t}\left(1-s^{2}\right)^{(k-3) / 2} d s \quad(-1<t<1)
$$

Hint: $\mathrm{f}_{\mathrm{k}}$ satisfies the differential equations

$$
\mathbf{x} \cdot\left(\nabla \mathrm{f}_{\mathrm{k}}\right)(\mathbf{x})=0
$$

and

$$
\left(D_{k} f_{k}\right)(\mathbf{x})=\frac{(-1)^{k}\left(r_{k-1}\right)^{k-1}}{\left(r_{k}\right)^{k}}
$$

(c) Is $\omega_{n}$ exact in $E_{n}$ ?
(d) Note that (b) is a generalization of part (e) of Exercise 10.22. Try to extend some of the other assertions of Exercise 10.21 and 10.22 to $\omega_{n}$, for arbitrary $n$.
10.24. Let $\omega=\Sigma \mathfrak{a}_{\mathrm{i}}(\mathbf{x}) \mathrm{dx}_{\mathrm{i}}$ be a 1 -form of class $\mathscr{C}^{2}$ in a convex open set $E \subset \mathbb{R}^{n}$. Assume $\mathrm{d} \omega=0$ and prove that $\omega$ is exact in $E$, by completing the following outline:

Fix $\mathbf{p} \in \mathrm{E}$. Define

$$
f(\mathbf{x})=\int_{[\mathbf{p}, \mathbf{x}]} \omega \quad(\mathbf{x} \in \mathrm{E})
$$

Apply Stokes' theorem to affine-oriented 2-simplexes $[\mathbf{p}, \mathbf{x}, \mathbf{y}]$ in E. Deduce that

$$
f(y)-f(x)=\sum_{i=1}^{n}\left(y_{i}-x_{i}\right) \int_{0}^{1} a_{i}((1-t) x+t y) d t
$$

for $\mathbf{x} \in \mathrm{E}, \mathbf{y} \in \mathrm{E}$. Hence $\left(\mathrm{D}_{\mathrm{i}} \mathrm{f}\right)(\mathbf{x})=\mathfrak{a}_{\mathrm{i}}(\mathbf{x})$.
10.25. Assume that $\omega$ is a 1 -form in an open set $E \subset \mathbb{R}^{n}$ such that

$$
\int_{\gamma} \omega=0
$$

for every closed curve $\gamma$ in $E$ of class $\mathscr{C}^{1}$. Prove that $\omega$ is exact in $E$, by imitating part of the argument sketched in Exercise 10.24.
10.26. Assume $\omega$ is a 1 -form in $\mathbb{R}^{3}-\{0\}$ of class $\mathscr{C}^{1}$ such that $\mathrm{d} \omega=0$. Prove that $\omega$ is exact in $\mathbb{R}^{3}-\{0\}$. Hint: Every closed continuously differentiable curve in $\mathbb{R}^{3}-\{0\}$ is the boundary of the 2-surface in $\mathbb{R}^{3}-\{0\}$. Apply Stokes' theorem and Exercise 10.25.
10.27. Let $E$ be an open ball 3 -cell in $\mathbb{R}^{3}$ with edges parallel to the coordinate axes. Suppose $(\mathfrak{a}, \mathrm{b}, \mathrm{c}) \in \mathrm{E}, \mathrm{f}_{\mathrm{i}} \in \mathscr{C}^{1}(\mathrm{E})$ for $\mathrm{i}=1,2,3$,

$$
\omega=\mathrm{f}_{1} \mathrm{~d} y \wedge \mathrm{~d} z+\mathrm{f}_{2} \mathrm{~d} z \wedge \mathrm{~d} x+\mathrm{f}_{3} \mathrm{~d} x \wedge \mathrm{~d} y
$$

and assume that $\mathrm{d} \omega=0$ in E . Define

$$
\lambda=g_{1} \mathrm{~d} x+g_{2} \mathrm{~d} y
$$

where

$$
\begin{aligned}
& g_{1}(x, y, z)=\int_{c}^{z} f_{2}(x, y, s) d s-\int_{b}^{y} f_{3}(x, t, c) d t \\
& g_{2}(x, y, z)=-\int_{c}^{z} f_{1}(x, y, s) d s
\end{aligned}
$$

for $(x, y, z) \in E$. Prove that $d \lambda=\omega$ in $E$.
Evaluate these integrals when $\omega=\zeta$ and thus find the form $\lambda$ that occurs in part (e) of Exercise 10.22.

10.28. Fix $b>a>0$, define

$$
\Phi(\tau, \theta)=(\tau \cos \theta, \tau \sin \theta)
$$

for $a \leq \tau \leq b, 0 \leq \theta \leq 2 \pi$. (The range of $\Phi$ is an annulus in $\mathbb{R}^{2}$.) Put $\omega=x^{3} d y$, and compute both

$$
\int_{\Phi} \mathrm{d} \omega \quad \text { and } \quad \int_{\partial \Phi} \omega
$$

to verify that they are equal.
10.29. Prove the existence of a function $\alpha$ with the properties needed in the proof of Theorem 10.38, and prove that the resulting function $F$ is of class $\mathscr{C}^{1}$. (Both assertions become trivial if $E$ is an open cell or an open ball, since $\alpha$ can then be taken to be a constant. Refer to Theorem 9.42.)
10.30. If $\mathbf{N}$ is the vector given by (10.135), prove that

$$
\operatorname{det}\left[\begin{array}{lll}
\alpha_{1} & \beta_{1} & \alpha_{2} \beta_{3}-\alpha_{3} \beta_{2} \\
\alpha_{2} & \beta_{2} & \alpha_{3} \beta_{1}-\alpha_{1} \beta_{3} \\
\alpha_{3} & \beta_{3} & \alpha_{1} \beta_{2}-\alpha_{2} \beta_{1}
\end{array}\right]=|\mathbf{N}|^{2}
$$

Also, verify Eq. (10.137).
10.31. Let $E \subset \mathbb{R}^{3}$ be open, suppose $g \in \mathscr{C}^{2}(E), h \in \mathscr{C}^{2}(E)$, and consider the vector field

$$
\mathbf{F}=g \nabla h
$$

(a) Prove that

$$
\nabla \cdot \mathrm{F}=g \nabla^{2} \mathrm{~h}+(\nabla g) \cdot(\nabla \mathrm{h})
$$

where $\nabla^{2} \mathrm{~h}=\nabla \cdot(\nabla \mathrm{h})=\Sigma \partial^{2} \mathrm{~h} / \partial \mathrm{x}_{\mathrm{i}}^{2}$ is the so-called "Laplacian" of h .
(b) If $\Omega$ is a closed subset of $E$ with positively oriented boundary $\partial \Omega$ (as in Theorem 10.51), prove that

$$
\int_{\Omega}\left[g \nabla^{2} \mathrm{~h}+(\nabla g) \cdot(\nabla \mathrm{h})\right] \mathrm{dV}=\int_{\partial \Omega} g \frac{\partial h}{\partial n} \mathrm{~d} A
$$

where (as is customary) we have written $\partial \mathrm{h} / \partial \mathrm{n}$ in place of $(\nabla \mathrm{h}) \cdot \mathbf{n}$. (Thus $\partial \mathrm{h} / \partial \mathrm{n}$ is the directional derivative of $h$ in the direction of the outward normal to $\partial \Omega$, the socalled normal derivative of $h$.) Interchange $g$ and $h$ and subtract the resulting formula from the first one to obtain

$$
\int_{\Omega}\left(g \nabla^{2} \mathrm{~h}-\mathrm{h} \nabla^{2} g\right) \mathrm{dV}=\int_{\partial \Omega}\left(g \frac{\partial h}{\partial n}-\mathrm{h} \frac{\partial g}{\partial n}\right) \mathrm{dA}
$$

These two formulas are usually called Green's identities.
(c) Assume that $h$ is harmonic in $E$; this means that $\nabla^{2} h=0$. Take $g=1$ and conclude that

$$
\int_{\partial \Omega} \frac{\partial h}{\partial n} d A=0
$$

Take $g=h$ and conclude that $h=0$ in $\Omega$ if $h=0$ on $\partial \Omega$.
(d) Show that Green's identities are also valid in $\mathbb{R}^{2}$.
10.32. Fix $\delta, 0<\delta<1$. Let $D$ be the set of all $(\theta, t) \in \mathbb{R}^{2}$ such that $0 \leq \theta \leq \pi,-\delta \leq t \leq \delta$. Let $\Phi$ be the 2 -surface in $\mathbb{R}^{3}$, with the parameter domain $D$, given by

$$
\begin{aligned}
& x=(1-t \sin \theta) \cos 2 \theta \\
& y=(1-t \sin \theta) \sin 2 \theta \\
& z=t \cos \theta
\end{aligned}
$$

where $(x, y, z)=\Phi(\theta, t)$. Note that $\Phi(\pi, t)=\Phi(0,-t)$, and that $\Phi$ is one-to-one on the rest of D.

The range of $M=\Phi(D)$ of $\Phi$ is known as a Möbius band. It is the simplest example of a nonorientable surface.

Prove the various assertions made in the following description: Put $\mathbf{p}_{1}=(0,-\delta), \mathbf{p}_{2}=$ $(\pi,-\delta), \mathbf{p}_{3}=(\pi, \delta), \mathbf{p}_{4}=(0, \delta), \mathbf{p}_{5}=\mathbf{p}_{1}$. Put $\gamma_{i}=\left[\mathbf{p}_{i}, \mathbf{p}_{i+1}\right], i=1, \ldots, 4$, and put $\Gamma_{i}=\Phi \circ \gamma_{i}$. Then

$$
\partial \Phi=\Gamma_{1}+\Gamma_{2}+\Gamma_{3}+\Gamma_{4}
$$

Put $\mathbf{a}=(1,0,-\delta), \mathbf{b}=(1,0, \delta)$. Then

$$
\Phi\left(\mathbf{p}_{1}\right)=\Phi\left(\mathbf{p}_{3}\right)=\mathbf{a}, \quad \Phi\left(\mathbf{p}_{2}\right)=\Phi\left(\mathbf{p}_{4}\right)=\mathbf{b}
$$

and $\partial \Phi$ can be described as follows.

- $\Gamma_{1}$ spirals up from a to b; its projection into the $(x, y)$-plane has winding number +1 around the origin. (See Exercise 8.23.)
- $\Gamma_{2}=[\mathbf{b}, \mathbf{a}]$.
- $\Gamma_{3}$ spirals up from a to b; its projection into the $(x, y)$ plane has winding number -1 around the origin.
- $\Gamma_{4}=[\mathbf{b}, \mathbf{a}]$.

Thus $\partial \Phi=\Gamma_{1}+\Gamma_{3}+2 \Gamma_{2}$.
If we go from a to b along $\Gamma_{1}$ and continue along the "edge" of $M$ until we return to a, the curve traced out is

$$
\Gamma=\Gamma_{1}-\Gamma_{3}
$$

which may also be represented on the parameter interval $[0,2 \pi]$ by the equations

$$
\begin{aligned}
& x=(1+\delta \sin \theta) \cos 2 \theta \\
& y=(1+\delta \sin \theta) \sin 2 \theta \\
& z=-\delta \cos \theta
\end{aligned}
$$

It should be emphasized that $\Gamma \neq \partial \Phi$ : Let $\eta$ be the 1 -form discussed in Exercises 10.21 and 10.22. Since $\mathrm{d} \eta=0$, Stokes' theorem shows that

$$
\int_{\partial \Phi} \eta=0
$$

But although $\Gamma$ is the "geometric" boundary of $M$, we have

$$
\int_{\Gamma} \eta=4 \pi
$$

In order to avoid this possible source of confusion, Stokes' formula (Theorem 10.50) is frequently stated only for orientable surfaces $\Phi$.

# Chapter 11 

## THE LEBESGUE THEORY

It is the purpose of this chapter to present the fundamental concepts of the Lebesgue theory of measure and integration and to prove some of the crucial theorems in a rather general setting, without obscuring the main lines of development by a mass of comparatively trivial detail. Therefore proofs are only sketched in some cases, and some of the easier propositions are stated without proof. However, the reader who has become familiar with the techniques used in the preceding chapters will certainly find no difficulty in supplying the missing steps.

The theory of the Lebesgue integral can be developed in several distinct ways. Only one of these methods will be discussed here. For alternative procedures we refer to the more specialized treatises on integration listed in the Bibliography.

## SET FUNCTIONS

If $A$ and $B$ are any two sets, we write $A-B$ for the set of all elements $x$ such that $x \in A, x \notin B$. The notation $A-B$ does not imply that $B \subset A$. We denote the empty set by $\varnothing$ and say that $A$ and $B$ are disjoint if $A \cap B=\varnothing$.
11.1 Definition. A family $\mathscr{R}$ of sets is called a ring if $A \in \mathscr{R}$ and $B \in \mathscr{R}$ implies

$$
A \cup B \in \mathscr{R}, \quad A-B \in \mathscr{R}
$$

Since $A \cap B=A-(A-B)$, we also have $A \cap B \in \mathscr{R}$ if $\mathscr{R}$ is a ring.
A ring is called a $\sigma$-ring if

$$
\bigcup_{n=1}^{\infty} A_{n} \in \mathscr{R}
$$

whenever $A_{n} \in \mathscr{R}(n=1,2,3, \ldots)$. Since

$$
\bigcap_{n=1}^{\infty} A_{n}=A_{1}-\bigcup_{n=1}^{\infty}\left(A_{1}-A_{n}\right)
$$

we also have

$$
\bigcap_{n=1}^{\infty} A_{n} \in \mathscr{R}
$$

if $\mathscr{R}$ is a $\sigma$-ring.
11.2 Definition. We say that $\phi$ is a set function defined on $\mathscr{R}$ if $\phi$ assigns to every $A \in \mathscr{R}$ a number $\phi(A)$ of the extended real number system. $\phi$ is additive if $A \cap B=\varnothing$ implies

$$
\phi(A \cup B)=\phi(A)+\phi(B)
$$

and $\phi$ is countably additive if $A_{i} \cap A_{j}=\varnothing(i \neq j)$ implies

$$
\phi\left(\bigcup_{n=1}^{\infty} A_{n}\right)=\sum_{n=1}^{\infty} \phi\left(A_{n}\right)
$$

We shall always assume that the range of $\phi$ does not contain both $+\infty$ and $-\infty$; if it did, the right side of (11.3) could become meaningless. Also, we exclude set functions whose only value is $+\infty$ or $-\infty$.

It is interesting to note that the left side of (11.4) is independent of the order in which the $A_{n}$ 's are arranged. Hence the rearrangement theorem shows that the right side of (11.4) converges absolutely if it converges at all; if it does not converge, the partial sums tend to $+\infty$ or to $-\infty$.

If $\phi$ is additive, the following properties are easily verified:

$$
\begin{aligned}
\phi(\varnothing) & =\varnothing \\
\phi\left(A_{1} \cup \cdots \cup A_{n}\right) & =\phi\left(A_{1}\right)+\cdots+\phi\left(A_{n}\right)
\end{aligned}
$$

if $A_{i} \cap A_{j}=\varnothing$ whenever $i \neq j$.

$$
\phi\left(A_{1} \cup A_{2}\right)+\phi\left(A_{1} \cap A_{2}\right)=\phi\left(A_{1}\right)+\phi\left(A_{2}\right)
$$

If $\phi(A) \geq 0$ for all $A$ and $A_{1} \cup A_{2}$, then

$$
\phi\left(A_{1}\right) \leq \phi\left(A_{2}\right)
$$

Because of (11.8), nonnegative additive set functions are often called monotonic.

$$
\phi(A-B)=\phi(A)-\phi(B)
$$

if $B \subset A$ and $|\phi(B)|<+\infty$.
11.3 Theorem. Suppose $\phi$ is countably additive on a ring $\mathscr{R}$. Suppose $A_{n} \in \mathscr{R}(n=$ $1,2,3, \ldots), A_{1} \subset A_{2} \subset A_{3} \subset \cdots, A \in \mathscr{R}$, and

$$
A=\bigcup_{n=1}^{\infty} A_{n}
$$

Then, as $\mathrm{n} \rightarrow \infty$,

$$
\phi\left(A_{n}\right) \rightarrow \phi(A)
$$

Proof. Put $B_{1}=A_{1}$ and

$$
B_{n}=A_{n}-A_{n-1} \quad(n=2,3, \ldots)
$$

Then $B_{i} \cap B_{j}=\varnothing$ for $i \neq j, A_{n}=B_{1} \cup \cdots \cup B_{n}$, and $A=\bigcup B_{n}$. Hence

$$
\phi\left(A_{n}\right)=\sum_{i=1}^{n} \phi\left(B_{i}\right)
$$

and

$$
\phi(A)=\sum_{i=1}^{\infty} \phi\left(B_{i}\right)
$$

# CONSTRUCTION OF THE LEBESGUE MEASURE 

11.4 Definition. Let $\mathbb{R}^{\mathrm{p}}$ denote p -dimensional euclidean space. By an interval in $\mathbb{R}^{\mathrm{p}}$, we mean the set of points $\mathbf{x}=\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{p}}\right)$ such that

$$
a_{i} \leq x_{i} \leq b_{i} \quad(i=1, \ldots, p)
$$

or the set of points which is characterized by (11.10) with any or all of the $\leq$ signs replaced by $<$. The possibility that $a_{i}=b_{i}$ for any value of $i$ is not ruled out; in particular, the empty set is included among intervals.

If $A$ is the union of a finite number of intervals, $A$ is said to be an elementary set. If I is an interval, we define

$$
m(I)=\prod_{i=1}^{p}\left(b_{i}-a_{i}\right)
$$

no matter whether equality is included or excluded in any of the inequalities (11.10).
If $A=I_{1} \cup \cdots \cup I_{n}$, and if these intervals are pairwise disjoint, we set

$$
m(A)=m\left(I_{1}\right)+\cdots+m\left(I_{n}\right)
$$

We let $\mathscr{E}$ denote the family of all elementary subsets of $\mathbb{R}^{\mathrm{p}}$.

At this point, the following properties should be verified:
(11.12) $\mathscr{E}$ is a ring but not a $\sigma$-ring.
(11.13) If $A \in \mathscr{E}$, then $A$ is the union of a finite number of disjoint intervals.
(11.14) If $A \in \mathscr{E}, m(A)$ is well defined by (11.11); that is, if two different decompositions of $A$ into disjoint intervals are used, each gives rise to the same value of $m(A)$.
(11.15) $m$ is additive on $\mathscr{E}$.

Note that if $p=1,2,3$, then $m$ is length, area, and volume, respectively.
11.5 Definition. A nonnegative additive set function $\phi$ defined on $\mathscr{E}$ is said to be regular if the following is true: To every $A \in \mathscr{E}$ and to every $\varepsilon>0$, there exists sets $F \in \mathscr{E}, G \in \mathscr{E}$ such that $F$ is closed, $G$ is open, $F \subset A \subset G$, and

$$
\phi(G)-\varepsilon \leq \phi(A) \leq \phi(F)+\varepsilon
$$

# 11.6 Examples. 

(a) The set function $m$ is regular.

If $A$ is an interval, it is trivial that the requirements of Definition 11.5 are satisfied. The general case follows from (11.13).
(b) Take $\mathbb{R}^{p}=\mathbb{R}^{1}$ and let $\alpha$ be a monotonically increasing function defined for all real $x$. Put

$$
\begin{aligned}
& \mu([a, b))=\alpha(b-)-\alpha(a-), \\
& \mu([a, b])=\alpha(b+)-\alpha(a-), \\
& \mu((a, b])=\alpha(b+)-\alpha(a+), \\
& \mu((a, b))=\alpha(b-)-\alpha(a+)
\end{aligned}
$$

Here $[a, b)$ is the set $a \leq x<b$, etc. Because of the possible discontinuities of $\alpha$, these cases have to be distinguished. If $\mu$ is defined for elementary sets as in (11.11), $\mu$ is regular on $\mathscr{E}$. The proof is just like that of (a).
Our next objective is to show that every regular set function on $\mathscr{E}$ can be extended to a countably additive set function on a $\sigma$-ring which contains $\mathscr{E}$.
11.7 Definition. Let $\mu$ be additive, regular, nonnegative, and finite on $\mathscr{E}$. Consider countable coverings of any set $E \subset \mathbb{R}^{p}$ by open elementary sets $A_{n}$ :

$$
E \subset \bigcup_{n=1}^{\infty} A_{n}
$$

Define

$$
\mu^{*}(E)=\inf \sum_{n=1}^{\infty} \mu\left(A_{n}\right)
$$

the inf being taken over all countable coverings of $E$ by open elementary sets. $\mu^{*}(E)$ is called the outer measure of $E$, corresponding to $\mu$.

It is clear that $\mu^{*}(\mathrm{E}) \geq 0$ for all E and that

$$
\mu^{*}\left(E_{1}\right) \leq \mu^{*}\left(E_{2}\right)
$$

if $E_{1} \subset E_{2}$.

# 11.8 Theorem. 

(a) For every $A \in \mathscr{E}, \mu^{*}(A)=\mu(A)$.
(b) If $\mathrm{E} \subset \bigcup_{n=1}^{\infty} \mathrm{E}_{n}$, then

$$
\mu^{*}(\mathrm{E}) \leq \sum_{n=1}^{\infty} \mu^{*}\left(E_{n}\right)
$$

Note that (a) asserts that $\mu^{*}$ is an extension of $\mu$ from $\mathscr{E}$ to the family of all subsets of $\mathbb{R}^{p}$. The property (11.19) is called subadditivity.

Proof. Choose $A \in \mathscr{E}$ and $\varepsilon>0$.
The regularity of $\mu$ shows that $A$ is contained in an open elementary set $G$ such that $\mu(\mathrm{G}) \leq \mu(\mathrm{A})+\varepsilon$. Since $\mu^{*}(\mathrm{~A}) \leq \mu(\mathrm{G})$ and since $\varepsilon$ was arbitrary, we have

$$
\mu^{*}(A) \leq \mu(A)
$$

The definition of $\mu^{*}$ shows that there is a countable collection of open elementary sets $\left\{A_{n}\right\}$ whose union contains $A$, such that

$$
\sum_{n=1}^{\infty} \mu\left(A_{n}\right) \leq \mu^{*}(A)+\varepsilon
$$

The regularity of $\mu$ shows that $A$ contains a closed elementary set $F$ such that $\mu(\mathrm{F}) \geq \mu(\mathrm{A})-\varepsilon$; since F is compact, we have

$$
\mathrm{F} \subset \mathrm{~A}_{1} \cup \cdots \cup \mathrm{~A}_{\mathrm{N}}
$$

for some N. Hence

$$
\mu(A) \leq \mu(F)+\varepsilon \leq \mu\left(A_{1} \cup \cdots \cup A_{N}\right)+\varepsilon \leq \sum_{n=1}^{N} \mu\left(A_{n}\right)+\varepsilon \leq \mu^{*}(A)+2 \varepsilon
$$

In conjunction with (11.20), this proves (a).
Next, suppose $E=\bigcup E_{n}$ and assume that $\mu^{*}\left(E_{n}\right)<+\infty$ for all $n$. Given $\varepsilon>0$,

there are coverings $\left\{A_{n, k}\right\}, k=1,2,3, \ldots$, of $E_{n}$ by open elementary sets such that

$$
\sum_{k=1}^{\infty} \mu\left(A_{n, k}\right) \leq \mu^{*}\left(E_{n}\right)+2^{-n} \varepsilon
$$

Then

$$
\mu^{*}(E) \leq \sum_{n=1}^{\infty} \sum_{k=1}^{\infty} \mu\left(A_{n, k}\right) \leq \sum_{n=1}^{\infty} \mu^{*}\left(E_{n}\right)+\varepsilon
$$

and (11.19) follows. In the excluded case, i.e., if $\mu^{*}\left(E_{n}\right)=+\infty$ for some $n$, (11.19) is of course trivial.
11.9 Definition. For any $A \subset \mathbb{R}^{p}, B \subset \mathbb{R}^{p}$, we define

$$
\begin{aligned}
& S(A, B)=(A-B) \cup(B-A) \\
& d(A, B)=\mu^{*}(S(A, B))
\end{aligned}
$$

We write $A_{n} \rightarrow A$ if

$$
\lim _{n \rightarrow \infty} d\left(A, A_{n}\right)=0
$$

If there is a sequence $\left(A_{n}\right)$ of elementary sets such that $A_{n} \rightarrow A$, we say that $A$ is finitely $\mu$-measurable and write $A \in \mathfrak{M}_{F}(\mu)$. If $A$ is the union of a countable collection of finitely $\mu$-measurable sets, we say that $A$ is $\mu$-measurable and write $A \in \mathfrak{M}(\mu)$.
$S(A, B)$ is the so-called "symmetric difference" of $A$ and $B$. We shall see that $d(A, B)$ is essentially a distance function.

The following theorem will enable us to obtain the desired extension of $\mu$.
11.10 Theorem. $\mathfrak{M}(\mu)$ is a $\sigma$-ring and $\mu^{*}$ is countably additive on $\mathfrak{M}(\mu)$.

Before we turn to the proof of this theorem, we develop some of the properties of $S(A, B)$ and $d(A, B)$. We have

$$
\begin{gathered}
S(A, B)=S(B, A), \quad S(A, A)=0 \\
S(A, B) \subset S(A, C) \cup S(C, B) \\
\left.\begin{array}{l}
S\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \\
S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) \\
S\left(A_{1}-A_{2}, B_{1}-B_{2}\right)
\end{array}\right\} \subset S\left(A_{1}, B_{1}\right) \cup S\left(A_{1}, B_{2}\right) \\
\left.\begin{array}{l}
S\left(A_{1}-A_{2}, B_{1}-B_{2}\right)
\end{array}\right\}
\end{gathered}
$$

(11.24) is clear and (11.25) follows from

$$
(A-B) \subset(A-C) \cup(C-B), \quad(B-A) \subset(C-A) \cup(B-C)
$$

The first formula of (11.26) is obtained from

$$
\left(A_{1} \cup A_{2}\right)-\left(B_{1} \cup B_{2}\right) \subset\left(A_{1}-B_{1}\right) \cup\left(A_{2}-B_{2}\right)
$$

Next, writing $\mathrm{E}^{\mathrm{c}}$ for the complement of E , we have

$$
\begin{aligned}
S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) & =S\left(A_{1}^{c} \cup A_{2}^{c}, B_{1}^{c} \cup B_{2}^{c}\right) \\
& \subset S\left(A_{1}^{c}, B_{1}^{c}\right) \cup S\left(A_{2}^{c}, B_{2}^{c}\right)=S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
\end{aligned}
$$

the last formula of (11.26) is obtained if we note that

$$
A_{1}-A_{2}=A_{1} \cap A_{2}^{c}
$$

by (11.23), (11.19), and (11.18), these properties of $S(A, B)$ imply

$$
\begin{gathered}
\mathrm{d}(\mathrm{~A}, \mathrm{~B})=\mathrm{d}(\mathrm{~B}, \mathrm{~A}), \quad \mathrm{d}(\mathrm{~A}, \mathrm{~A})=0 \\
\mathrm{~d}(\mathrm{~A}, \mathrm{~B}) \leq \mathrm{d}(\mathrm{~A}, \mathrm{C})+\mathrm{d}(\mathrm{C}, \mathrm{~B}) \\
\left.\begin{array}{c}
\mathrm{d}\left(\mathrm{~A}_{1} \cup \mathrm{~A}_{2}, \mathrm{~B}_{1} \cup \mathrm{~B}_{2}\right) \\
\mathrm{d}\left(\mathrm{~A}_{1} \cap \mathrm{~A}_{2}, \mathrm{~B}_{1} \cap \mathrm{~B}_{2}\right)
\end{array}\right\} \leq \mathrm{d}\left(\mathrm{A}_{1}, \mathrm{~B}_{1}\right)+\mathrm{d}\left(\mathrm{A}_{2}, \mathrm{~B}_{2}\right) \\
\mathrm{d}\left(\mathrm{~A}_{1}-\mathrm{A}_{2}, \mathrm{~B}_{1}-\mathrm{B}_{2}\right)
\end{gathered}
$$

The relations (11.27) and (11.28) show that $\mathrm{d}(\mathrm{A}, \mathrm{B})$ satisfies the requirements of Definition 2.15 , except that $\mathrm{d}(\mathrm{A}, \mathrm{B})=0$ does not imply $\mathrm{A}=\mathrm{B}$. For instance, if $\mu=\mathrm{m}, \mathrm{A}$ is countable, and B is empty, we have

$$
\mathrm{d}(\mathrm{~A}, \mathrm{~B})=\mathrm{m}^{*}(\mathrm{~A})=0
$$

to see this, cover the nth point of A by an interval $\mathrm{I}_{\mathrm{n}}$ such that

$$
\mathrm{m}\left(\mathrm{I}_{\mathrm{n}}\right)<2^{-\mathrm{n}} \varepsilon
$$

However, if we define two sets $A$ and $B$ to be equivalent, provided

$$
\mathrm{d}(\mathrm{~A}, \mathrm{~B})=0
$$

we divide the subsets of $\mathbb{R}^{\mathrm{p}}$ into equivalence classes and $\mathrm{d}(\mathrm{A}, \mathrm{B})$ makes the set of these equivalence classes into a metric space. $\mathfrak{M}_{\mathrm{F}}(\mu)$ is then obtained as the closure of $\mathscr{E}$. This interpretation is not essential for the proof, but it explains the underlying idea.

We need one more property of $\mathrm{d}(\mathrm{A}, \mathrm{B})$, namely,

$$
\left|\mu^{*}(\mathrm{~A})-\mu^{*}(\mathrm{~B})\right| \leq \mathrm{d}(\mathrm{~A}, \mathrm{~B})
$$

if at least one of $\mu^{*}(\mathrm{~A}), \mu^{*}(\mathrm{~B})$ is finite. For suppose $0 \leq \mu^{*}(\mathrm{~B}) \leq \mu^{*}(\mathrm{~A})$. Then (11.28) showos that

$$
\mathrm{d}(\mathrm{~A}, \varnothing) \leq \mathrm{d}(\mathrm{~A}, \mathrm{~B})+\mathrm{d}(\mathrm{~B}, \varnothing)
$$

that is,

$$
\mu^{*}(\mathrm{~A}) \leq \mathrm{d}(\mathrm{~A}, \mathrm{~B})+\mu^{*}(\mathrm{~B})
$$

Since $\mu^{*}(\mathrm{~B})$ is finite, it follows that

$$
\mu^{*}(\mathrm{~A})-\mu^{*}(\mathrm{~B}) \leq \mathrm{d}(\mathrm{~A}, \mathrm{~B})
$$

Proof of Theorem 11.10. Suppose $A \in \mathfrak{M}_{F}(\mu), B \in \mathfrak{M}_{F}(\mu)$. Choose $\left(A_{n}\right),\left(B_{n}\right)$ such that $A_{n} \in \mathscr{E}, B_{n} \in \mathscr{E}, A_{n} \rightarrow A, B_{n} \rightarrow B$. Then (11.29) and (11.30) show that

$$
\begin{aligned}
A_{n} \cup B_{n} & \rightarrow A \cup B \\
A_{n} \cap B_{n} & \rightarrow A \cap B \\
A_{n}-B_{n} & \rightarrow A-B \\
\mu^{*}\left(A_{n}\right) & \rightarrow \mu^{*}(A)
\end{aligned}
$$

and $\mu^{*}(A)<+\infty$ since $d\left(A_{n}, A\right) \rightarrow 0$. By (11.31) and (11.33), $\mathfrak{M}_{F}(\mu)$ is a ring. By (11.7),

$$
\mu\left(A_{n}\right)+\mu\left(B_{n}\right)=\mu\left(A_{n} \cup B_{n}\right)+\mu\left(A_{n} \cap B_{n}\right)
$$

Letting $n \rightarrow \infty$, we obtain, by (11.34) and Theorem 11.8(a),

$$
\mu^{*}(A)+\mu^{*}(B)=\mu^{*}(A \cup B)+\mu^{*}(A \cap B)
$$

If $A \cap B=\varnothing$, then $\mu^{*}(A \cap B)=0$. It follows that $\mu^{*}$ is additive on $\mathfrak{M}_{F}(\mu)$.
Now let $A \in \mathfrak{M}(\mu)$. Then $A$ can be represented as the union of a countable collection of disjoint sets of $\mathfrak{M}_{F}(\mu)$. For if $A=\bigcup A_{n}^{\prime}$, with $A_{n}^{\prime} \in \mathfrak{M}_{F}(\mu)$, write $A_{1}=A_{1}^{\prime}$ and

$$
A_{n}=\left(A_{1}^{\prime} \cup \cdots \cup A_{n}^{\prime}\right)-\left(A_{1}^{\prime} \cup \cdots \cup A_{n-1}^{\prime}\right) \quad(n=2,3,4, \ldots)
$$

Then

$$
A=\bigcup_{n=1}^{\infty} A_{n}
$$

is the required representation. By (11.19),

$$
\mu^{*}(A) \leq \sum_{n=1}^{\infty} \mu^{*}\left(A_{n}\right)
$$

On the other hand, $A \supset A_{1} \cup \cdots \cup A_{n}$; by the additivity of $\mu^{*}$ on $\mathfrak{M}_{F}(\mu)$, we obtain

$$
\mu^{*}(A) \geq \mu^{*}\left(A_{1} \cup \cdots \cup A_{n}\right)=\mu^{*}\left(A_{1}\right)+\cdots+\mu^{*}\left(A_{n}\right)
$$

Equations (11.36) and (11.37) imply

$$
\mu^{*}(A)=\sum_{n=1}^{\infty} \mu^{*}\left(A_{n}\right)
$$

Suppose $\mu^{*}(\mathrm{~A})$ is finite. Put $\mathrm{B}_{n}=\mathrm{A}_{1} \cup \cdots \cup \mathrm{~A}_{n}$. Then (11.38) shows that

$$
\mathrm{d}\left(\mathrm{~A}, \mathrm{~B}_{n}\right)=\mu^{*}\left(\bigcup_{i=n+1}^{\infty} A_{i}\right)=\sum_{i=n+1}^{\infty} \mu^{*}\left(A_{i}\right) \rightarrow 0
$$

as $n \rightarrow \infty$. Hence $B_{n} \rightarrow A$; since $B_{n} \in \mathfrak{M}_{F}(\mu)$, it is easily seen that $A \in \mathfrak{M}_{F}(\mu)$. We have thus shown that $A \in \mathfrak{M}_{F}(\mu)$ if $A \in \mathfrak{M}(\mu)$ and $\mu^{*}(A)<+\infty$.

It is now clear that $\mu^{*}$ is countably additive on $\mathfrak{M}(\mu)$. For if

$$
A=\bigcup_{n=1}^{\infty} A_{n}
$$

where $\left\{A_{n}\right\}$ is a countable collection of disjoint sets of $\mathfrak{M}(\mu)$, we have shown that (11.38) holds if $\mu^{*}\left(A_{n}\right)<+\infty$ for every $n$, and in the other case (11.38) is trivial.

Finally, we have to show that $\mathfrak{M}(\mu)$ is a $\sigma$-ring. If $A_{n} \in \mathfrak{M}(\mu), n=1,2,3, \ldots$, it is clear that $\bigcup A_{n} \in \mathfrak{M}(\mu)$ (Theorem 2.12). Suppose $A \in \mathfrak{M}(\mu), B \in \mathfrak{M}(\mu)$, and

$$
A=\bigcup_{n=1}^{\infty} A_{n}, \quad B=\bigcup_{n=1}^{\infty} B_{n}
$$

where $A_{n}, B_{n} \in \mathfrak{M}_{F}(\mu)$. Then the identity

$$
A_{n} \cap B=\bigcup_{i=1}^{\infty}\left(A_{n} \cap B_{i}\right)
$$

shows that $A_{n} \cap B \in \mathfrak{M}(\mu)$; since

$$
\mu^{*}\left(A_{n} \cap B\right) \leq \mu^{*}\left(A_{n}\right)<\infty
$$

$A_{n} \cap B \in \mathfrak{M}_{F}(\mu)$. Hence $A_{n}-B \in \mathfrak{M}_{F}(\mu)$, and $A-B \in \mathfrak{M}(\mu)$ since $A-B=$ $\bigcup_{n=1}^{\infty}\left(A_{n}-B\right)$.

We now replace $\mu^{*}(A)$ by $\mu(A)$ if $A \in \mathfrak{M}(\mu)$. Thus $\mu$, originally only defined on $\mathscr{E}$, is extended to a countably additive set function on the $\sigma$-ring $\mathfrak{M}(\mu)$. This extended set function is called a measure. The special case $\mu=m$ is called the Lebesgue measure on $\mathbb{R}^{p}$.

# 11.11 Remarks. 

(a) If $A$ is open, then $A \in \mathfrak{M}(\mu)$. For every open set in $\mathbb{R}^{p}$ is the union of a countable collection of open intervals. To see this, it is sufficient to construct a countable base whose members are open intervals. By taking complements, it follows that every closed set is in $\mathfrak{M}(\mu)$.
(b) If $A \in \mathfrak{M}(\mu)$ and $\varepsilon>0$, there exist sets $F$ and $G$ such that

$$
F \subset A \subset G
$$

F is closed, G is open, and

$$
\mu(\mathrm{G}-\mathrm{A})<\varepsilon, \quad \mu(\mathrm{~A}-\mathrm{F})<\varepsilon
$$

The first inequality holds since $\mu^{*}$ was defined by means of coverings by open elementary sets. The second inequality then follows by taking complements.
(c) We say that $E$ is a Borel set if $E$ can be obtained by a countable number of operations, starting from open sets, each operation consisting in taking unions, intersections, or complements. The collection $\mathscr{B}$ of all Borel sets in $\mathbb{R}^{\mathrm{p}}$ is a $\sigma$-ring; in fact, it is the smallest sigma ring which contains all open sets. By (a), $E \in \mathfrak{M}(\mu)$ if $E \in \mathscr{B}$.
(d) If $A \in \mathfrak{M}(\mu)$, there exist Borel sets $F$ and $G$ such that $F \subset A \subset G$, and

$$
\mu(\mathrm{G}-\mathrm{A})=\mu(\mathrm{A}-\mathrm{F})=0
$$

This follows from (b) if we take $\varepsilon=1 / n$ and let $n \rightarrow \infty$.
Since $A=F \cup(A-F)$ we see that every $\mathfrak{M}(\mu)$ is the union of a Borel set and a set of measure zero.

The Borel sets are $\mu$-measurable for every $\mu$. But the sets of measure zero [that is, the sets $E$ for which $\mu^{*}(E)=0$ ] may be different for different $\mu$ 's.
(e) For every $\mu$, the sets of measure zero form a $\sigma$-ring.
(f) In the case of the Lebesgue measure, every countable set has measure zero. But there are uncountable sets of measure zero. The Cantor set may be taken as an example: Using the notation of Theorem 2.44, it is easily seen that

$$
m\left(E_{n}\right)=\left(\frac{2}{3}\right)^{n} \quad(n=1,2,3, \ldots)
$$

since $P=\bigcap E_{n}, P \subset E_{n}$ for every $n$ so that $m(P)=0$.

# MEASURE SPACES 

11.12 Definition. Suppose $X$ is a set, not necessarily a subset of a euclidean space or, indeed, of any metric space. $X$ is said to be a measure space if there exists a $\sigma$-ring $\mathfrak{M}$ of subsets of $X$ (which are called measurable sets) and a nonnegative countably additive set function $\mu$ (which is called a measure), defined on $\mathfrak{M}$. If, in addition, $X \in \mathfrak{M}$, then $X$ is said to be a measurable space. ${ }^{1}$

For instance, we can take $X=\mathbb{R}^{\mathrm{p}}, \mathfrak{M}$ the collection of all Lebesgue-measurable subsets of $\mathbb{R}^{\mathrm{p}}$, and $\mu$ the Lebesgue measure.

Or, let $X$ be the set of all positive integers, $\mathfrak{M}$ be the collection of all subsets of $X$, and $\mu(E)$ the number of elements of $E$.

[^0]
[^0]:    ${ }^{1}$ The definition that Rudin gives here is very much at-odds with everybody else. Even he defines this term differently later, in his Real and Complex Analysis text.

Another example is provided by probability theory, where events may be considered as sets, and the probability of the occurrence of events is an additive (or countably additive) set function.

In the following sections we shall always deal with measurable spaces. It should be emphasized that the integration theory which we shall soon discuss would not become simpler in any respect if we sacrificed the generality we have now attained and restricted ourselves to Lebesgue measure, say, on an interval of the real line. In fact, the essential features of the theory are brought out with much greater clarity in the more general situation, where it is seen that everything depends only on the countable additivity of $\mu$ on a $\sigma$-ring.

It will be convenient to introduce the notation

$$
\{x \mid P\}
$$

for the set of all elements $x$ which have the property $P$.

# MEASURABLE FUNCTIONS 

11.13 Definition. Let $f$ be a function defined on the measurable space $X$ with values in the extended real number system. The function $f$ is said to be measurable if the set

$$
\{x \mid f(x)>a\}
$$

is measurable for every real a.
11.14 Example. If $X=\mathbb{R}^{p}$ and $\mathfrak{M}=\mathfrak{M}(\mu)$ as defined in Definition 11.9, then every continuous $f$ is measurable, since then (11.42) is an open set.
11.15 Theorem. Each of the following four conditions implies the other three:

$$
\begin{aligned}
& \{x \mid f(x)>a\} \text { is measurable for every real } a \\
& \{x \mid f(x) \geq a\} \text { is measurable for every real } a \\
& \{x \mid f(x)<a\} \text { is measurable for every real } a \\
& \{x \mid f(x) \leq a\} \text { is measurable for every real } a
\end{aligned}
$$

Proof. The relations

$$
\begin{aligned}
& \{x \mid f(x) \geq a\}=\bigcap_{n=1}^{\infty}\left\{x \mid f(x)>a-\frac{1}{n}\right\} \\
& \{x \mid f(x)<a\}=X-\{x \mid f(x) \geq a\} \\
& \{x \mid f(x) \leq a\}=\bigcap_{n=1}^{\infty}\left\{x \mid f(x)<a+\frac{1}{n}\right\} \\
& \{x \mid f(x)>a\}=X-\{x \mid f(x) \leq a\}
\end{aligned}
$$

show successively that (11.43) implies (11.44), (11.44) implies (11.45), (11.45) implies (11.46), and (11.46) implies (11.43).

Hence any of these conditions may be used instead of (11.42) to define measurability.
11.16 Theorem. If f is measurable, then $|\mathrm{f}|$ is measurable.

Proof. $\{\mathrm{x}||\mathrm{f}(\mathrm{x})|<\mathrm{a}\}=\{\mathrm{x} \mid \mathrm{f}(\mathrm{x})<\mathrm{a}\} \cup\{\mathrm{x} \mid \mathrm{f}(\mathrm{x})>-\mathrm{a}\}$.
11.17 Theorem. Let $\left(f_{n}\right)$ be a sequence of measurable functions. For $x \in X$, put

$$
\begin{aligned}
& g(x)=\sup f_{n}(x) \quad(n=1,2,3, \ldots) \\
& h(x)=\limsup _{n \rightarrow \infty} f_{n}(x)
\end{aligned}
$$

Then $g$ and $h$ are measurable. The same is of course true of the inf and $\lim \inf$.
Proof.

$$
\begin{aligned}
\{x \mid g(x)>a\} & =\bigcup_{n=1}^{\infty}\left\{x \mid f_{n}(x)>a\right\} \\
h(x) & =\inf g_{m}(x)
\end{aligned}
$$

where $g_{m}(x)=\sup f_{n}(x)(n \geq m)$.

# Corollary. 

(a) If f and g are measurable, then $\max (\mathrm{f}, \mathrm{g})$ and $\min (\mathrm{f}, \mathrm{g})$ are measurable. If

$$
f^{+}=\max (f, 0), \quad f^{-}=-\min (f, 0)
$$

it follows, in particular, that $\mathrm{f}^{+}$and $\mathrm{f}^{-}$are measurable.
(b) The limit of a convergent sequence of measurable functions is measurable.
11.18 Theorem. Let f and g be measurable real-valued functions defined on X , let F be real and continuous on $\mathbb{R}^{2}$, and put

$$
h(x)=F(f(x), g(x)) \quad(x \in X)
$$

Then h is measurable. In particular, $\mathrm{f}+\mathrm{g}$ and fg are measurable.
Proof. Let

$$
G_{a}=\{(u, v) \mid F(u, v)>a\}
$$

Then $G_{a}$ is an open subset of $\mathbb{R}^{2}$ and we can write

$$
G_{a}=\bigcup_{n=1}^{\infty} I_{n}
$$

where $\left(I_{n}\right)$ is a sequence of open intervals:

$$
I_{n}=\left\{\left(u, v \mid a_{n}<u<b_{n}, c_{n}<v<d_{n}\right\}\right.
$$

Since

$$
\left\{x \mid a_{n}<f(x)<b_{n}\right\}=\left\{x \mid f(x)>a_{n}\right\} \cap\left\{x \mid f(x)<b_{n}\right\}
$$

is measurable, it follows that the set

$$
\left\{x \mid(f(x), g(x)) \in I_{n}\right\}=\left\{x \mid a_{n}<f(x)<b_{n}\right\} \cap\left\{x \mid c_{n}<g(x)<d_{n}\right\}
$$

is measurable. Hence the same is true of

$$
\begin{aligned}
\{x \mid h(x)>a\} & =\left\{x \mid(f(x), g(x)) \in G_{a}\right\} \\
& =\bigcup_{n=1}^{\infty}\left\{x \mid(f(x), g(x)) \in I_{n}\right\} .
\end{aligned}
$$

Summing up, we may say that all ordinary operations of analysis, including limit operations, when applied to measurable functions, lead to measurable functions; in other words, all functions that are ordinarily met with are measurable.

That this is, however, only a rough statement is shown by the following example (based on Lebesgue measure, on the real line): If $h(x)=f(g(x))$, where $f$ is measurable and $g$ is continuous, then $h$ is not necessarily measurable. (For the details, we refer to McShane [McS44], page 241).

The reader may have noticed that measure has not been mentioned in our discussion of measurable functions. In fact, the class of measurable functions on X depends only on the $\sigma$-ring $\mathfrak{M}$ (using the notation of Definition 11.12). For instance, we may speak of Borel-measurable functions on $\mathbb{R}^{\mathrm{P}}$, that is, of functions f for which

$$
\{x \mid f(x)>a\}
$$

is always a Borel set, without reference to any particular measure.

# SIMPLE FUNCTIONS 

11.19 Definition. Let $s$ be a real-valued function defined on $X$. If the range of $s$ is finite, we say that $s$ is a simple function.

Let $E \subset X$, and put

$$
K_{E}(x)= \begin{cases}1 & (x \in E) \\ 0 & (x \notin E)\end{cases}
$$

$\mathrm{K}_{\mathrm{E}}$ is called the characteristic function of E .

Suppose the range of $s$ consists of the distinct numbers $c_{1}, \ldots, c_{n}$. Let

$$
E_{i}=\left\{x \mid s(x)=c_{i}\right\} \quad(i=1, \ldots, n)
$$

Then

$$
s=\sum_{i=1}^{n} c_{i} K_{E_{i}}
$$

that is, every simple function is a finite linear combination of characteristic functions. It is clear that $s$ is measurable if and only if the sets $E_{1}, \ldots, E_{n}$ are measurable.

It is of interest that every function can be approximated by simple functions:
11.20 Theorem. Let f be a real function on X . There exists a sequence $\left(s_{n}\right)$ of simple functions such that $s_{n}(x) \rightarrow f(x)$ as $n \rightarrow \infty$, for every $x \in X$. If $f$ is measurable, $\left(s_{n}\right)$ may be chosen to be a sequence of measurable functions. If $\mathrm{f} \geq 0,\left(\mathrm{~s}_{\mathrm{n}}\right)$ may be chosen to be a monotonically increasing sequence.

Proof. If $\mathrm{f} \geq 0$, define

$$
E_{n, i}=\left\{x \left\lvert\, \frac{i-1}{2^{n}} \leq f(x)<\frac{i}{2^{n}}\right.\right\}, \quad F_{n}=\{x \mid f(x) \geq n\}
$$

for $n=1,2,3, \ldots, i=1,2, \ldots, n \cdot 2^{n}$. Put

$$
s_{n}=\sum_{i=1}^{n \cdot 2^{n}} \frac{i-1}{2^{n}} K_{E_{n, i}}+n K_{F_{n}}
$$

In the general case, let $f=f^{+}-f^{-}$and apply the preceding construction to $f^{+}$and $\mathrm{f}^{-}$.

It may be noted that the sequence $\left(s_{n}\right)$ given by (11.50) converges uniformly to f if f is bounded.

# INTEGRATION 

We shall define integration on a measurable space $X$, in which $\mathfrak{M}$ is the $\sigma$-ring of measurable sets, and $\mu$ is the measure. The reader who wishes to visualize a more concrete situation may think of $X$ as the real line, or an interval, and of $\mu$ as the Lebesgue measure $m$.
11.21 Definition. Suppose

$$
s(x)=\sum_{i=1}^{n} c_{i} K_{E_{i}}(x) \quad\left(x \in X, c_{i}>0\right)
$$

is measurable, and suppose $E \in \mathfrak{M}$. We define

$$
I_{E}(s)=\sum_{i=1}^{n} c_{i} \mu\left(E \cap E_{i}\right)
$$

If $f$ is measurable and nonnegative, we define

$$
\int_{E} f d \mu=\sup I_{E}(s)
$$

where the sup is taken over all measurable simple functions $s$ such that $0 \leq s \leq f$.
The left member of (11.53) is called the Lebesgue integral of $f$, with respect to the measure $\mu$, over the set $E$. It should be noted that the integral may have the value $+\infty$.

It is easily verified that

$$
\int_{E} s d \mu=I_{E}(s)
$$

for every nonnegative simple measurable function $s$.
11.22 Definition. Let $f$ be measurable and consider the two integrals

$$
\int_{E} f^{+} \mathrm{d} \mu, \quad \int_{E} f^{-} \mathrm{d} \mu
$$

where $f^{+}$and $f^{-}$are defined as in (11.47). If at least one of the integrals (11.55) is finite, we define

$$
\int_{E} f d \mu=\int_{E} f^{+} d \mu-\int_{E} f^{-} d \mu
$$

If both integrals in (11.55) are finite, then (11.56) is finite, and we say that $f$ is integrable (or summable) on $E$ in the Lebesgue sense, with respect to $\mu$; we write $f \in \mathscr{L}(\mu)$ on $E$. If $\mu=m$, the usual notation is $f \in \mathscr{L}$ on $E$.

This terminology may be a little confusing: If (11.56) is $+\infty$ or $-\infty$, then the integral of $f$ over $E$ is defined, although $f$ is not integrable in the above sense of the word; $f$ is integrable on $E$ if and only if its integral over $E$ is finite.

We shall mainly be interested in integrable functions, although in some cases it is desirable to deal with the more general situation.
11.23 Remarks. The following properties are evident
(a) If $f$ is measurable and bounded on $E$, and if $\mu(E)<+\infty$, then $f \in \mathscr{L}(\mu)$ on $E$.
(b) If $a \leq f(x) \leq b$ for $x \in E$, and $\mu(E)<+\infty$, then

$$
a \mu(E) \leq \int_{E} f d \mu \leq b \mu(E)
$$

(c) If $f$ and $g \in \mathscr{L}(\mu)$ on $E$, and if $f(x) \leq g(x)$ for $x \in E$, then

$$
\int_{E} f d \mu \leq \int_{E} g d \mu
$$

(d) If $f \in \mathscr{L}(\mu)$ on $E$, then $c f \in \mathscr{L}(\mu)$ on $E$ for every finite constant $c$, and

$$
\int_{E} c f d \mu=c \int_{E} f d \mu
$$

(e) If $\mu(E)=0$ and $f$ is measurable, then

$$
\int_{E} f d \mu=0
$$

(f) If $f \in \mathscr{L}(\mu)$ on $E, A \in \mathfrak{M}$, and $A \subset E$, then $f \in \mathscr{L}(\mu)$ on $A$.

# 11.24 Theorem. 

(a) Suppose f is measurable and nonnegative on X . For $\mathrm{A} \in \mathfrak{M}$, define

$$
\phi(\mathrm{A})=\int_{\mathrm{A}} \mathrm{f} \mathrm{~d} \mu
$$

Then $\phi$ is countably additive on $\mathfrak{M}$.
(b) The same conclusion holds if $\mathrm{f} \in \mathscr{L}(\mu)$ on X .

Proof. It is clear that (b) follows from (a) if we write $f=f^{+}-f^{-}$and apply (a) to $\mathrm{f}^{+}$and $\mathrm{f}^{-}$.

To prove (a), we have to show that

$$
\phi(A)=\sum_{n=1}^{\infty} \phi\left(A_{n}\right)
$$

if $A_{n} \in \mathfrak{M}(n=1,2,3, \ldots), A_{i} \cap A_{j}=0$ for $i \neq j$, and $A=\bigcup_{n=1}^{\infty} A_{n}$.
If $f$ is a characteristic function, then the countable additivity of $\phi$ is precisely the same as the countable additivity of $\mu$, since

$$
\int_{A} K_{E} d \mu=\mu(A \cap E)
$$

If $f$ is simple, then $f$ is of the form (11.51), and the conclusion again holds.
In the general case, we have, for every measurable simple function $s$ such that $0 \leq s \leq f$,

$$
\int_{A} s d \mu=\sum_{n=1}^{\infty} \int_{A_{n}} s d \mu \leq \sum_{n=1}^{\infty} \phi\left(A_{n}\right)
$$

Therefore, by (11.53),

$$
\phi(A) \leq \sum_{n=1}^{\infty} \phi\left(A_{n}\right)
$$

Now if $\phi\left(A_{n}\right)=+\infty$ for some $n$, (11.58) is trivial, since $\phi(A) \geq \phi\left(A_{n}\right)$. Suppose $\phi\left(A_{n}\right)<+\infty$ for every $n$.

Given $\varepsilon>0$, we can choose a measurable function $s$ such that $0 \leq \mathrm{s} \leq \mathrm{f}$, and such that

$$
\int_{A_{1}} s d \mu \geq \int_{A_{1}} f d \mu-\varepsilon, \quad \int_{A_{2}} s d \mu \geq \int_{A_{2}} f d \mu-\varepsilon
$$

Hence

$$
\phi\left(A_{1} \cup A_{2}\right) \geq \int_{A_{1} \cup A_{2}} s d \mu=\int_{A_{1}} s d \mu+\int_{A_{2}} s d \mu \geq \phi\left(A_{1}\right)+\phi\left(A_{2}\right)-2 \varepsilon
$$

so that

$$
\phi\left(A_{1} \cup A_{2}\right) \geq \phi\left(A_{1}\right)+\phi\left(A_{2}\right)
$$

It follows that we have, for every n ,

$$
\phi\left(A_{1} \cup \cdots \cup A_{n}\right) \geq \phi\left(A_{1}\right)+\cdots+\phi\left(A_{n}\right)
$$

Since $A \supset A_{1} \cup \cdots \cup A_{n}$, (11.61) implies

$$
\phi(A) \geq \sum_{n=1}^{\infty} \phi\left(A_{n}\right)
$$

and (11.58) follows from (11.59) and (11.62).
Corollary. If $A \in \mathfrak{M}, B \in \mathfrak{M}, B \subset A$, and $\mu(A-B)=0$, then

$$
\int_{A} f d \mu=\int_{B} f d \mu
$$

Since $A=B \cup(A-B)$, this follows from Remark 11.23(e).
11.25 Remarks. The preceding corollary shows that sets of measure zero are negligible in integration.

Let us write $f \sim g$ on $E$ if the set

$$
\{x \mid f(x) \neq g(x)\} \cap E
$$

has measure zero. Then $f \sim f ; f \sim g$ implies $g \sim f$; and $f \sim g, g \sim h$ implies $f \sim h$. That is, the relation $\sim$ is an equivalence relation.

If $\mathrm{f} \sim \mathrm{g}$ on E , we clearly have

$$
\int_{A} f d \mu=\int_{A} g d \mu
$$

provided the integrals exist, for every measurable subset $A$ of $E$.
If a property P holds for every $\mathrm{x} \in \mathrm{E}-\mathrm{A}$, and if $\mu(\mathrm{A})=0$, it is customary to say that P holds for almost all $\mathrm{x} \in \mathrm{E}$, or that P holds almost everywhere on E . (This concept of "almost everywhere" depends of course on the particular measure under consideration. In the literature, unless something is said to the contrary, it usually refers to the Lebesgue measure.)

If $f \in \mathscr{L}(\mu)$ on $E$, it is clear that $f(x)$ must be finite almost everywhere on E. In most cases, we therefore do not lose any generality if we assume the given functions to be finite-valued from the outset.
11.26 Theorem. If $\mathrm{f} \in \mathscr{L}(\mu)$ on E , then $|\mathrm{f}| \in \mathscr{L}(\mu)$ on E , and

$$
\left|\int_{E} f d \mu\right| \leq \int_{E}|f| d \mu
$$

Proof. Write $E=A \cup B$, where $f(x) \geq 0$ on $A$ and $f(x)<0$ on $B$. By Theorem 11.24,

$$
\int_{E}|f| d \mu=\int_{A}|f| d \mu+\int_{B}|f| d \mu=\int_{A} f^{+} d \mu+\int_{B} f^{-} d \mu<\infty
$$

so that $|f| \in \mathscr{L}(\mu)$. Since $f \leq|f|$ and $-f \leq|f|$, we see that

$$
\int_{E} f d \mu \leq \int_{E}|f| d \mu, \quad-\int_{E} f d \mu \leq \int_{E}|f| d \mu
$$

and (11.63) follows.
Since the integrability of $f$ implies that of $|f|$, the Lebesgue integral is often called an absolutely convergent integral. It is of course possible to define nonabsolutely convergent integrals, and in the treatment of some problems it is essential to do so. But these integrals lack some of the most useful properties of the Lebesgue integral and play a somewhat less important role in analysis.
11.27 Theorem. Suppose f is measurable on $\mathrm{E},|\mathrm{f}| \leq \mathrm{g}$, and $\mathrm{g} \in \mathscr{L}(\mu)$ on E . Then $\mathrm{f} \in \mathscr{L}(\mu)$ on E .

Proof. We have $\mathrm{f}^{+} \leq \mathrm{g}$ and $\mathrm{f}^{-} \leq \mathrm{g}$.
11.28 Theorem (Lebesgue's Monotone Convergence Theorem). Suppose $\mathrm{E} \in \mathfrak{M}$. Let $\left(f_{n}\right)$ be a sequence of measurable functions such that

$$
0 \leq f_{1}(x) \leq f_{2}(x) \leq \cdots \quad(x \in E)
$$

Let f be defined by

$$
\mathrm{f}_{\mathrm{n}}(\mathrm{x}) \rightarrow \mathrm{f}(\mathrm{x}) \quad(\mathrm{x} \in \mathrm{E})
$$

as $\mathrm{n} \rightarrow \infty$. Then

$$
\int_{E} f_{n} d \mu \underset{n \rightarrow \infty}{\longrightarrow} \int_{E} f d \mu
$$

Proof. By (11.64), it is clear that, as $\mathrm{n} \rightarrow \infty$,

$$
\int_{E} f_{n} d \mu \rightarrow \alpha
$$

for some $\alpha$; since $\int f_{n} \leq \int f$, we have

$$
\alpha \leq \int_{E} f d \mu
$$

Choose c such that $0<c<1$ and let $s$ be a simple measurable function such that $0 \leq \mathrm{s} \leq \mathrm{f}$. Put

$$
E_{n}=\left\{x \mid f_{n}(x) \geq c s(x)\right\} \quad(n=1,2,3, \ldots)
$$

By (11.64), $\mathrm{E}_{1} \subset \mathrm{E}_{2} \subset \mathrm{E}_{3} \subset \cdots$; by (11.65)

$$
E=\bigcup_{n=1}^{\infty} E_{n}
$$

For every n ,

$$
\int_{E} f_{n} d \mu \geq \int_{E_{n}} f_{n} d \mu \geq c \int_{E_{n}} s d \mu
$$

We let $\mathrm{n} \rightarrow \infty$ in (11.70). Since the integral is a countably additive set function (Theorem 11.24), (11.69) shows that we may apply Theorem 11.3 to the last integral in (11.70) and we obtain

$$
\alpha \geq c \int_{E} s d \mu
$$

Letting $\mathrm{c} \rightarrow 1$, we see that

$$
\alpha \geq \int_{E} s d \mu
$$

and (11.53) implies

$$
\alpha \geq \int_{E} f d \mu
$$

The theorem follows from (11.67), (11.68), and (11.72).
11.29 Theorem. Suppose $\mathrm{f}=\mathrm{f}_{1}+\mathrm{f}_{2}$, where $\mathrm{f}_{\mathrm{i}} \in \mathscr{L}(\mu)$ on $\mathrm{E}(\mathrm{i}=1,2)$. Then $\mathrm{f} \in \mathscr{L}(\mu)$ on E , and

$$
\int_{\mathrm{E}} \mathrm{f} \mathrm{~d} \mu=\int_{\mathrm{E}} \mathrm{f}_{1} \mathrm{~d} \mu+\int_{\mathrm{E}} \mathrm{f}_{2} \mathrm{~d} \mu
$$

Proof. First, suppose $f_{1} \geq 0, f_{2} \geq 0$. If $f_{1}$ and $f_{2}$ are simple, (11.73) follows trivially from (11.52) and (11.54). Otherwise, choose monotonically increasing sequences $\left(s_{n}^{\prime}\right),\left(s_{n}^{\prime \prime}\right)$ of nonnegative measurable simple functions which converge to $f_{1}, f_{2}$. Theorem 11.20 shows that this is possible. Put $s_{n}=s_{n}^{\prime}+s_{n}^{\prime \prime}$. Then

$$
\int_{\mathrm{E}} s_{n} \mathrm{~d} \mu=\int_{\mathrm{E}} s_{n}^{\prime} \mathrm{d} \mu+\int_{\mathrm{E}} s_{n}^{\prime \prime} \mathrm{d} \mu
$$

and (11.73) follows if we let $\mathrm{n} \rightarrow \infty$ and appeal to Theorem 11.28.
Next, suppose $f_{1} \geq 0, f_{2} \leq 0$. Put

$$
A=\{x \mid f(x) \geq 0\}, \quad B=\{x \mid f(x)<0\}
$$

Then $f, f_{1}$, and $-f_{2}$ are nonnegative on $A$. Hence

$$
\int_{A} f_{1} d \mu=\int_{A} f d \mu+\int_{A}\left(-f_{2}\right) d \mu=\int_{A} f d \mu-\int_{A} f_{2} d \mu
$$

Similarly, $-f, f_{1}$, and $-f_{2}$ are nonnegative on $B$, so that

$$
\int_{B}\left(-f_{2}\right) d \mu=\int_{B} f_{1} d \mu+\int_{B}(-f) d \mu
$$

or

$$
\int_{B} f_{1} d \mu=\int_{B} f d \mu-\int_{B} f_{2} d \mu
$$

and (11.73) follows if we add (11.74) and (11.75).
In the general case, E can be decomposed into four sets $\mathrm{E}_{\mathrm{i}}$ on each of which $f_{1}(x)$ and $f_{2}(x)$ are of constant sign. These two cases we have proved so far imply

$$
\int_{E_{i}} f d \mu=\int_{E_{i}} f_{1} d \mu+\int_{E_{i}} f_{2} d \mu \quad(i=1,2,3,4)
$$

and (11.73) follows by adding these four equations.
We are now in a position to reformulate Theorem 11.28 for series.

11.30 Theorem. Suppose $\mathrm{E} \in \mathfrak{M}$. If $\left(\mathrm{f}_{\mathrm{n}}\right)$ is a sequence of nonnegative measurable functions and

$$
f(x)=\sum_{n=1}^{\infty} f_{n}(x) \quad(x \in E)
$$

then

$$
\int_{E} f d \mu=\sum_{n=1}^{\infty} \int_{E} f_{n} d \mu
$$

Proof. The partial sums of (11.76) form a monotonically increasing sequence.
11.31 Theorem (Fatou's Theorem). Suppose $\mathrm{E} \in \mathfrak{M}$. If $\left(\mathrm{f}_{\mathrm{n}}\right)$ is a sequence of nonnegative measurable functions and

$$
f(x)=\liminf _{n \rightarrow \infty} f_{n}(x) \quad(x \in E)
$$

then

$$
\int_{E} f d \mu \leq \liminf _{n \rightarrow \infty} \int_{E} f_{n} d \mu
$$

Strict inequality may hold in (11.77). An example is given in Exercise 11.5.
Proof. For $n=1,2,3, \ldots$ and $x \in E$, put

$$
g_{n}(x)=\inf f_{i}(x) \quad(i \geq n)
$$

Then $g_{n}$ is measurable on $E$, and

$$
\begin{gathered}
0 \leq g_{1}(x) \leq g_{2}(x) \leq \cdots \\
g_{n}(x) \leq f_{n}(x) \\
g_{n}(x) \rightarrow f(x) \quad(n \rightarrow \infty)
\end{gathered}
$$

By (11.78), (11.80), and Theorem 11.28,

$$
\int_{E} g_{n} d \mu \rightarrow \int_{E} f d \mu
$$

so that (11.77) follows from (11.79) and (11.81).
11.32 Theorem (Lebesgue's Dominated Convergence Theorem). Suppose $\mathrm{E} \in \mathfrak{M}$. Let $\left(f_{n}\right)$ be a sequence of measurable functions such that

$$
f_{n}(x) \rightarrow f(x) \quad(x \in E)
$$

as $n \rightarrow \infty$. If there exists a function $g \in \mathscr{L}(\mu)$ on $E$ such that

$$
\left|f_{n}(x)\right| \leq g(x) \quad(n=1,2,3, \ldots, x \in E)
$$

then

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu=\int_{E} f d \mu
$$

Because of (11.83), $\left(f_{n}\right)$ is said to be dominated by $g$, and we talk about dominated convergence. By Remark 11.25, the conclusion is the same if (11.82) holds almost everywhere on $E$.

Proof. First, (11.83) and Theorem 11.27 imply that $f_{n} \in \mathscr{L}(\mu)$ and $f \in \mathscr{L}(\mu)$ on $E$. Since $f_{n}+g \geq 0$, Fatou's theorem shows that

$$
\int_{E}(f+g) d \mu \leq \liminf _{n \rightarrow \infty} \int_{E}\left(f_{n}+g\right) d \mu
$$

or

$$
\int_{E} f d \mu \leq \liminf _{n \rightarrow \infty} \int_{E} f_{n} d \mu
$$

Since $g-f_{n} \geq 0$, we see similarly that

$$
\int_{E}(g-f) d \mu \leq \liminf _{n \rightarrow \infty} \int_{E}\left(g-f_{n}\right) d \mu
$$

so that

$$
-\int_{E} f d \mu \leq \liminf _{n \rightarrow \infty}\left[-\int_{E} f_{n} d \mu\right]
$$

which is the same as

$$
\int_{E} f d \mu \geq \limsup _{n \rightarrow \infty} \int_{E} f d \mu
$$

The existence of the limit in (11.84) and the equality asserted by (11.84) now follow from (11.85) and (11.86).

Corollary. If $\mu(\mathrm{E})<+\infty,\left(\mathrm{f}_{\mathrm{n}}\right)$ is uniformly bounded on E , and $\mathrm{f}_{\mathrm{n}}(\mathrm{x}) \rightarrow \mathrm{f}(\mathrm{x})$ on E , then (11.84) holds.

# COMPARISON WITH THE RIEMANN INTEGRAL 

Our next theorem will show that every function which is Riemann-integrable on an interval is also Lebesgue-integrable, and that the Riemann-integrable functions are subject to rather stringent continuity conditions. Quite apart from the fact that the Lebesgue theory therefore enables us to integrate a much larger class of functions, its greatest advantage lies perhaps in the ease with which many limit operations can be handled; from this point of view, Lebesgue's convergence theorems may well be regarded as the core of the Lebesgue theory.

One of the difficulties which is encountered in the Riemann theory is that limits of Riemann-integrable functions (or even continuous functions) may fail to be Riemann-integrable. This difficulty is now almost eliminated, since limits of measurable functions are always measurable.

Let the measure space $X$ be the interval $[a, b]$ of the real line, with $\mu=m$ (the Lebesgue measure), and $\mathfrak{M}$ be the family of Lebesgue-measurable subsets of $[a, b]$. Instead of

$$
\int_{X} \mathrm{f} d \mathrm{~m}
$$

it is customary to use the familiar notation

$$
\int_{a}^{b} f d x
$$

for the Lebesgue integral of $f$ over $[a, b]$. To distinguish Riemann integrals from Lebesgue integrals, we shall now denote the former by

$$
\mathscr{R} \int_{a}^{b} f d x
$$

# 11.33 Theorem. 

(a) If $\mathrm{f} \in \mathscr{R}$ on $[\mathrm{a}, \mathrm{b}]$, then $\mathrm{f} \in \mathscr{L}$ on $[\mathrm{a}, \mathrm{b}]$, and

$$
\int_{a}^{b} f d x=\mathscr{R} \int_{a}^{b} f d x
$$

(b) Suppose f is bounded on $[a, b]$. Then $f \in \mathscr{R}$ on $[a, b]$ if and only if f is continuous almost everywhere on $[a, b]$.

Proof. Suppose f is bounded. By Definition 6.1 and Theorem 6.4, there is a sequence $\left\{P_{k}\right\}$ of partitions of $[a, b]$ such that $P_{k+1}$ is a refinement of $P_{k}$, the distance between adjacent points of $\mathrm{P}_{\mathrm{k}}$ is less than $1 / \mathrm{k}$, and

$$
\lim _{k \rightarrow \infty} L\left(P_{k}, f\right)=\mathscr{R} \int_{f} f d x, \quad \lim _{k \rightarrow \infty} U\left(P_{k}, f\right)=\mathscr{R} \int_{f} f d x
$$

(In this proof, all integrals are taken over $[a, b]$.)
If $P_{k}=\left\{x_{0}, x_{1}, \ldots, x_{n}\right\}$, with $x_{0}=a, x_{n}=b$, define

$$
U_{k}(a)=L_{k}(a)=f(a)
$$

put $U_{k}(x)=M_{i}$ and $L_{k}(x)=m_{i}$ for $x_{i-1}<x \leq x_{i}, 1 \leq i \leq n$, using the notation introduced in Definition 6.1. Then

$$
L\left(P_{k}, f\right)=\int L_{k} d x, \quad U\left(P_{k}, f\right)=\int U_{k} d x
$$

and

$$
L_{1}(x) \leq L_{2}(x) \leq \cdots \leq f(x) \leq \cdots \leq U_{2}(x) \leq U_{1}(x)
$$

for all $x \in[a, b]$, since $P_{k+1}$ refines $P_{k}$. By (11.90), there exist

$$
L(x)=\lim _{k \rightarrow \infty} L_{k}(x), \quad U(x)=\lim _{k \rightarrow \infty} U_{k}(x)
$$

Observe that $L$ and $U$ are bounded measurable functions on $[a, b]$, that

$$
L(x) \leq f(x) \leq U(x) \quad(a \leq x \leq b)
$$

and that

$$
\int \mathrm{Ldx}=\mathscr{R} \int \mathrm{fdx}, \quad \int \mathrm{Udx}=\mathscr{R} \int \mathrm{fdx}
$$

by (11.88), (11.90), and the monotone convergence theorem.
So far, nothing has been assumed about $f$ except that $f$ is a bounded real function on $[a, b]$.

To complete the proof, note that $f \in \mathscr{R}$ if and only if its upper and lower Riemann integrals are equal, hence if and only if

$$
\int \mathrm{Ldx}=\int \mathrm{Udx}
$$

Since $L \leq U$, (11.94) happens if and only if $L(x)=U(x)$ for almost all $x \in[a, b]$ (Exercise 11.1). In that case, (11.92) implies that

$$
L(x)=f(x)=U(x)
$$

almost everywhere on $[a, b]$, so that $f$ is measurable, and (11.87) follows from (11.93) and (11.95).

Furthermore, if $x$ belongs to no $P_{k}$, it is quite easy to see that $U(x)=L(x)$ if and only if $f$ is continuous at $x$. Since the union of the sets $P_{k}$ is countable, its measure is 0 , and we conclude that $f$ is continuous almost everywhere on $[a, b]$ if and only if $L(x)=U(x)$ almost everywhere, hence (as we saw above) if and only if $f \in \mathscr{R}$. This completes the proof.

The familiar connection between integration and differentiation is to a large degree carried over into the Lebesgue theory. If $f \in \mathscr{L}$ on $[a, b]$ and

$$
F(x)=\int_{a}^{x} f d t \quad(a \leq x \leq b)
$$

then $F^{\prime}(x)=f(x)$ almost everywhere on $[a, b]$.
Conversely, if $F$ is differentiable at every point of $[a, b]$ ("almost everywhere" is

not good enough here!) and if $F^{\prime} \in \mathscr{L}$ on $[a, b]$, then

$$
F(x)-F(a)=\int_{a}^{x} F^{\prime}(t) d t \quad(a \leq x \leq b)
$$

For the proofs of these two theorems, we refer the reader to any of the works on integration cited in the Bibliography.

# INTEGRATION OF COMPLEX FUNCTIONS 

Suppose f is a complex-valued function defined on a measure space X , and $\mathrm{f}=$ $\mathrm{u}+\mathrm{i} v$, where u and v are real. We say that f is measurable if and only if both u and $v$ are measurable.

It is easy to verify that sums and products of complex measurable functions are again measurable. Since

$$
|f|=\left(u^{2}+v^{2}\right)^{1 / 2}
$$

Theorem 11.18 shows that $|f|$ is measurable for every complex measurable $f$.
Suppose $\mu$ is a measure on $X, E$ is a measurable subset of $X$, and $f$ is a complex function on X . We say that $\mathrm{f} \in \mathscr{L}(\mu)$ on E provided that f is measurable and

$$
\int_{E}|f| d \mu<+\infty
$$

and we define

$$
\int_{E} f d \mu=\int_{E} u d \mu+i \int_{E} v d \mu
$$

if (11.97) holds. Since $|u| \leq|f|,|v| \leq|f|$, and $|f| \leq|u|+|v|$, it is clear that (11.97) holds if and only if $u \in \mathscr{L}(\mu)$ and $v \in \mathscr{L}(\mu)$ on $E$.

Theorems 11.23(a), (d), (e), (f), 11.24(b), 11.26, 11.27, 11.29, and 11.32 can now be extended to Lebesgue integrals of complex functions. The proofs are quite straightforward. That of Theorem 11.26 is the only one that offers anything of interest:

If $f \in \mathscr{L}(\mu)$ on $E$, there is a complex number $c,|c|=1$, such that

$$
c \int_{E} f d \mu \geq 0
$$

Put $g=c f=u+i v, u$ and $v$ real. Then

$$
\left|\int_{E} f d \mu\right|=c \int_{E} f d \mu=\int_{E} g d \mu=\int_{E} u d \mu \leq \int_{E}|f| d \mu
$$

The third of the above equalities holds since the preceding ones show that $\int g d \mu$ is real.

# FUNCTIONS OF CLASS $\mathscr{L}^{2}$ 

As an application of the Lebesgue theory, we shall now extend the Parseval theorem (which we proved only for Riemann-integrable functions in Chap. 8) and prove the Riesz-Fischer theorem for orthonormal sets of functions.
11.34 Definition. Let X be a measurable space. We say that a complex function $\mathrm{f} \in \mathscr{L}^{2}(\mu)$ on X is measurable if

$$
\int_{X}|f|^{2} d \mu<+\infty
$$

If $\mu$ is Lebesgue measure, we say $f \in \mathscr{L}^{2}$. For $f \in \mathscr{L}^{2}(\mu)$ (we shall omit the phrase "on X" from now on) we define

$$
\|f\|=\left\{\int_{X}|f|^{2} d \mu\right\}^{1 / 2}
$$

and call $\|f\|$ the $\mathscr{L}^{2}(\mu)$ norm of $f$.
11.35 Theorem. Suppose $\mathrm{f} \in \mathscr{L}^{2}(\mu)$ and $\mathrm{g} \in \mathscr{L}^{2}(\mu)$. Then $\mathrm{fg} \in \mathscr{L}(\mu)$ and

$$
\int_{X}|f g| d \mu \leq\|f\|\|g\|
$$

This is the Schwarz inequality, which we have already encountered for series and for Riemann integrals. It follows from the inequality

$$
0 \leq \int_{X}(|f|+\lambda|g|)^{2} d \mu=\|f\|^{2}+2 \lambda \int_{X}|f g| d \mu+\lambda^{2}\|g\|^{2}
$$

which holds for every real $\lambda$.
11.36 Theorem. If $\mathrm{f} \in \mathscr{L}^{2}(\mu)$ and $\mathrm{g} \in \mathscr{L}^{2}(\mu)$, then $\mathrm{f}+\mathrm{g} \in \mathscr{L}^{2}(\mu)$ and

$$
\|f+g\| \leq\|f\|+\|g\|
$$

Proof. The Schwarz inequality shows that

$$
\begin{aligned}
\|f+g\|^{2} & =\int|f|^{2}+\int f \bar{g}+\int \bar{f} g+\int|g|^{2} \\
& \leq\|f\|^{2}+2\|f\|\|g\|+\|g\|^{2} \\
& =(\|f\|+\|g\|)^{2}
\end{aligned}
$$

11.37 Remark. If we define the distance between two functions $f$ and $g$ in $\mathscr{L}^{2}(\mu)$ to be $\|f-g\|$, we see that the conditions of Definition 2.15 are satisfied, except for the fact that $\|f-g\|=0$ does not imply that $f(x)=g(x)$ for all $x$, but only for almost all x . Thus, if we identify functions which differ only on a set of measure zero, $\mathscr{L}^{2}(\mu)$ is a metric space.

We now consider $\mathscr{L}^{2}$ on an interval of the real line, with respect to Lebesgue measure.
11.38 Theorem. The continuous functions form a dense subset of $\mathscr{L}^{2}$ on $[a, b]$.

More explicitly, this means that for any $f \in \mathscr{L}^{2}$ on $[a, b]$, and any $\varepsilon>0$, there is a function $g$, continuous on $[a, b]$, such that

$$
\|f-g\|=\left\{\int_{a}^{b}|f-g|^{2} d x\right\}^{1 / 2}<\varepsilon
$$

Proof. We shall say that $f$ is approximated in $\mathscr{L}^{2}$ by a sequence $\left\{g_{n}\right\}$ if $\left\|f-g_{n}\right\| \rightarrow$ 0 as $n \rightarrow \infty$.

Let $A$ be a closed subset of $[a, b]$ and $K_{A}$ its characteristic function. Put

$$
t(x)=\inf |x-y| \quad(y \in A)
$$

and

$$
g_{n}(x)=\frac{1}{1+n t(x)} \quad(n=1,2,3, \ldots)
$$

Then $g_{n}$ is continuous on $[a, b], g_{n}(x)=1$ on $A$, and $g_{n}(x) \rightarrow 0$ on $B$, where $B=[a, b]-A$. Hence

$$
\left\|g_{n}-K_{A}\right\|=\left\{\int_{B} g_{n}^{2} d x\right\}^{1 / 2} \rightarrow 0
$$

by Theorem 11.32. Thus characteristic functions of closed sets can be approximated in $\mathscr{L}^{2}$ by continuous functions.

By (11.39), the same is true for the characteristic functions of any measurable set, and hence also for simple measurable functions.

If $f \geq 0$ and $f \in \mathscr{L}^{2}$, let $\left\{s_{n}\right\}$ be a monotonically increasing sequence of simple nonnegative measurable functions such that $s_{n}(x) \rightarrow f(x)$. Since $\left|f-s_{n}\right|^{2} \leq f^{2}$, Theorem 11.32 shows that $\left\|f-s_{n}\right\| \rightarrow 0$. The general case follows.
11.39 Definition. We say that a sequence of complex functions $\left(\phi_{n}\right)$ is an orthonormal set of functions on a measurable space $X$ if

$$
\int_{X} \phi_{n} \bar{\phi}_{m} d \mu= \begin{cases}0 & (n \neq m) \\ 1 & (n=m)\end{cases}
$$

In particular, we must have $\phi_{n} \in \mathscr{L}^{2}(\mu)$. If $f \in \mathscr{L}^{2}(\mu)$ and if

$$
c_{n}=\int_{X} f \bar{\phi}_{n} d \mu \quad(n=1,2,3, \ldots)
$$

we write

$$
\mathrm{f} \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}
$$

as in Definition 8.10.
The definition of a trigonometric Fourier series is extended in the same way to $\mathscr{L}^{2}$ (or even to $\mathscr{L}$ ) on $[-\pi, \pi]$. Theorem 8.11 and Theorem 8.12 (the Bessel inequality) hold for any $\mathrm{f} \in \mathscr{L}^{2}(\mu)$. The proofs are the same, word for word.

We can now prove the Parseval theorem.
11.40 Theorem. Suppose

$$
f(x) \sim \sum_{n=-\infty}^{\infty} c_{n} e^{i n x}
$$

where $\mathrm{f} \in \mathscr{L}^{2}$ on $[-\pi, \pi]$. Let $s_{n}$ be the nth partial sum of (11.99). Then

$$
\begin{aligned}
\lim _{n \rightarrow \infty}\left\|f-s_{n}\right\| & =0 \\
\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2} & =\frac{1}{2 \pi} \int_{-\pi}^{\pi}|f|^{2} d x
\end{aligned}
$$

Proof. Let $\varepsilon>0$ be given. By Theorem 11.38, there is a continuous function $g$ such that

$$
\|f-g\|<\frac{\varepsilon}{2}
$$

Moreover, it is easy to see that we can arrange it so that $g(\pi)=g(-\pi)$. Then $g$ can be extended to a periodic continuous function. By Theorem 8.16, there is a trigonometric polynomial T , of degree N , say, such that

$$
\|g-T\|<\frac{\varepsilon}{2}
$$

Hence, by Theorem 8.11 (extended to $\mathscr{L}^{2}$ ), $\mathrm{n} \geq \mathrm{N}$ implies

$$
\left\|s_{n}-f\right\| \leq\|T-f\|<\varepsilon
$$

and (11.100) follows. Equation (11.101) is deduced from (11.100) as in the proof of Theorem 8.16.

Corollary. If $\mathrm{f} \in \mathscr{L}^{2}$ on $[-\pi, \pi]$, and if

$$
\int_{-\pi}^{\pi} f(x) e^{-i n x} d x=0 \quad(n=0, \pm 1, \pm 2, \ldots)
$$

then $\|f\|=0$.
Thus if two functions in $\mathscr{L}^{2}$ have the same Fourier series, they differ at most on a set of measure zero.

11.41 Definition. Let $f$ and $f_{n} \in \mathscr{L}^{2}(\mu)(n=1,2,3, \ldots)$. We say that $\left(f_{n}\right)$ converges to $f$ in $\mathscr{L}^{2}(\mu)$ if $\left\|f_{n}-f\right\| \rightarrow 0$. We say that $\left(f_{n}\right)$ is a Cauchy sequence in $\mathscr{L}^{2}(\mu)$ if for every $\varepsilon>0$ there is an integer N such that $\mathrm{n} \geq \mathrm{N}, \mathrm{m} \geq \mathrm{N}$ implies $\left\|f_{n}-f_{m}\right\| \leq \varepsilon$.
11.42 Theorem. If $\left(f_{n}\right)$ is a Cauchy sequence in $\mathscr{L}^{2}(\mu)$, then there exists a function $f \in \mathscr{L}^{2}(\mu)$ such that $\left(f_{n}\right)$ converges to $f$ in $\mathscr{L}^{2}(\mu)$.

This says, in other words, that $\mathscr{L}^{2}(\mu)$ is a complete metric space.
Proof. Since $\left(f_{n}\right)$ is a Cauchy sequence, we can find a sequence $\left(n_{k}\right), k=1,2,3, \ldots$ such that

$$
\left\|f_{n_{k}}-f_{n_{k+1}}\right\|<\frac{1}{2^{k}} \quad(k=1,2,3, \ldots)
$$

Choose a function $g \in \mathscr{L}^{2}(\mu)$. By the Schwarz inequality,

$$
\int_{X}\left|g\left(f_{n_{k}}-f_{n_{k+1}}\right)\right| d \mu \leq \frac{\|g\|}{2^{k}}
$$

Hence

$$
\sum_{k=1}^{\infty} \int_{X}\left|g\left(f_{n_{k}}-f_{n_{k+1}}\right)\right| d \mu \leq\|g\|
$$

By Theorem 11.30, we may interchange the summation and integration in (11.102). It follows that

$$
|g(x)| \sum_{k=1}^{\infty}\left|f_{n_{k}}(x)-f_{n_{k+1}}(x)\right|<+\infty
$$

almost everywhere on $X$. Therefore

$$
\sum_{k=1}^{\infty}\left|f_{n_{k+1}}(x)-f_{n_{k}}(x)\right|<+\infty
$$

almost everywhere on $X$. For if the series in (11.104) were divergent on a set $E$ of positive measure, we could take $g(x)$ to be nonzero on a subset of $E$ of positive measure, thus obtaining a contradiction to (11.103).

Since the kth partial sum of the series

$$
\sum_{k=1}^{\infty}\left(f_{n_{k+1}}(x)-f_{n_{k}}(x)\right)
$$

which converges almost everywhere on $X$, is

$$
f_{n_{k+1}}(x)-f_{n_{1}}(x)
$$

we see that the equation

$$
f(x)=\lim _{k \rightarrow \infty} f_{n_{k}}(x)
$$

defines $f(x)$ for almost all $x \in X$, and it does not matter how we define $f(x)$ at the remaining points of $X$.

We shall now show that this function $f$ has the desired properties. Let $\varepsilon>0$ be given and choose N as indicated in Definition 11.41. If $n_{k}>N$, Fatou's theorem shows that

$$
\left\|f-f_{n_{k}}\right\|<\liminf _{i \rightarrow \infty}\left\|f_{n_{i}}-f_{n_{k}}\right\| \leq \varepsilon
$$

Thus $f-f_{n_{k}} \in \mathscr{L}^{2}(\mu)$, and since $f=\left(f-f_{n_{k}}\right)+f_{n_{k}}$, we see that $f \in \mathscr{L}^{2}(\mu)$. Also, since $\varepsilon$ is arbitrary,

$$
\lim _{k \rightarrow \infty}\left\|f-f_{n_{k}}\right\|=0
$$

Finally, the inequality

$$
\left\|f-f_{n}\right\| \leq\left\|f-f_{n_{k}}\right\|+\left\|f_{n_{k}}-f_{n}\right\|
$$

shows that $\left(f_{n}\right)$ converges to $f$ in $\mathscr{L}^{2}(\mu)$; for if we take $n$ and $n_{k}$ large enough, each of the two terms on the right of (11.105) can be made arbitrarily small.
11.43 The Riesz-Fischer Theorem. Let $\left(\phi_{n}\right)$ be orthonormal on $X$. Suppose $\Sigma\left|c_{n}\right|^{2}$ converges, and put $s_{n}=c_{1} \phi_{1}+\cdots+c_{n} \phi_{n}$. Then there exists a function $f \in \mathscr{L}^{2}(\mu)$ such that $\left(s_{n}\right)$ converges to $f$ in $\mathscr{L}^{2}(\mu)$, and

$$
f \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}
$$

Proof. For $n>m$,

$$
\left\|s_{n}-s_{m}\right\|^{2}=\left|c_{m+1}\right|^{2}+\cdots+\left|c_{n}\right|^{2}
$$

so that $\left(s_{n}\right)$ is a Cauchy sequence in $\mathscr{L}^{2}(\mu)$. By Theorem 11.42, there is a function $f \in \mathscr{L}^{2}(\mu)$ such that

$$
\lim _{n \rightarrow \infty}\left\|f-s_{n}\right\|=0
$$

Now, for $n>k$,

$$
\int_{X} f \bar{\phi}_{k} d \mu-c_{k}=\int_{X} f \bar{\phi}_{k} d \mu-\int_{X} s_{n} \bar{\phi}_{k} d \mu
$$

so that

$$
\left|\int_{X} f \bar{\phi}_{k} d \mu-c_{k}\right| \leq\left\|f-s_{n}\right\| \cdot\left\|\phi_{k}\right\|+\left\|f-s_{n}\right\|
$$

Letting $n \rightarrow \infty$, we see that

$$
c_{k}=\int_{X} f \bar{\phi}_{k} d \mu \quad(k=1,2,3, \ldots)
$$

and the proof is complete.
11.44 Definition. An orthonormal set $\left(\phi_{n}\right)$ is said to be complete if, for $f \in \mathscr{L}^{2}(\mu)$, the equations

$$
\int_{X} f \bar{\phi}_{n} d \mu=0 \quad(n=1,2,3, \ldots)
$$

imply that $\|f\|=0$.
In the Corollary to Theorem 11.40 we deduced the completeness of the trigonometric system from the Parseval equation (11.101). Conversely, the Parseval equation holds for every complete orthonormal set:
11.45 Theorem. Let $\left(\phi_{n}\right)$ be a complete orthonormal set. If $f \in \mathscr{L}^{2}(\mu)$ and if

$$
f \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}
$$

then

$$
\int_{X}|f|^{2} d \mu=\sum_{n=1}^{\infty}\left|c_{n}\right|^{2}
$$

Proof. By the Bessel inequality, $\Sigma\left|c_{n}\right|^{2}$ converges. Putting

$$
s_{n}=c_{1} \phi_{1}+\cdots+c_{n} \phi_{n}
$$

The Riesz-Fischer theorem shows that there is a function $g \in \mathscr{L}^{2}(\mu)$ such that

$$
g \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}
$$

and such that $\left\|g-s_{n}\right\| \rightarrow 0$. Hence $\left\|s_{n}\right\| \rightarrow\|g\|$. Since

$$
\left\|s_{n}\right\|^{2}=\left|c_{1}\right|^{2}+\cdots+\left|c_{n}\right|^{2}
$$

we have

$$
\int_{X}|g|^{2} d \mu=\sum_{n=1}^{\infty}\left|c_{n}\right|^{2}
$$

Now (11.106), (11.108), and the completeness of $\left(\phi_{n}\right)$ show that $\|f-g\|=0$, so that (11.109) implies (11.107).

Combining Theorems 11.43 and 11.45, we arrive at the very interesting conclusion that every complete orthonormal set induces a 1-1 correspondence between the functions $f \in \mathscr{L}^{2}(\mu)$ (identifying those which are equal almost everywhere)

on the one hand and the sequences $\left(c_{n}\right)$ for which $\Sigma\left|c_{n}\right|^{2}$ converges, on the other. The representation

$$
f \sim \sum_{n=1}^{\infty} c_{n} \phi_{n}
$$

together with the Parseval equation, shows that $\mathscr{L}^{2}(\mu)$ may be regarded as an infinite-dimensional euclidean space (the so-called "Hilbert space"), in which the point $f$ has coordinates $c_{n}$ and the functions $\phi_{n}$ are the coordinate vectors.

# EXERCISES 

11.1. If $f \geq 0$ and $\int_{E} f d \mu=0$, prove that $f(x)=0$ almost everywhere on $E$. Hint: Let $E_{n}$ be the subset of $E$ on which $f(x)>1 / n$. Write $A=\bigcup E_{n}$. Then $\mu(A)=0$ if and only if $\mu\left(E_{n}\right)=0$ for every $n$.
11.2. If $\int_{A} f d \mu=0$ for every measurable subset $A$ of a measurable set $E$, then $f(x)=0$ almost everywhere on $E$.
11.3. If $\left(f_{n}\right)$ is a sequence of measurable functions, prove that the set of points $x$ at which $\left(f_{n}(x)\right)$ converges is measurable.
11.4. If $f \in \mathscr{L}(\mu)$ on $E$ and $g$ is bounded and measurable on $E$, prove that $f g \in \mathscr{L}(\mu)$ on $E$.
11.5. Put

$$
\begin{aligned}
g(x) & = \begin{cases}0 & (0 \leq x \leq \frac{1}{2}) \\
1 & \left(\frac{1}{2} \leq x \leq 1\right)\end{cases} \\
f_{2 k}(x) & =g(x) \quad(0 \leq x \leq 1) \\
f_{2 k+1}(x) & =g(1-x) \quad(0 \leq x \leq 1)
\end{aligned}
$$

Show that

$$
\liminf _{n \rightarrow \infty} f_{n}(x)=0 \quad(0 \leq x \leq 1)
$$

but

$$
\int_{0}^{1} f_{n}(x) d x=\frac{1}{2}
$$

[Compare with (11.77).]
11.6. Let

$$
f_{n}(x)= \begin{cases}\frac{1}{n} & (|x| \leq n) \\ 0 & (|x|>n)\end{cases}
$$

Then $f_{n}(x) \rightarrow 0$ uniformly on $\mathbb{R}^{1}$, but

$$
\int_{-\infty}^{\infty} f_{n} d x=2 \quad(n=1,2,3, \ldots)
$$

(We write $\int_{-\infty}^{\infty}$ in place of $\int_{\mathbb{R}^{1}}$.) Thus uniform convergence does not imply dominated convergence in the sense of Theorem 11.32. However, on sets of finite measure, uniformly convergent sequences of bounded functions do satisfy Theorem 11.32.
11.7. Find a necessary and sufficient condition that $f \in \mathscr{R}(\alpha)$ on $[a, b]$. Hint: Consider Example 11.6(b) and Theorem 11.33.
11.8. If $f \in \mathscr{R}$ on $[a, b]$ and if $F(x)=\int_{a}^{x} f(t) d t$, prove that $F^{\prime}(x)=f(x)$ almost everywhere on $[a, b]$.

11.9. Prove that the function $F$ given by (11.96) is continuous on $[a, b]$.
11.10. If $\mu(X)<+\infty$ and $f \in \mathscr{L}^{2}(\mu)$ on $X$, prove that $f \in \mathscr{L}(\mu)$ on $X$. If

$$
\mu(X)=+\infty
$$

this is false. For instance, if

$$
f(x)=\frac{1}{1+|x|}
$$

then $f \in \mathscr{L}^{2}$ on $\mathbb{R}^{1}$, but $f \notin \mathscr{L}$ on $\mathbb{R}^{1}$.
11.11. If $f, g \in \mathscr{L}(\mu)$ on $X$, define the distance between $f$ and $g$ by

$$
\int_{X}|f-g| d \mu
$$

Prove that $\mathscr{L}(\mu)$ is a complete metric space.
11.12. Suppose
(a) $|f(x, y)| \leq 1$ if $0 \leq x \leq 1,0 \leq y \leq 1$,
(b) for fixed $x, f(x, y)$ is a continuous function of $y$,
(c) for fixed $y, f(x, y)$ is a continuous function of $x$.

Put

$$
g(x)=\int_{0}^{1} f(x, y) d y \quad(0 \leq x \leq 1)
$$

Is $g$ continuous?
11.13. Consider the functions

$$
f_{n}(x)=\sin n x \quad(n=1,2,3, \ldots,-\pi \leq x \leq \pi)
$$

as points of $\mathscr{L}^{2}$. Prove that the set of these points is closed and bounded, but not compact.
11.14. Prove that a complex function $f$ is measurable if and only if $f^{-1}(V)$ is measurable for every open set $V$ in the plane.
11.15. Let $\mathscr{R}$ be the ring of all elementary subsets of $(0,1]$. If $0<a \leq b \leq 1$, define

$$
\phi((a, b])=\phi((a, b))=\phi((a, b])=\phi((a, b))=b-a
$$

but define

$$
\phi((0, b))=\phi((0, b])=1+b
$$

if $0<b \leq 1$. Show that this gives an additive set function $\phi$ on $\mathscr{R}$ which is not regular and cannot be extended to a countably additive set function on a $\sigma$-ring.
11.16. Suppose $\left(n_{k}\right)$ is an increasing sequence of positive integers and $E$ is the set of all $x \in$ $(-\pi, \pi)$ at which $\left(\sin n_{k} x\right)_{k=1}^{\infty}$ converges. Prove that $m(E)=0$. Hint: For every $A \subset E$,

$$
\int_{A} \sin n_{k} x d x \rightarrow 0
$$

and

$$
2 \int_{A}\left(\sin n_{k} x\right)^{2} d x=\int_{A}\left(1-\cos ^{2} n_{k} x\right) d x \rightarrow m(A) \quad \text { as } k \rightarrow \infty
$$

11.17. Suppose $E \subset(-\pi, \pi), m(E)>0, \delta>0$. Use the Bessel inequality to prove that there are at most finitely many integers $n$ such that $\sin n x \geq \delta$ for all $x \in E$.
11.18. Suppose $f \in \mathscr{L}^{2}(\mu), g \in \mathscr{L}^{2}(\mu)$. Prove that

$$
\left|\int f g d \mu\right|^{2}=\int|f|^{2} d \mu \int|g|^{2} d \mu
$$

if and only if there is a constant c such that $\mathrm{g}(\mathrm{x})=\mathrm{cf}(\mathrm{x})$ almost everywhere. (Compare Theorem 11.35.)

# BIBLIOGRAPHY 

## Articles (Not Originally Listed Here)

[Bel43] Richard Bellman. "A Note on the Divergence of a Series". In: The American Mathematical Monthly 50.5 (1943), pp.318-319. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2302832.
[Cun67] F. Cunningham. "Taking Limits under the Integral Sign". In: Mathematics Magazine 40.4 (1967), pp. 179-186. ISSN: 0025570X, 19300980. URL: http://www.jstor.org/stable/2688673.
[Dav59] Philip J. Davis. "Leonhard Euler's Integral: A Historical Profile of the Gamma Function: In Memoriam: Milton Abramowitz". In: The American Mathematical Monthly 66.10 (1959), pp. 849-869. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2309786.
[Ebe54] W.F. Eberlein. "The Elementary Transcendental Functions". In: The American Mathematical Monthly 61.6 (1954), pp.386-392. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2307899.
[Fel67] William Feller. "A Direct Proof of Stirling's Formula". In: The American Mathematical Monthly 74.10 (1967), pp. 1223-1225. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2315671.
[Fel68] William Feller. "Correction to "A Direct Proof of Stirling's Formula"". In: The American Mathematical Monthly 75.5 (1968), pp. 518-518. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2314719.
[GF66] A.M. Gleason and N.J. Fine. "E1792". In: The American Mathematical Monthly 73.7 (1966), pp. 782-782. ISSN: 00029890, 19300972. URL: http: //www.jstor.org/stable/2314001.
[Kes70] H. Kestelman. "Riemann Integration of Limit Functions". In: The American Mathematical Monthly 77.2 (1970), pp. 182-187. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2317340.
[Niv71] Ivan Niven. "A Proof of the Divergence of $\sigma 1 / \mathrm{p}$ ". In: The American Mathematical Monthly 78.3 (1971), pp. 272-273. ISSN: 00029890, 19300972. URL: http://www.jstor.org/stable/2317524.

[Rob68] Gerson B. Robison. "A New Approach to Circular Functions, II and lim (sin x)/x". In: Mathematics Magazine 41.2 (1968), pp. 66-70. DOI: 10.1080/0025570X.1968.11975839. eprint: https://doi.org/10. 1080/0025570X.1968.11975839. URL: https://doi.org/10.1080/ 0025570X. 1968.11975839.
[Sch38] I.J. Schoenberg. "On the Peano curve of Lebesgue". In: Bulletin of the American Mathematical Society 44.8 (1938), p. 519.
[Sta74] E.L. Stark. "The Series $\sum_{k=1}^{\infty} k^{-s}, s=2,3,4, \ldots$, Once More". In: Mathematics Magazine 47.4 (1974), pp. 197-202. ISSN: 0025570X, 19300980. URL: http://www.jstor.org/stable/2689209.

# Books (Cited in the Original) 

[Art64] E. Artin. The Gamma Function. New York: Holt, Rinehart and Winston, Inc., 1964.
[Boa60] R.P. Boas. A Primer of Real Functions. Carus mathematical monographs No. 13. New York: Mathematical Association of America, distributed by Wiley \& Sons, Inc., 1960. ISBN: 9780883850008.
[Buc62a] R.C. Buck. Advanced Calculus. 2nd ed. Studies in Mathematics. Englewood Cliffs, N.J.: Prentice-Hall, 1962.
[Buc62b] R.C. Buck. Studies in Modern Analysis. Studies in Mathematics. Englewood Cliffs, N.J.: Prentice-Hall, 1962.
[Bur51] J.C. Burkill. The Lesbesgue Integral. New York: Cambridge University Press, 1951.
[Die60] J. Dieudonné. Foundations of Modern Analysis. New York: Academic Pres, Inc., 1960.
[Fle65] W.H. Fleming. Functions of Several Variables. Reading, Mass.: AddisonWesley Publishing Company, Inc., 1965.
[Gra65] L.M. Graves. The Theory of Functions of Real Variables. 2nd ed. New York: McGraw-Hill Book Company, 1965.
[Hal50] P.R. Halmos. Measure Theory. Princeton, N.J.: D. Van Nostrand Company, Inc., 1950.
[Hal58] P.R. Halmos. Finite-dimensional Vector Spaces. 2nd ed. Princeton, N.J.: D. Van Nostrand Company, Inc., 1958.
[Har47] G.H. Hardy. Pure Mathematics. New York: Cambridge University Press, 1947.
[Her64] I.N. Herstein. Topics in Algebra. New York: Blaisdell Publishing Company, 1964.

[HR50] G.H. Hardy and W. Rogosinski. Fourier Series. 2nd ed. New York: Cambridge University Press, 1950.
[HS65] E. Hewitt and K. Stromberg. Real and Abstract Analysis. New York: Springer Publishing Co., Inc., 1965.
[Kel40] O.D. Kellogg. Foundations of Potential Theory. New York: Frederick Ungar Publishing Co., 1940.
[Kno28] K. Knopp. Theory and Application of Infinite Series. Glasgow: Blackie \& Son, Ltd., 1928.
[Lan51] E.G.H Landau. Foundations of Analysis. New York: Chelsea Publishing Company, 1951.
[McS44] E.J. McShane. Integration. Princeton, N.J.: Princeton University Press, 1944.
[Niv65] I.M. Niven. Irrational Numbers. Carus mathematical monographs No. 11. New York: Mathematical Association of America, distributed by Wiley \& Sons, Inc., 1965.
[Roy63] H.L. Royden. Real Analysis. New York: The Macmillan Company, 1963.
[Rud74] W. Rudin. Real and Complex Analysis. 2nd ed. New York: McGraw-Hill Book Company, 1974.
[Sim63] G.F. Simmons. Topology and Modern Analysis. New York: McGraw-Hill Book Company, 1963.
[Smi71] K.T. Smith. Primer of Modern Analysis. Tarrytown-on-Hudson, N.Y.: Bogden and Quigley, 1971.
[Spi65] M. Spivak. Calculus on Manifolds. New York: W.A. Benjamin, Inc., 1965.
[ST67] I.M. Singer and J.A. Thorpe. Lecture Notes on Elementary Topology and Geometry. Glenview, Ill.: Scott, Foresman and Company, 1967.
[Thu56] H.A. Thurston. The Number System. London-Glasgow: Blackie \& Son, Ltd., 1956.

