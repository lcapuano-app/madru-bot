from typing import Any

from models import ConfigQuoteType, ConfigQuoteCanvasType, QuoteGenModes
from validators.validate_props import ValidateProps


class QuoteConfigValidator ( ValidateProps ):

    def crash_invalid( data: Any ) -> None:
        self = QuoteConfigValidator

        self.exit_on_error( prop='quote', obj=data, expected_type=object )

        quote_config: ConfigQuoteType = data['quote']

        self.__crash_invalid_canvas( quote_config['canvas'] )


    def __crash_invalid_canvas( canvas_cfg: ConfigQuoteCanvasType ) -> None:
        self = QuoteConfigValidator
        self.exit_on_error( prop='color',  obj=canvas_cfg, expected_type=str )
        self.exit_on_error( prop='mode',   obj=canvas_cfg, expected_type=str )
        self.exit_on_error( prop='height', obj=canvas_cfg, expected_type=int )
        self.exit_on_error( prop='width',  obj=canvas_cfg, expected_type=int )

        if not QuoteGenModes.has_value( canvas_cfg['mode'] ):
            self.print_and_exit(
                prop=f'mode ({canvas_cfg["mode"]})',
                missing=False,
                should_be='<class str> RGB | RGBA'
            )
