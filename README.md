### Website
   - 請點選以下網址查看 API 內容 (https://annproduct.herokuapp.com/swagger/)

### GitHub Link
   - 請點選以下網址查看 Code ()
### Model
1. **Product** 商品資料
2. **Order** 訂單資料
3. **Shop** 館別資料
### API
1. **加入訂單,訂單成立需檢查是否符合vip身份,並確認商品庫存數量(身份和庫存檢查限用decorator實作)**
   - mer-01-get 查詢商品列表
   - order-02-post 將商品新增至訂單

2. **刪除訂單(庫存檢查限用decorator實作)**
   - order-03-delete 刪除訂單

3. **根據訂單記錄計算出最受用戶歡迎的商品前三名(根據商品銷售量)**
   - mer-01-get 查詢商品列表

### 設計排成功能
1. **每日零點根據訂單記錄算出各個館別的1.總銷售金額 2.總銷售數量 3.總訂單數量**
   
   使用 Celery beat 製作每日排程，用 Redis 當作 Broker 存放 message，進行 sync_shop_info task
   sync_shop_info task 會計算館別料，並生成 csv file
   下載每日報表
   
   - shop-01-get 下載每日每個館別的統計報表

### 雲端部署
1. **使用 Dockerfile 將 python server 打包**
2. **使用 Heroku 進行 deployment，部署至 heroku**
