# -*- coding: utf-8 -*-
#import pymysql
# import queue
import socket
import struct
import csv
import io
file1 = io.open("2018-08-31-143130-1.csv","w",encoding='utf-8',newline='')
file2 = io.open("2018-08-31-143130-2.csv","w",encoding='utf-8',newline='')
file3 = io.open("2018-08-31-143130-3.csv","w",encoding='utf-8',newline='')
writer1 = csv.writer(file1)
writer2 = csv.writer(file2)
writer3 = csv.writer(file3)

class Urlread():
    def queryTable(self):
        stop_word = ['.pdf', 'jpg', '.ico', 'webp', '.png', '.gif', '.jpeg', '.JPEG', '.mp4', '.mp3', '.xlsx', '.doc',
                     '.plg', '.txt', '.dat', '.xls', '.ttf', '.swf', '.rpm', '.zip', '.act', '.ini', '.bmp', 'img',
                     'css', 'ts', 'js', 'php']
        line = b'\r\n'
        # url_queue = queue.Queue(maxsize=0)
        # urlnameList = []
        # url_set = set()
        url_dict = {}
        with open("2018-08-31-143130.txt", "rb") as fb:
            while line:
                # 如果该行为\r\n 则对下一行进行数据提取工作
                if line == b'\r\n':
                    # 读出下一行
                    line = fb.readline()

                    # 将前4位作为req_flag提取出来
                    chunkbuf = line[0:4]
                    # req_flag = int.from_bytes(chunkbuf, byteorder='little')
                    try:
                        req_flag = (socket.ntohl(struct.unpack("!I", chunkbuf)[0]))
                    except:
                        continue

                    # 如果既是request又是response
                    if req_flag == 2:
                        # 将该行第32位到第36位作为请求的长度提取出来
                        chunkbuf = line[32:36]
                        # reqbuflen = int.from_bytes(chunkbuf, byteorder='little')
                        try:
                            reqbuflen = socket.ntohl(struct.unpack("!L", chunkbuf)[0])
                        except:
                            continue

                        # 重新定位文件指针并读取出请求
                        now_point = fb.tell() - len(line) + 36
                        fb.seek(now_point)
                        try:
                            req_buf = fb.read(reqbuflen).decode('ascii')
                            reqbuf_array = str(req_buf).split('\r\n')
                            path = reqbuf_array[0].split(' ')[1]
                            for reqbuf_item in reqbuf_array:
                                reqbuf_item_array = reqbuf_item.split(': ')
                                if reqbuf_item_array[0] == 'host' or reqbuf_item_array[0] == 'Host':
                                    host = reqbuf_item_array[1]
                            url = host + path
                            if 'https:' not in url:
                                url = 'https://' + url
                        except UnicodeDecodeError as e:
                            continue
                        # print("req_buf:" + req_buf)
                        # url_queue.put(url)
                        flag = 0
                        for word in stop_word:
                            if word in url:
                                flag = 1
                        if flag == 0:
                            url_dict[url] = host
                        #url_set.add(url)

                        # 将请求后的4位作为回应的长度提取出来
                        chunkbuf = fb.read(4)
                        try:
                            respbuflen = socket.ntohl(struct.unpack("!L", chunkbuf)[0])
                        except struct.error as e:
                            continue

                        #读取回应长度的数据
                        chunkbuf = fb.read(respbuflen)
                        #会出现多读的错误 所以用\r\n\r\n进行拆分
                        if b'\r\n\r\n' in chunkbuf:
                            chunkbuf_array = chunkbuf.split(b'\r\n\r\n')
                            try:
                                resp_buf = chunkbuf_array[0].decode('ascii')
                            except UnicodeDecodeError:
                                continue
                            #重定位指针到回应数据末尾
                            now_point = fb.tell() - len(chunkbuf_array[1]) - 4
                            fb.seek(now_point)
                        else:
                            try:
                                resp_buf = chunkbuf.decode('ascii')
                            except UnicodeDecodeError:
                                continue

                line = fb.readline()

        #没有爬取必要的网址
        #.aspx网址有没有爬取必要？



        #print("____________________________________"+str(len(urlnameList))+"_____________________________________")

        return url_dict
