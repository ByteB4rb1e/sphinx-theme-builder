"""Compilation entrypoint."""

import os

import click

from ..nodejs import generate_assets, generate_assets_relaxed
from ..project import Project


class CompileCommand:
    """Compile the current project's assets."""

    interface: list[click.Parameter] = [
        click.Option(
            ["--production"],
            is_flag=True,
            default=False,
            help="Runs the build with `NODE_ENV=production` (`development` by default).",
        ),
    ]

    def run(self, production: bool) -> int:
        """Make it happen."""
        project = Project.from_cwd()

        if os.environ.get("STB_USE_SYSTEM_NODE", 'True') in ['True', '1']:
            generate_assets_relaxed(project)
        else:
            generate_assets(project, production=production)
        return 0
