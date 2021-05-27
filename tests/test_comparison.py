from src.lupartition.methods.iset import iset_decision as iset
from src.lupartition.methods.naive import naive_decision as naive


class TestComparisonInt:
    def test_comparison_int_small(self,
                                  rand_tree_int_small1,
                                  rand_tree_int_small2,
                                  rand_tree_int_small3,
                                  rand_tree_int_small4,
                                  rand_tree_int_small5):
        assert naive(*rand_tree_int_small1) == iset(*rand_tree_int_small1)
        assert naive(*rand_tree_int_small2) == iset(*rand_tree_int_small2)
        assert naive(*rand_tree_int_small3) == iset(*rand_tree_int_small3)
        assert naive(*rand_tree_int_small4) == iset(*rand_tree_int_small4)
        assert naive(*rand_tree_int_small5) == iset(*rand_tree_int_small5)

    def test_comparison_int_large(self,
                                  rand_tree_int_large1,
                                  rand_tree_int_large2):
        assert naive(*rand_tree_int_large1) == iset(*rand_tree_int_large1)
        assert naive(*rand_tree_int_large2) == iset(*rand_tree_int_large2)
