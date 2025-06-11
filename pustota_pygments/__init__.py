from typing import final

from pygments.style import Style
from pygments import token


@final
class PustotaStyle(Style):
    """Regular style for dark themes."""

    styles = {
        # Group 1: comments
        token.Comment: 'italic #626A73',
        # Group 2: strings / text
        token.Literal.String: '#C2D94C',
        # Group 3: constants
        token.Literal: '#E6B450',
        # Group 4: keywords and operators
        token.Keyword: '#FF8F40',
        token.Operator: '#FF8F40',
        # Group 5: Function definitions
        token.Name.Function: '#FFB454',
        # Group 6: Type definitons
        token.Name.Class: '#59C2FF',
        # Everything else:
        token.Token: '#B3B1AD',
    }


@final
class PustotaLightStyle(Style):
    """Regular style for light themes."""

    styles = {
        # Group 1: comments
        token.Comment: 'italic #787B80',
        # Group 2: strings / text
        token.Literal.String: '#86B300',
        # Group 3: constants
        token.Literal: '#ED9366',
        # Group 4: keywords and operators
        token.Keyword: '#FA8D3E',
        token.Operator: '#FA8D3E',
        # Group 5: Function definitions
        token.Name.Function: '#F2AE49',
        # Group 6: Type definitons
        token.Name.Class: '#399EE6',
        # Everything else:
        token.Token: '#5C6166',
    }
