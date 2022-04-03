import click
from simple_url_crawler_cli.cli.help.main import get_help


@click.command()
@click.option('--help', '-h', is_flag=True, help='Get help using the cli.')
@click.argument('command', default='-h', required=False)
def cmd_help(command, argin):
    """A simple Cli link scrapper which can extract and parse all links from a given url. """
    click.echo(get_help(command, argin))
