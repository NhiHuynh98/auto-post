from playwright.sync_api import sync_playwright
import time

# Facebook Credentials (Replace with your credentials)
FB_EMAIL = "0853771565"
FB_PASSWORD = "Tuyetnhi98@"

# List of Facebook group URLs where you want to post
GROUP_URLS = [
    # "https://www.facebook.com/groups/821840388272394",
    "https://www.facebook.com/duyanh01011996",
    "https://www.facebook.com/thanhthanh.thanhthanh.798278",
    "https://www.facebook.com/profile.php?id=100011907707044",
]

# The message you want to post
POST_MESSAGE = "🚀 Đây là tin nhắn tự động, Nhi code test"
IMAGE_PATH = [
    "./images/test.jpeg",
    "./images/test_2.jpeg",
    "./images/test_3.jpeg"
]

def auto_post_facebook():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Keep False for debugging
        context = browser.new_context(storage_state="fb_session.json")  # Load session
        page = context.new_page()

        page.goto("https://www.facebook.com/", timeout=10000)
        print("✅ Logged in using saved session!")

        for group_url in GROUP_URLS:
            print(f"Posting to: {group_url}")
            page.goto(group_url, timeout=120000)
            # page.wait_for_load_state("networkidle")
            page.wait_for_load_state("domcontentloaded", timeout=60000)  # Faster page detection


            try:
                post_container = page.locator("//div[@role='button']//span[starts-with(text(), 'Write something to') or text() = 'Bạn viết gì đi...']")

                # 5️⃣ Debug: Check if post area is found
                # 4️⃣ Ensure it's visible and click it
                post_container.wait_for(timeout=5000)
                post_container.click()
                time.sleep(10)

                button_upload = page.locator('div[role="button"][aria-label*="Ảnh/video"]')
                button_upload.click()
                time.sleep(5)

                file_input = page.locator('input[type="file"][accept*="image"][class="x1s85apg"][multiple]')
                file_input.set_input_files(IMAGE_PATH)
                time.sleep(5)
                
                input_box = page.locator('div[role="textbox"][aria-label*="Write"], div[role="textbox"][aria-label*="Tạo bài"], div[role="textbox"][aria-label*="viết"]')

                input_box.fill(POST_MESSAGE)
                page.wait_for_timeout(2000)

                post_button = page.locator('div[role="button"][aria-label="Đăng"]')
                post_button.click()

                print(f"✅ Successfully posted in: {group_url}")
                
                page.wait_for_timeout(10000)  # Wait before next post
            except Exception as e:
                print(f"⚠️ Skipping {group_url} due to error: {e}")
                continue  

        browser.close()

auto_post_facebook()

