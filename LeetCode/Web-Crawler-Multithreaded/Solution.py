1# """
2# This is HtmlParser's API interface.
3# You should not implement it, or speculate about its implementation
4# """
5#class HtmlParser(object):
6#    def getUrls(self, url):
7#        """
8#        :type url: str
9#        :rtype List[str]
10#        """
11from concurrent.futures import ThreadPoolExecutor, wait
12from threading import Lock
13from typing import List
14
15class Solution:
16    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
17        hostname = startUrl.split("/")[2]
18        visited = set([startUrl])
19        lock = Lock()
20
21        def get_next_urls(url):
22            res = []
23            for next_url in htmlParser.getUrls(url):
24                if next_url.split("/")[2] != hostname:
25                    continue
26
27                with lock:
28                    if next_url in visited:
29                        continue
30                    visited.add(next_url)
31
32                res.append(next_url)
33            return res
34
35        urls = [startUrl]
36
37        with ThreadPoolExecutor(max_workers=16) as executor:
38            while urls:
39                futures = [executor.submit(get_next_urls, url) for url in urls]
40                wait(futures)
41
42                next_level = []
43                for future in futures:
44                    next_level.extend(future.result())
45
46                urls = next_level
47
48        return list(visited)