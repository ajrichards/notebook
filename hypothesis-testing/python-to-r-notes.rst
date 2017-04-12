

If you are familiar with R here are the equivalents

import scipy.stats as stats

+-------------------------------------------+-------------------------------------+-----------------------------+
| Description                               | Python                              | R                           |
+===========================================+=====================================+=============================+
| Cumulative distribution function (CDF)    | stats.norm.cdf(1.96) = 0.975        | pnorm(1.96) = 0.975         |
| Inverse of CDF (or Percent point function)| stats.norm.ppf(0.975) = 1.96        | qnorm(0.975) = 1.96         |
| Evaluate the PDF                          | stats.norm.pdf(1.96) = 0.05         | dnorm(1.96) = 0.05          |
| Calculate a 2-sided pvalue with Z = 1.99  | 2 * (1 - s.norm.cdf(1.99)) = 0.047  | 2 *(1-  pnorm(1.99)) = 0.047|
+-------------------------------------------+------------------------------+------------------------------------+

Two sided p-value if Z > 0 2 * (1-Phi(Z)) else 2 * (Phi(Z))
One sided p-value if Z > 0 (1-Phi(Z)) else (Phi(Z))
Phi is the standard notation for the inverse CDF
