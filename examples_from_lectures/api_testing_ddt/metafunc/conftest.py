def pytest_addoption(parser):
    parser.addoption(
        "--inp", action="append", default=[], type=str,
        help="inputs to pass to tests functions",
    )

    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):

    if "inp" in metafunc.fixturenames:
        metafunc.parametrize("inp", metafunc.config.getoption("--inp"))

    if "limited_param" in metafunc.fixturenames:
        end = 3

        if metafunc.config.getoption("--all"):
            end = 10

        metafunc.parametrize("limited_param", range(end))