from int_to_Roman import int_to_Roman


def test_ans():
    assert int_to_Roman(14) == 'XIV'
    assert int_to_Roman(18) == 'XVIII'
    assert int_to_Roman(80) == 'LXXX'
    assert int_to_Roman(99) == 'XCIX'
    assert int_to_Roman(199) == 'CXCIX'
    assert int_to_Roman(1437) == 'MCDXXXVII'
    assert int_to_Roman(1880) == 'MDCCCLXXX'
    assert int_to_Roman(3333) == 'MMMCCCXXXIII'
    assert int_to_Roman(3999) == 'MMMCMXCIX'
    assert int_to_Roman(4975) == 'MMMMCMLXXV'
