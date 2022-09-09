from typing import Any

from validators.validate_props import ValidateProps
from models import ConfigLogType, ConfigLogLevel


class LogConfigValidator ( ValidateProps ):

    def crash_invalid( data: Any ) -> None:
        self = LogConfigValidator

        self.exit_on_error( prop = 'log', obj = data, expected_type = object )

        log_config: ConfigLogType = data['log']

        self.exit_on_error( prop = 'filename', obj = log_config, expected_type = str )
        self.exit_on_error( prop = 'out_dir', obj = log_config, expected_type = str )
        self.exit_on_error( prop = 'level', obj = log_config, expected_type = int )

        if not ConfigLogLevel.has_value( log_config['level'] ):
            self.print_and_exit(
                prop=f'level ({log_config["level"]})',
                missing=False,
                should_be='<class int> 10(DEBUG) | 20(INFO) | 30(WARNING) | (40)ERROR | (50)CRITICAL'
            )
