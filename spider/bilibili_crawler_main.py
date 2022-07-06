import argparse

from spider.utils.bilibili_spider import Bilibili_Spider


def main(args):
    bilibili_spider = Bilibili_Spider(args.uid, args.save_dir, args.save_by_page, args.time)
    bilibili_spider.get()
    if args.detailed:
        bilibili_spider.get_detail()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uid', type=str, default='18337466')
    parser.add_argument('--save_dir', type=str, default='out')
    parser.add_argument('--save_by_page', action='store_true', default=False)
    parser.add_argument('--time', type=int, default=2, help='waiting time for browser.get(url) by seconds')
    parser.add_argument('--detailed', action='store_true', default=False)
    args = parser.parse_args()

    main(args)
