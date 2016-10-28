import interleaving as il
from interleaving import BalancedRanking
import numpy as np
import pytest
np.random.seed(0)
from .test_methods import TestMethods

class TestBalanced(TestMethods):

    def test_raise_value_error(self):
        with pytest.raises(ValueError):
            il.Balanced([[0], [1], [2]]) # three rankings are not acceptable

    def test_interleave(self):
        self.interleave(il.Balanced, [[1, 2], [2, 3]], 2, [(1, 2), (2, 1)])
        self.interleave(il.Balanced, [[1, 2], [3, 4]], 2, [(1, 3), (3, 1)])
        self.interleave(il.Balanced, [[1, 2], [2, 3]], 3, [(1, 2), (2, 1, 3)])
        self.interleave(il.Balanced, [[1, 2], [3, 4]], 3, [(1, 3, 2), (3, 1, 4)])

    def test_init_sampling(self):
        b = il.Balanced([[1, 2], [2, 3]], sample_num=100)
        rankings, probabilities = zip(*b.ranking_distribution)
        assert set([(1, 2), (2, 1)]) == set([tuple(r) for r in rankings])
        self.assert_almost_equal(*probabilities)

        res = b.interleave()
        assert res == [1, 2] or res == [2, 1]

    def test_evaluate(self):
        ranking = BalancedRanking([1, 2])
        ranking.a = [1, 2]
        ranking.b = [2, 3]
        self.evaluate(il.Balanced, ranking, [0, 1], [])
        self.evaluate(il.Balanced, ranking, [0], [(0, 1)])
        self.evaluate(il.Balanced, ranking, [1], [(1, 0)])
        self.evaluate(il.Balanced, ranking, [], [])

        ranking = BalancedRanking([2, 1, 3])
        ranking.a = [1, 2]
        ranking.b = [2, 3]
        self.evaluate(il.Balanced, ranking, [0, 1, 2], [])
        self.evaluate(il.Balanced, ranking, [0, 1], [])
        self.evaluate(il.Balanced, ranking, [0, 2], [(1, 0)])
        self.evaluate(il.Balanced, ranking, [1, 2], [])
        self.evaluate(il.Balanced, ranking, [0], [(1, 0)])
        self.evaluate(il.Balanced, ranking, [1], [(0, 1)])
        self.evaluate(il.Balanced, ranking, [2], [(1, 0)])
        self.evaluate(il.Balanced, ranking, [], [])
