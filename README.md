# Interleaving
A python library for conducting **interleaving**, which comparing two or multiple rankers based on observed user clicks by **interleaving** their results.

## Introduction
A/B testing is a well-known technique for comparing two or more systems based on user behaviors in a production environment,
and has been used for improving the quality of systems in many services.
Interleaving, which can be an alternative to A/B testing for comparing rankings, has shown x100 efficiency compared to A/B testing<sup>1, 2</sup>.
Since the efficiency matters a lot in particular for many alternatives in comparison, interleaving is a promising technique for user-based ranking evaluation.
This library aims to provide most of the algorithms that have been proposed in the literature.


## Interleaving algorithms

### Interleaving for two rankers

- Balanced interleaving<sup>3</sup>
- Team draft interleaving<sup>4</sup>
- Probabilistic interleaving<sup>5</sup>
- Optimized interleaving (to be implemented)<sup>6</sup>

### Interleaving for multiple rankers
- Team draft multileaving (to be implemented)<sup>7</sup>
- Probabilistic multileaving<sup>8</sup>
- Optimized multileaving (to be implemented)<sup>7</sup>

## Examples
```
>>> import interleaving
>>>
>>> method = interleaving.TeamDraft() # initialize an interleaving method
>>> a = [1, 2, 3, 4, 5] # Ranking 1
>>> b = [4, 3, 5, 1, 2] # Ranking 2
>>>
>>> ranking = method.interleave(a, b) # interleaving
>>> ranking
[1, 4, 2, 3, 5]
>>>
>>> clicks = [0, 2] # observed clicks, i.e. documents 1 and 2 are clicked
>>> result = method.evaluate(ranking, clicks)
>>> result # (1, 0) indicates Ranking 1 won.
(1, 0)
>>>
>>> clicks = [1, 3] # observed clicks, i.e. documents 4 and 3 are clicked
>>> result = method.evaluate(ranking, clicks)
>>> result # (0, 1) indicates Ranking 2 won.
(0, 1)
>>>
>>> clicks = [0, 1] # observed clicks, i.e. documents 1 and 4 are clicked
>>> result = method.evaluate(ranking, clicks)
>>> result # (0, 0) indicates a tie.
(0, 0)
```

## References
1. Chapelle et al. "Large-scale Validation and Analysis of Interleaved Search Evaluation." ACM TOIS 30.1 (2012): 6.
2. Schuth, Hofmann, Radlinski. "Predicting Search Satisfaction Metrics with Interleaved Comparisons." SIGIR 2015.
3. Joachims. "Evaluating retrieval performance using clickthrough data". Text Mining 2003.
4. Radlinski, Kurup, and Joachims. "How does clickthrough data reflect retrieval quality?" CIKM 2008.
5. Hofmann, Whiteson, and de Rijke. "A probabilistic method for inferring preferences from clicks." CIKM 2011.
6. Radlinski and Craswell. "Optimized Interleaving for Online Retrieval Evaluation." WSDM 2013.
7. Schuth et al. "Multileaved Comparisons for Fast Online Evaluation." CIKM 2014.
8. Schuth et al. "Probabilistic Multileave for Online Retrieval Evaluation." SIGIR 2015.

## License
MIT License (see LICENSE file).
