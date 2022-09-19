from typing import TypedDict


class QuoteAuthorConf( TypedDict ):
    img_aplha          : int
    resize_limit_ratio : float
    rotate_degs        : int


class QuoteCanvasConf( TypedDict ):
    color        : str
    height       : int
    margin_ratio : float
    mode         : str
    width        : int


class QuoteDecorBottomConf( TypedDict ):
    color  : str
    height : int


class QuoteDecorConf( TypedDict ):
    bottom: QuoteDecorBottomConf


class QuoteImgsConf( TypedDict ):
    fallback    : str
    overlay_dir : str
    out_dir     : str


class QuoteTextBottomConf( TypedDict ):
    font_color  : str
    font_face   : str
    font_size   : int
    size_factor : float


class QuoteTextCenterConf( QuoteTextBottomConf ):
    stroke_color : str
    stroke_size  : int
    wrap         : int


class QuoteTextsConf( TypedDict ):
    bottom : QuoteTextBottomConf
    center : QuoteTextCenterConf


class QuoteWalkerConf( TypedDict ):
    asset               : str
    bottom_margin_ratio : float
    proportion_ratio    : float


class QuoteConf( TypedDict ):
    author : QuoteAuthorConf
    canvas : QuoteCanvasConf
    decor  : QuoteDecorConf
    imgs   : QuoteImgsConf
    text   : QuoteTextsConf
    walker : QuoteWalkerConf


