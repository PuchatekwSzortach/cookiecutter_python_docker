"""
Module with docker commands
"""

import invoke


@invoke.task
def build_app_container(context):
    """
    Build app container

    :param context: invoke.Context instance
    """

    command = (
        "DOCKER_BUILDKIT=1 docker build "
        "--tag puchatek_w_szortach/{{ cookiecutter.project_name }}:latest "
        "-f ./docker/app.Dockerfile ."
    )

    context.run(command, echo=True)


@invoke.task
def run(context):
    """
    Run app container

    Args:
        context (invoke.Context): invoke context instance
        config_path (str): path to configuration file
    """

    command = (
        "docker run -it --rm "
        "puchatek_w_szortach/{{ cookiecutter.project_name }}:latest /bin/bash"
    )

    context.run(command, pty=True, echo=True)
