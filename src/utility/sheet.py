import gspread
from google.oauth2.service_account import Credentials
from common import constant, classes


class ClientSheet(metaclass=classes.Singleton):
    _sheet: str = constant.GSPREAD_SHEET_NAME
    _scope: list[str] = constant.GSPREAD_SCOPES
    _cell_reference: str = constant.GSPREAD_CELL_REFERENCE
    _auth: gspread.client.Client
    _values: dict[str, str]

    def __init__(self) -> None:
        self._auth = self.auth()

    def auth(self) -> gspread.client.Client:
        return gspread.authorize(
            Credentials.from_service_account_file("api_key.json", scopes=self._scope)
        )

    def update_values(self) -> None:
        opened_worksheet = self._auth.open(self._sheet).worksheet("main")
        rows: list[list[str]] = opened_worksheet.get_values(self._cell_reference)
        empty_dict = {}
        for row in rows:
            empty_dict[row[0]] = row[1]
        self._values = empty_dict

    def get_values(self) -> dict[str, str]:
        return self._values
