import typer

from scrapyd_config.service import ScrapydConfigService

app = typer.Typer()


@app.callback()
def callback():
    """== scrapyd-config =="""


@app.command()
def generate(
    env: str = typer.Option(
        ..., "--env", help="The environment for which you want a scrapyd.conf file."
    )
):
    """Generates a scrapyd.conf file, dynamically."""
    service = ScrapydConfigService()

    service.generate_conf_file(env=env, output_dir=".")
