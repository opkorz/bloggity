import click
from bloggity.app import create_app


@click.group()
@click.pass_context
def cli(ctx):
  ctx.obj = create_app()


@cli.command()
@click.pass_obj
def runserver(app):
  app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
  cli()
