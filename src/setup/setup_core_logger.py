from core.config import CoreConfig
from core.logger import CoreAppLog


def set_core_logger( core_config: CoreConfig ):
    """ 
    Applies the suplied configs to logging lib.\n
        ::param:: core_config: :ref:`CoreConfig`.
        ::returs: `None`.
    """
    log = core_config.log
  
    CoreAppLog.set_logging(
        level = log['level'],
        filename = log['filename'],
        output_dir = log['out_dir']
    )