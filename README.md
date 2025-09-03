# Algorithms

Python implementation of algorithms used to solve the classic problems of:
**sorting**, **searching**, etc. This package is reinvention of wheel. The goal
is to better understand Python and explore popular algorithms in depth.

## Table of contents

1. [Package features](#package-features)
2. [Introduction](#introduction)
3. [Sorting algorithms](#sorting-algorithms)
    1. [Insertion sort](#insertion-sort)
    2. [Selection sort](#selection-sort)
4. [Search algorithms](#search-algorithms)
    1. [Binary search](#binary-search)
5. [Misc. algorithms](#misc-algorithms)
6. [Next steps](#next-steps)
7. [References](#references)

## Package features

Upon installation package offers a `Numbers` object which behaves like a
Python's `list` object, i.e. it supports iteration, access by index, etc.
`Numbers` class implements sorting algorithms.

1. Install this package.
2. Inside an environment or Python shell import the `algorithms.sorter` module.
3. Now you have access to `Numbers` class.

## Introduction

The analysis of all algorithms assumes the RAM model of computation.

### Definition. ($O$-notation (big-oh))

Let a function $g : \mathbb{N} \to \mathbb{R}$ be given. Then
```math
    O(g(n)) := \{f \in \mathbb{R}^{\mathbb{N}} : (\exists c > 0)(\exists n_0 > 0)(\forall n \in \mathbb{N})(n \ge n_0 \implies 0 \le f(n) \le cg(n))\}.
```
> The shape of the above definition suggests than the $n$ in the $O(g(n))$ is
> fixed, i.e. for different $n$ the set one the right hand side might possibly
> have different functions as members. This is not the case. It's just a way the
> authors in the Cormen book [[1]](#cormen) have stated it. To be more correct
> one should avoid the parenthesis and the $n$ as in $O(g)$, and when $g$ is
> annonymous: $O(n \mapsto g(n))$ (not a fan of the last one).

According to the definition above a function $f \in O(g)$ (or $f \in O(g(n))$ if 
one wishes) iff there is some $c > 0$ such that beginning at some point ($n_0$)
the inequality $0 \le f(n) \le cg(n)$ holds for all $n$ ($n \ge n_0$).

### Definition. ($\Omega$-notation)

Suppose a function $g : \mathbb{N} \to \mathbb{R}$ is given. Then
```math
    \Omega(g(n)) := \{f \in \mathbb{R}^{\mathbb{N}} : (\exists c > 0)(\exists n_0 > 0)(\forall n \in \mathbb{N})(n \ge n_0 \implies 0 \le cg(n) \le f(n))\}.
```

### Definition. ($\Theta$-notation)

For a given function $g : \mathbb{N} \to \mathbb{R}$ we define
```math
    \Theta(g(n)) := \{f \in \mathbb{R}^{\mathbb{N}} : (\exists c_1 > 0)(\exists c_2 > 0)(\exists n_0 > 0)(\forall n \in \mathbb{N})(n \ge n_0 \implies 0 \le c_1g(n) \le f(n) \le c_2g(n))\}.
```

Obviously $\Theta(g) \subset O(g) \cap \Omega(g)$. To show the inclusion in the
other direction suppose that $f \in O(g) \cap \Omega(g)$. Then there is $c_1 > 0$
such that $0 \le f(n) \le c_1g(n)$ for all $n \ge n_1$ and there is $c_2 > 0$
such that $0 \le c_2g(n) \le f(n)$ for all $n \ge n_2$. We conclude that 
$0 \le c_2g(n) \le f(n) \le c_1g(n)$ for all $n \ge N$, where $N = \max\{n_1, n_2\}$.
Hence $\Theta(g) = O(g) \cap \Omega(g)$.

Also note that $(\forall c > 0)(O(c) = O(1))$. To see this fix $c > 0$ and
$f \in O(c)$. This implies that there is $\varepsilon > 0$ such that
$0 \le f(n) \le \varepsilon c$ for all $n \ge n_1$. Since
$\varepsilon c \cdot 1 = \varepsilon c > 0$ we conclude $f \in O(1)$. Now
suppose $f \in O(1)$ i.e. there is $\varepsilon > 0$ such that $0 \le f(n) \le \varepsilon$
for all $n \ge n_0$, then if we set $\eta = \varepsilon / c$ the inequality
$0 \le f(n) \le \eta c$ is satisfied for all $n \ge n_0$. Since $c > 0$ was
arbitrarily chosen we conclude that the statement is proven.

Using similar arguments one can see that $(\forall c > 0)(\Omega(c) = \Omega(1))$
and $(\forall c > 0)(\Theta(c) = \Theta(1))$.

Each member of $O(1)$ is a bounded function.

### Definition. ($o$-notation (little-oh))

Let $g: \mathbb{N} \to \mathbb{R}$ be given. Then
```math
    o(g(n)) = \{f \in \mathbb{R}^{\mathbb{N}} : (\forall c > 0)(\exists n_0 > 0)(\forall n \in \mathbb{N})(n \ge n_0 \implies 0 \le f(n) < cg(n))\}.
```
Recall the usual definition of a limit of a sequence. Let $f : \mathbb{N} \to \mathbb{R}$
and $L \in \mathbb{R}$. If the following condition is satisfied:
```math
    (\forall c > 0)(\exists n_0 \in \mathbb{N})(\forall n \in \mathbb{N})(n \ge n_0 \implies \vert f(n) - L \vert < c),
```
then we say that $L$ is the limit of a sequence $f$ and write $L \in \lim\limits_{n\to\infty} f(n)$.
Suppose $L_1, L_2 \in \lim\limits_{n\to\infty} f(n)$. Then for arbitrarily
chosen $c / 2 > 0$ there are $n_1, n_2 \in \mathbb{N}$ such that $n \ge n_1 \implies \vert f(n) - L_1 \vert < c / 2$ and $n \ge n_2 \implies \vert f(n) - L_2 \vert < c / 2$ for all $n \in \mathbb{N}$.
We have
```math
    \vert L_1 - L_2 \vert = \vert f(n) - L_2 - (f(n) - L_1) \vert \le \vert f(n) - L_2 \vert + \vert f(n) - L_1 \vert < \frac{c}{2} + \frac{c}{2} = c
```
for all $n \in \mathbb{N}$ such that $n \ge \max\{n_1, n_2\}$. Since $c$ was
arbitrarily chosen we conclude that $L_1 = L_2$. In other words if the limit of
the sequence exists, it is unique. We can then write $L = \lim\limits_{n\to\infty} f(n)$
for the limit instead of $L \in \lim\limits_{n\to\infty} f(n)$.

We say that a sequence converges if there is a limit of this sequence. Next, we
can define **weak convergence under condition**: let $f : \mathbb{N} \to \mathbb{R}$ be
a sequence and let $w : f[\mathbb{N}] \to \{\top, \bot\}$ be a condition. Then
we say that $f$ converges under the condition $w$ if there is a number $L \in \mathbb{R}$
such that:
```math
    (\forall c > 0)(\exists n_0 \in \mathbb{N})(\forall n \in \mathbb{N})(n \ge n_0 \implies (\vert f(n) - L \vert < c \wedge w(f(n)) = \top)),
```
and write
```math
    L = \lim\limits_{n\to\infty, w(f(n))} f(n).
```
The word weak is used to emphasize that the condition need not to be satisfied
for the first terms of the sequence.

Using the notion of weak conditional convergence we can reformulate the definition of
the set $o(\cdot)$ in the following way:
```math
    o(g) = \left\{f \in \mathbb{R}^{\mathbb{N}} : \lim\limits_{n\to\infty, \frac{f(n)}{g(n)}\cdot g(n) > 0} \frac{f(n)}{g(n)} = 0 \right\}.
```

### Definition. ($\omega$-notation)

For a given function $g : \mathbb{N} \to \mathbb{R}$ we define
```math
    \omega(g(n)) := \{f \in \mathbb{R}^{\mathbb{N}} : (\forall c > 0)(\exists n_0 > 0)(\forall n \in \mathbb{N})(n \ge n_0 \implies 0 \le cg(n) < f(n))\}.
```
Note that $f \in \omega(g)$ iff $g \in o(f)$. For example if $f \in \omega(g)$,
then for any choice of $c_1 > 0$ the inequality $0 \le cg(n) < f(n)$ is
satisfied for all sufficiently large $n \in \mathbb{N}$. For the same large $n$
the inequality $0 \le g(n) < c_2f(n)$, where $c_2 = 1/c_1$ is also true, hence
$g \in o(f)$. The implication in the other direction is similar. This means
that $\omega$ can be defined using previously defined $o$:
```math
    \omega(g) := \{f \in \mathbb{R}^{\mathbb{N}} : g \in o(f)\}.
```
As we've shown before these definitions are equivalent.

### Proposition.

Let $R := \{(f, g) \in \mathbb{R}^{\mathbb{N}} \times \mathbb{R}^{\mathbb{N}} : f \in \Theta(g)\}$.
The set $R$ is an equivalence relation in $\mathbb{R}^{\mathbb{N}}$.

*Proof.* We need to show that $R$ is reflexive, symmetric and transitive.
Reflexivity is trivial. To show symmetry assume $f \in \Theta(g)$. Then there
are $\alpha, \beta > 0$, $n_0 \in \mathbb{N}$ such that 
$n \ge n_0 \implies 0 \le \alpha g(n) \le f(n) \le \beta g(n)$ for all $n \in \mathbb{N}$.
Also we have
```math
    0 \le \frac{1}{\beta} f(n) \le g(n) \le \frac{1}{\alpha} f(n),
```
which means $g \in \Theta(f)$. Now assume that $f \in \Theta(g)$ and $g \in \Theta(h)$.
Then there are $\alpha_1, \alpha_2, \beta_1, \beta_2 > 0$ and $n_f, n_g \in \mathbb{N}$
such that
```math
    n \ge n_f \implies 0 \le \alpha_1 g(n) \le f(n) \le \alpha_2 g(n)
```
and
```math
    n \ge n_g \implies 0 \le \beta_1 g(n) \le f(n) \le \beta_2 g(n).
```
It is easy to see that
```math
n \ge \max\{n_f, n_g\} \implies 0 \le \alpha_1 \beta_1 h(n) \le \alpha_1 g(n) \le f(n) \le \alpha_2 g(n) \le \alpha_2 \beta_2 h(n).
```
From the above we conclude that $f \in \Theta(h)$ and the statement is proven. $\square$

For a given function $f \in \mathbb{R}^{\mathbb{N}}$ we define its equivalence
class as
```math
    [f]_R := \{g \in \mathbb{R}^{\mathbb{N}} : (g, f) \in R\} = \{g \in \mathbb{R}^{\mathbb{N}} : g \in \Theta(f)\}.
```
Note that for $f, g : \mathbb{N} \to \mathbb{R}$ it is either $[f]_R \cap [g]_R = \emptyset$
or $[f]_R = [g]_R$.

### Examples

1.
For each $k = 1, 2, \dots$ consider the functions $f_k : \mathbb{N} \to \mathbb{N}$
defined as $f_k(n) = n^k$. Fix $k, l \in \mathbb{N}$, $k < l$. We'll show that
$\Theta(n^l) \cap \Theta(n^k) = \emptyset$. Take $f \in \Theta(n^l)$. Then there
are $\alpha, \beta > 0$ and $N \in \mathbb{N}$ such that
```math
    n \ge N \implies 0 \le \alpha n^l \le f(n) \le \beta n^l
```
for all $n \in \mathbb{N}$. Suppose there are $\gamma, \delta > 0$ and
$M \in \mathbb{N}$ such that
```math
    n \ge M \implies 0 \le \gamma n^k \le f(n) \le \delta n^k.
```
It cannot be that $\alpha n^l \le \gamma n^k$, because then $n^{l-k} \le \gamma / \alpha$,
which means that the function $n \mapsto n^{l-k}$ is bounded, so it must be
$\gamma n^k \le \alpha n^l$. Similarly it must be that $\delta n^k \le \beta n^l$.
With this we obtain
```math
    n \ge \max\{N, M\} \implies 0 \le \gamma n^k \le \alpha n^l \le f(n) \le \delta n^k \le \beta n^l
```
for all $n \in \mathbb{N}$. But for the same reason discussed above it is not
possible that $\gamma n^k \le \beta n^l$ or $\alpha n^l \le \delta n^k$. Thus
$f \notin \Theta(n^k)$. Since $\Theta(n^l)$ and $\Theta(n^l)$ differ by at least
one element they must be disjoint.

2.
Fix two functions $f, g : \mathbb{N} \to \mathbb{R}$. Then $\max\{f, g\} \in \Theta(f + g)$.
Assume that for sufficiently large $n \in \mathbb{N}$ the sum $f + g$ is positive.
Otherwise if $f + g < 0$, then $\Theta(f + g) = \emptyset$. The case where $f + g = 0$
is also troublesome. First of all $\Theta(n \mapsto 0) = \{n \mapsto 0\}$ - in
other words the only member is the zero function (a function that maps $0$ to every
argument). Suppose that $f > 0$ and $g = -f$ for sufficiently large $n$, then
$\max\{f, g\} = f$ and $f \notin \Theta(f + g)$. Assume that $f$ and $g$ are
chosen so that their sum if positive for sufficiently large $n$. Then
```math
    0 \le \frac{1}{2}(f + g) \le \max\{f, g\} \le f + g
```
for sufficiently large $n$ and we conclude that $\max\{f, g\} \in \Theta(f + g)$.

## Sorting algorithms

### Insertion sort

The following pseudocode and analysis of this algorithm are from the Cormen book
[[1]](#cormen).

> ```
> Insertion-Sort(A, n)
> 1. for i = 2 to n
> 2.    key = A[i]
> 3.    // Insert A[i] into the sorted subarray A[1:i-1]
> 4.    j = i - 1
> 5.    while j > 0 and A[j] > key
> 6.        A[j + 1] = A[j]
> 7.        j = j - 1
> 8.    A[j + 1] = key
> ```

Let us assume that in the previous pseudocode each statement 1., 2., ..., 8. has
a time *cost* equal to $c_1$, $c_2$, ..., $c_8$, where each $c_k$, $k = 1, \dots, 8$
is constant. Moreover let $t_i$, $i = 2, \dots, n$ denote the number of times
the `while` statement in line 5, i.e. `while j > 0 and A[j] > key` is executed
for that value of $i$. This means that $i \mapsto t(i) := t_i$ is a function of
$i$, i.e. $t: \{2, \dots, n\} \to \{1, \dots, n\}$.

Let $\{W_i(j)\}_{i=2}^n$ be a sequence of boolean functions (or predicates if
one will), i.e. ${W_i : \{0, \dots, i-1\} \to \{\top, \bot\}}$,

$$
    W_i(j) \equiv j > 0 \wedge A[j] > \mathrm{key}
$$

for each $i = 2, \dots, n$. Now fix $i$ and we have a sequence

$$
    (W_i(0), W_i(1), \dots, W_i(i-2), W_i(i-1)),
$$

but during the algorithm execution the elements of the above sequence are evaluated in reverse order (in step 4. we set $j \leftarrow i-1$ and later in step 7. we decrease it $j \leftarrow j-1$):

$$
    (W_i(i-1), W_i(i-2), \dots, W_i(1), W_i(0)).
$$

Now note that in the above sequence, if for say $j_0 \in \{0, \dots, i-1\}$ we have $W_i(j_0) = \bot$, then:

$$
    W_i(j_0) = W_i(j_0-1) = \dots = W_i(0) = \bot,
$$

because `A[1:i]` is sorted, so if $A[j_0] < \mathrm{key}$, then $A[j_0 - 1] < \mathrm{key}$, but

$$
    W_i(i-1) = W_i(i-2) = \dots = W_i(j_0+1) = \top.
$$

So if $i$ is fixed, then $t_i$ is equal to the number of $\top$ in the sequence plus one (we take into account the first $j$ such that $W_i(j) = \bot$):

$$
    t_i = \mathrm{card}\{j \in \{0, \dots, i-1\} : W_i(j) = \top\} + 1 = \mathrm{card}W_i^{-1}[\{\top\}] + 1.
$$

If $i = 2$ then the cost of executing the `while` in line 5 if $c_5 t_2$; if $i = 3$ then the cost is equal to $c_5 t_3$. So the total cost after all iterations of $i$ is equal:

$$
    c_5 t_2 + c_5 t_3 + \dots + c_5 t_n = c_5 \sum_{i=2}^n t_i.
$$

Similarly the statement in line 6 is executed $t_i - 1$ times for each fixed $i$. We subtract $1$, because if the test in the `while` statement evaluates to $\bot$, then the algorithm does not enter the body of the loop. The corresponding cost of the execution of line 6 is equal to $c_6(t_i - 1)$. Summing over all values of $i$ yields:

$$
    c_6 (t_2 - 1) + c_6 (t_3 - 1) + \dots + c_6 (t_n - 1) = c_6 \sum_{i=2}^n (t_i - 1).
$$

The explenation for line 7 is similar to line 6.


| statement number | *cost* |        *times*          |
| ---------------- | ------ | ----------------------- |
|         1        | $c_1$  |          $n$            |
|         2        | $c_2$  |        $n - 1$          |
|         3        |  $0$   |        $n - 1$          |
|         4        | $c_4$  |        $n - 1$          |
|         5        | $c_5$  |    $\sum_{i=2}^nt_i$    |
|         6        | $c_6$  | $\sum_{i=2}^n(t_i - 1)$ |
|         7        | $c_7$  | $\sum_{i=2}^n(t_i - 1)$ |
|         8        | $c_8$  |        $n - 1$          |

$$
    T(n) = c_1n + c_2(n - 1) + c_4(n - 1) + c_5\sum_{i=2}^nt_i + \\ + c_6\sum_{i=2}^n(t_i - 1) + c_7\sum_{i=2}^n(t_i - 1) + c_8(n - 1).
$$

The best case scenario would be if

$$
    (\forall i \in \{2, \dots, n\})(\forall j \in \{0, \dots, i-1\}) : W_i(j) = \bot,
$$

meaning that the `while` test always evaluates to $\bot$ and thus $t_i =1$ for each $i = 2, \dots, n$. Plugging $t_i = 1$ into the formulat for $T(n)$ gives:

$$
    T(n) = c_1n + c_2(n - 1) + c_4(n - 1) + c_5(n - 1) + c_8(n - 1) = \\ = (c_1 + c_2 + c_4 + c_8)n + (-c_2 - c_4 - c_5 - c_8).
$$

Putting $a = c_1 + c_2 + c_4 + c_8$ and $b = -c_2 - c_4 - c_5 - c_8$ we see that the best case running time is **linear** in $n$:

$$
    T(n) = an + b.
$$

The worst case would be when the `while` statement was executed maximum amount of times. Note that:

$$
    W_i(0) = \bot
$$

for all $i \in \{2, \dots, n\}$. Thus the worst case is achieved when:

$$
    W_i(j) = 
        \begin{cases}
            \top, & 0 < j \le i - 1,\\
            \bot, & j = 0.
        \end{cases}
$$

> **Note**
>
> Since arrays are assumed to be indexed from 1 the functions $W_i$ are not well-defined. In particular $A[0]$ is not defined. We abuse the fact that the boolean operators `and` and `or` are **short circuiting**, so that in our situation when $0 > 0$ evaluates to $\bot$ the expression $A[0] > \mathrm{key}$ is not evaluated. To avoid the abuse we could extend the definition of $W_i$ like so (assuming $W_i(0)$ is not defined for all $i \in \{2, \dots, n\}$):
> 
> $$
    W'_i : \{0, \dots, i - 1\} \to \{\top, \bot\},\\[2ex]
    W'_i(0) = \bot,\\[2ex]
    W'_i \restriction \{1, \dots, n\} = W_i
> $$
> 
> for all $i \in \{2, \dots, n\}$. The functions $\{W'_i\}_{i=2}^n$ are the desired extensions.

> **Note**
>
> To be fair the functions $W_i$, $i \in \{2, \dots, n\}$ are not really the predicates $j > 0 \wedge A[j] > \mathrm{key}$ but valuations of these predicates.

In the worst case we have:

$$
    t_i = \mathrm{card}W_i^{-1}[\{\top\}] + 1 = (i - 1) + 1 = i
$$

for all $i \in \{2, \dots, n\}$. Plugging $t_i = i$ in the formula for $T(n)$ we obtain:

$$
    T(n) = (c_1 + c_2 + c_4 + c_8)n + (-c_2 - c_4 - c_8) + \\[2ex] + c_5\frac{(2 + n)(n - 1)}{2} + (c_6 + c_7)\frac{(1 + n - 1)(n - 1)}{2} = \\[2ex] = \frac{1}{2}(c_5 + c_6 + c_7)n^2 + \frac{1}{2}(2c_1 + 2c_2 + 2c_4 + c_5 - c_6 - c_7 + 2c_8)n + \\[2ex] + (-c_2 - c_4 - c_5 - c_8).
$$

Thus worst case running time is quadratic in $n$: $T(n) = an^2 + bn + c$ for some $a,b,c$, $a\not=0$.

#### Recursive insertion sort

Insertion sort algorithm can be thought of as a recursive algorithm: in order to sort `A[1:n]`, recursively sort the subarray `A[1:n-1]` and then insert `A[n]` into the sorted subarray `A[1:n-1]`.

> ```
> Insertion-Sort-R(A, n)
> 1. if n < 2, then
> 2.    return
> 3. // recursively sort A[1:n-1]
> 4. Insertion-Sort-R(A, n-1)
> 5. // insert A[n-1] into the sorted array A[1:n-1]
> 6. key = A[n-1]
> 7. j = n - 2
> 8. while j >= 0 and A[j] > key:
> 9.      A[j+1] = A[j]
> 10.     j = j - 1
> 11. A[j+1] = key
> ```

### Selection sort

> ```
> Selection-Sort(A, n)
> 1. for i = 1 to n-1
> 2.    key = i
> 3.    // Find the index of the smallest element of A[i:n]
> 4.    for j=i+1 to n
> 5.        if A[i] > A[j]
> 6.            key = j
> 7.    // Swap A[i] and A[key]
> 8.    temp = A[i]
> 9.    A[i] = A[key]
> 10.   A[key] = temp
> ```

| statement number |  *cost*  |            *times*               |
| ---------------- | -------- | -------------------------------- |
|         1        |  $c_1$   |              $n$                 |
|         2        |  $c_2$   |            $n - 1$               |
|         3        |   $0$    |            $n - 1$               |
|         4        |  $c_4$   | $\sum_{i = 1}^{n-1} (n - i + 1)$ |
|         5        |  $c_5$   |   $\sum_{i = 1}^{n-1} (n - i)$   |
|         6        |  $c_6$   |      $\sum_{i=1}^{n-1} t_i$      |
|         7        |   $0$    |            $n - 1$               |
|         8        |  $c_8$   |            $n - 1$               |
|         9        |  $c_9$   |            $n - 1$               |
|         10       | $c_{10}$ |            $n - 1$               |

Let $\{W_i\}_{i=1}^{n-1}$ be a sequence of boolean functions ${W_i : \{i+1, \dots, n\} \to \{\top, \bot\}}$, $W_i(j) \equiv A[i] > A[j]$. Then for each $i \in \{i, \dots, n-1\}$ let $t_i$ denote the number of times the test in the `if` statement in line 5 evaluates to $\top$, i.e.:

$$
    t_i = \mathrm{card}W_i^{-1}[\{\top\}].
$$

The best case scenario is when $t_i = 0$ for all $i \in \{1, \dots, n-1\}$. Then the running time is:

$$
    T(n) = c_1 n + (c_2 + c_4 + c_8 + c_9 + c_{10})(n - 1) + \\[2ex] + (c_4 + c_5) \sum_{i=1}^{n-1} (n - i) = \\[2ex] = \frac{1}{2}(c_4 + c_5)n^2 + (c_1 + c_2 + \frac{c_4}{2} - \frac{c_5}{2} + c_8 + c_9 + c_{10})n + \\[2ex] - (c_2 + c_4 + c_8 + c_9 + c_{10}).
$$

Thus in the best case scenario the running time $T(n)$ is quadratic in $n$.

The worst case scenario would be when $W_i(j) = \top$ for all $j \in \{i+1, \dots, n\}$. That is, when each `if` evaluates to $\top$ every time. We have:

$$
    t_i = \mathrm{card}W_i^{-1}[\{\top\}] = \mathrm{card}\text{ }\mathrm{dom}W_i = n - (i + 1) + 1 = n - i
$$

for all $i \in \{i, \dots, n-1\}$. The formula for running time is similar, we just need to adjust for $c_6$:

$$
    T(n) = \frac{1}{2} (c_4 + c_5 + c_6)n^2 + (c_1 + c_2 + \frac{c_4}{2} - \frac{c_5}{2} - \frac{c_6}{2} + c_8 + c_9 + c_{10})n + \\[2ex] - (c_2 + c_4 + c_8 + c_9 + c_{10}).
$$

## Search algorithms

### Binary search ([Cormen](#cormen) task 2.3-6)

Recall the **linear search**. For given array $A$ and value $v$ we search for the index $i$ such that $A[i] = v$. Observe that if the subarray being searched is already sorted, the searching algorithm can check the midpoint of the subarray against $v$ and eliminate half of the subarray from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion of the subarray each time.

> ```
> Binary-Search(v, A, a, b)
> 1. if a > b
> 2.    return null
> 3. q = floor((a + b) / 2)
> 4. if v = A[q]
> 5.    return q
> 6. else if v < A[q]
> 7.    Binary-Search(v, A, a, q - 1)
> 8. else if v > A[q]
> 9.    Binary-Search(v, A, q + 1, b)

## Misc. algorithms

### Adding two binary numbers of length $n$ ([Cormen](#cormen) task 2.1-5)

Consider the problem of adding two $n$-bit binary integers $a$ and $b$, stored in two $n$-element arrays $A[0:n-1]$ and $B[0:n-1]$, where each element is either $0$ or $1$, $a = \sum_{i=0}^{n-1} A[i] \cdot 2^i$, and $b = \sum_{i=0}^{n-1} B[i] \cdot 2^i$. The sum $c = a + b$ of the two integers should be stored in binary form in an $(n + 1)$-element array $C[0:n]$, where $c = \sum_{i=0}^n C[i] \cdot 2^i$. Write a procedure <span style="font-variant:small-caps;">Add-Binary-Integers</span> that takes as input arrays $A$ and $B$, along with the length $n$, and returns array $C$ holding the sum.

> ```
> Add-Binary-Integers(A, B, n)
> 1. //Create a 0-based array of size n+1
> 2. C = C[0:n]
> 3. memory = 0
> 4. for i=0 to n-1
> 5.    C[i] = ((A[i] + B[i]) % 2) + memory
> 6.    memory = floor((A[i] + B[i] + memory) / 2)
> 7. C[n] = memory
> 8. return C
> ```

| statement number |  *cost*  | *times* |
| ---------------- | -------- | ------- |
|         1        |   $0$    |   $1$   |
|         2        |  $c_2$   |   $1$   |
|         3        |  $c_3$   |   $1$   |
|         4        |  $c_4$   | $n + 1$ |
|         5        |  $c_5$   |   $n$   |
|         6        |  $c_6$   |   $n$   |
|         7        |  $c_7$   |   $1$   |
|         8        |  $c_8$   |   $1$   |

Best/worst case running time $T$ is straight forward to find. Consulting the table above we have:

$$
    T(n) = c_2 + c_3 + c_4(n + 1) + c_5n + c_6n + c_7 + c_8 = an + b,
$$
for some $a,\ b$.

## Next steps

+ Implement further algorithms.

## References

<a name="cormen">[1]</a>: Cormen T.H., Leiserson C.E., Rivest R.L., Stein C, *Introduction to Algorithms*, 2nd edition, MIT Press, 2022.
