from django.conf import settings
from product.celery import app

from django.db.models import Sum

from shop.models import Shop

from datetime import datetime
import csv

print('settings.MEDIA_ROOT is =>', settings.MEDIA_ROOT)

@app.task(name = 'sync_shop_info')
def sync_shop_info(*args, **kwargs):
    '''
        每日零點根據訂單記錄算出各個館別的 1.總銷售金額 2.總銷售數量 3.總訂單數量
        輸出方式 : slack, email, csv ...
    '''
    file_name = f'{settings.MEDIA_ROOT}/{datetime.now().strftime("%Y-%m-%d")}-shop-info.csv'
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        for shop in Shop.objects.all():
            statistics = shop.order_b.aggregate(
                Sum('price'), Sum('qty')
            )
            total_price = str(statistics.get('price__sum'))
            total_qty = str(statistics.get('qty__sum'))
            order_aty = str(shop.order_b.count())
            data = (shop.pk, shop.shop_name, total_price, total_qty, order_aty)
            writer.writerow(data)
    f.close()

    
