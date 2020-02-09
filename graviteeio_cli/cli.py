import logging

import click
import click_completion

from .__version__ import __version__ as VERSION
from .environments import GRAVITEEIO_CONF_FILE
from .graviteeio.apim.apim import apim
from .graviteeio.config import GraviteeioConfiguration, config

# Enable shell completion.
click_completion.init()

@click.option(
    '--config', help='Path to configuration file. Default: ' + GRAVITEEIO_CONF_FILE,
    type=click.Path(), default=GRAVITEEIO_CONF_FILE
)
@click.option('--log', help='displays detailed information', is_flag=True)
@click.option('--log-level', help='displays detailed information', default= logging._levelToName[logging.INFO],
type=click.Choice(['CRITICAL','ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'], case_sensitive=False))
#@click.option('--username', help='HTTP Basic Authentication username', type=str)
#@click.option('--password', help='HTTP Basic Authentication password', type=str)
#@click.option('--timeout', help='Connection timeout in seconds.', type=int)
@click.group()
@click.version_option(prog_name=click.style('graviteeio-cli', fg='blue', bold=True), version=VERSION)
@click.pass_context
def main(ctx, config, log, log_level):
        """Graviteeio cli"""
        ctx.obj = {}
        ctx.obj['config_path'] = config
        
        log_level = logging._nameToLevel[log_level.upper()]
        if not log:
            logging.disable(logging.ERROR)

        logging.basicConfig(format='%(name)s-%(levelname)s: %(message)s', level=log_level)
        

main.add_command(apim)

if __name__ == '__main__':
    main()
