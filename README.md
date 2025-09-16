 # A-8 羊蹄咖啡專題

## Miro
```
https://miro.com/app/board/uXjVJdnIC-4=/?utm_source=notification&utm_medium=email&utm_campaign=daily-updates&utm_content=view-board-cta&lid=ilk838wmgwc3
```

## 設計稿(修改版)
```
https://www.figma.com/design/PrGtcgM9NgwmM1fsdcZSAd/%E5%9C%98%E9%9A%8A%E5%B0%88%E9%A1%8C--A-8-%E7%BE%8A%E8%B9%84%E5%92%96%E5%95%A1--Copy-?node-id=0-1&p=f&t=KnyMb6pyorANgp24-0
```

## 設計稿
```
https://www.figma.com/design/JR0sze2fVEr2cuvrhDuXd1/%E5%9C%98%E9%9A%8A%E5%B0%88%E9%A1%8C--A-8-%E7%BE%8A%E8%B9%84%E5%92%96%E5%95%A1?m=auto&t=WblgXowAmwolyREO-6
```

## 目前進度
```
header
電腦: % 手機: % 
footer
電腦: % 手機: %
about.html
電腦: % 手機: %
explore.html
電腦: 100% 手機:100%
index.html
電腦: % 手機: %
products.html
電腦: % 手機: %
porductdetail.html
電腦: % 手機: %
```

## Git
```
https://github.com/MarcoChiu/coffee
https://marcochiu.github.io/coffee/
```

## 結構說明

```
coffee
├─assests
├───scss
├─────base (通用樣式)
├───────_base.scss (全域通用樣式)
├───────_utils.scss (全域自訂義通用樣式)
├─────customize
├───────_utils.scss (暫時無用)
├───────_variables.scss (自訂義用來覆蓋bootstrap 顏色 間距的scss)
├─────layout (對應header or footer等共用的scss)
├───────_footer.scss (footer scss)
├───────_header.scss (header scss) 
├─────pages (對應個頁面的scss)
├───────about.scss (關於羊蹄 scss)
├───────explore.scss (探索羊蹄 scss)
├───────index.scss (首頁專用的scss)
├───────productdetail.scss (產品詳情頁 scss)
├───────products.scss (線上商店 scss)
├─────utils (老師的方式暫時無用)
├───────_variables-dark.scss  
├───────_variables.scss  
├───all.scss (所有import的scss)
├─layout (ejs)
├───footer.ejs (footer程式碼)
├───header.ejs (header程式碼)
├───js.ejs (所有javascript )
├───style.ejs (所有額外參考css)
├─pages (html)
├───about.html (關於羊蹄)
├───demo.html (通用樣式demo用)
├───explore.html (探索羊蹄)
├───index.html (首頁)
├───productdetail.html (產品詳情頁)
├───products.html (線上商店)
├─public (靜態不編譯檔案)
├───fonts (字體)
├─────ChenYuluoyan-2.0-Thin.woff2
├───images (靜態圖片)

```

# 網頁切版直播班 Vite 範例 - Bootstrap 版本

## Node.js 版本
  - 專案的 Node.js 版本需為 v18 以上
  - 查看自己版本指令：`node -v`


## 指令列表
- `npm install` - 初次下載該範例專案後，需要使用 npm install 來安裝套件
- `npm run dev` - 執行開發模式
  - 若沒有自動開啟瀏覽器，可嘗試手動在瀏覽器上輸入
    `http://localhost:5173/<專案名稱>/pages/index.html`
- `npm run build` - 執行編譯模式（不會開啟瀏覽器）
- `npm ru deploy` - 自動化部署

## 資料夾結構
  - assets # 靜態資源放置處
    - images # 圖片放置處
    - scss # SCSS 的樣式放置處

  - layout # ejs 模板放置處
  - pages # 頁面放置處

- JavaScript 程式碼可寫在 main.js 檔案

### 注意事項
- 已將 pages 資料夾內的 index.html 預設為首頁，建議不要任意修改 index.html 的檔案名稱
- .gitignore 檔案是用來忽略掉不該上傳到 GitHub 的檔案（例如 node_modules），請不要移除 .gitignore

## 開發模式的監聽
vite 專案執行開發模式 `npm run dev` 後即會自動監聽，不需要使用 `Live Sass Compiler` 的 `Watch SCSS` 功能


## 部署 gh-pages 流程說明
### Windows 版本
1. 在 GitHub 建立一個新的 Repository

2. 部署前請務必先將原始碼上傳到 GitHub Repository 也就是初始化 GitHub，因此通常第一步驟會在專案終端機輸入以下指令
```cmd
git init # 若已經初始化過就可以不用輸入
git add .
git commit -m 'first commit'
git branch -M main
git remote add origin [GitHub Repositories Url]
git push -u origin main // 僅限第一次輸入，往後只需要輸入 git push
```

3. 初始化完畢後，執行 `npm run deploy` 指令進行自動化部署