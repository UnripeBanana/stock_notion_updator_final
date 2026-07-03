from config import NOTION_PRICE_DB_ID
from notion.get_all_pages import get_all_pages
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할


for page in get_all_pages(NOTION_PRICE_DB_ID):

  ticker = 
