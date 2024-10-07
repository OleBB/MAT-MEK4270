import numpy as np # type: ignore


def mesh_function(f, t):
    fn = np.zeros(len(t))
    for i, tn in enumerate(t):
        fn[i] = f(tn)
    return fn

def func(t):
    if t >= 0 and t<= 3:
        return np.exp(-t)
    if t > 3 and t<=4:
        return np.exp(-3*t)
    else:
        raise RuntimeError(f"wrong input t")

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)
