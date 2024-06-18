## 環境

- Windows 11
- google chrome
- インターネット接続

## 手順

### 1. Microsoft Store から Python をインストール

1. Microsoft Store を開きます。
2. 「Python」を検索します。
3. 最新バージョンの Python（例：Python 3.9 または Python 3.10等）を選択します。
4. 「入手」をクリックして Python をインストールします。

### 2. Selenium をインストール

1. コマンドプロンプトを開きます。
2. 次のコマンドを実行して Selenium をインストールします：

   ```cmd
   pip install selenium
   ```

### 3. ChromeDriver をインストール

1. インストールされている Chrome のバージョンを確認します：

   - Chrome を開きます。
   - chrome://settings/help にアクセスしてバージョンを確認します。

2. 対応するバージョンの ChromeDriver をダウンロードします：

   - [ChromeDriver のダウンロードページ](https://googlechromelabs.github.io/chrome-for-testing/)にアクセスします。
   - お使いの Chrome ブラウザのバージョンに一致するバージョンをダウンロードします。

3. ダウンロードした ChromeDriver を任意のディレクトリに解凍して配置します（例：C:\Tools\chromedriver）。

### 4. ポートを指定して Google Chrome を起動
1. コマンドプロンプトを開きます。

2. 次のコマンドを実行して、リモートデバッグ用のポート（例：9222）を指定して Chrome を起動します：

   ```cmd
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeProfile"
   ```

   ※ポップアップを許可しておく

3. 指定のポートが使用中であることを確認：

    ```cmd
    netstat -ano | find ":9222"
    ```

### 5. ページにアクセスしてログイン

    リモートデバッグが有効になっている Chrome ブラウザで、対象の URL にアクセスします。
    ID とパスワードを使用してログインします。Cloudflare の認証は自動化では通過できないため、手動ログインが必要です。

### 6. chromedrive.py をコマンドプロンプトで実行
1. config.jsonを編集

    - chrome_debugger_address : chromeが使っているアドレスとポート
    - chrome_driver_path :　chromedriver.exeのパス（要エスケープ）
    - url : ページのURL（iframeで埋め込まれたURLを指定すること）
    - specified_time_jst : 実行する日時（開始日時？）
    - date_value : 「日付」選択肢で選択したいオプションのID
    - time_value : 「時間」選択肢で選択したい文字列
    - webdriver_wait_time : ページの要素が読み込まれるまで待つ時間

2. chromedrive.py スクリプトが作業ディレクトリにあることを確認します。

    ```cmd
    cd chromedrive.pyがあるディレクトリ
    ```

3. スクリプトを実行します。

    ```cmd
    python chromedrive4.py
    ```

4. specified_time_jstで指定した日時に操作が始まります。