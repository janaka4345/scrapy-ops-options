from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.lazada.com.my/products/dragon-kasut-lelaki-mens-shoes-men-oxfords-casual-canvas-shoes-breathable-comfortable-shoes-high-quality-men-shoes-i3889519519-s22502314795.html?spm=a2o4k.home-my.9451080930.23.75f84065iP8Ot5&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.06038866564631462%3Bfs_item_discount_price%3A26.96%3Bitem_id%3A3889519519%3Bpctr%3A0.06038866564631462%3Bcalib_pctr%3A0.0%3Bvoucher_price%3A26.96%3Bmt%3Ahot%3Bpromo_price%3A26.96%3Bfs_utdid%3A-1%3Bfs_item_sold_cnt%3A2%3Babid%3A287818%3Bfs_item_price%3A60.00%3Bpvid%3A14fdaa48-d410-4da7-8c2e-8111af9d8c33%3Bfs_min_price_l30d%3A0%3Bdata_type%3Aflashsale%3Bfs_pvid%3A14fdaa48-d410-4da7-8c2e-8111af9d8c33%3Btime%3A1711170090%3Bfs_biz_type%3Afs%3Bscm%3A1007.17760.287818.%3Bchannel_id%3A0000%3Bfs_item_discount%3A55%25%3Bcampaign_id%3A275001&scm=1007.17760.287818.0')
        page.wait_for_timeout(5000)


        browser.close()


if __name__=='__main__':
    main()
        
