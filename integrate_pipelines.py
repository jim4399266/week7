import codecs
import os

from config import Config
from util import *


def chatterbot_integrate():
	print("chatterbot_integrate")	
	file_path = 'clean_chat_corpus/chatterbot.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas


def douban_single_turn_integrate():
    print("douban_single_turn_integrate")	
    file_path = 'clean_chat_corpus/douban_single_turn.tsv'
    datas = []
    with open(file_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            dialogue = line.strip('\t\r\n').split('\t')
            dialogue = [''.join(utterance.split(' ')) for utterance in dialogue]
            datas.append(dialogue)
    return datas

def ptt_integrate():
	print("ptt_integrate")	
	file_path = 'clean_chat_corpus/ptt.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas

def qingyun_integrate():
	print("qingyun_integrate")	
	file_path = 'clean_chat_corpus/qingyun.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas

def subtitle_integrate():
	print("subtitle_integrate")	
	file_path = 'clean_chat_corpus/subtitle.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas

def tieba_integrate():
	print("tieba_integrate")	
	file_path = 'clean_chat_corpus/tieba.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas

def weibo_integrate():
	print("weibo_integrate")	
	file_path = 'clean_chat_corpus/weibo.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas

def xiaohuangji_integrate():
	print("xiaohuangji_integrate")	
	file_path = 'clean_chat_corpus/xiaohuangji.tsv'
	datas = []
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f.readlines():
			dialogue = line.strip('\t\r\n').split('\t')
			dialogue = [utterance.strip() for utterance in dialogue]
			datas.append(dialogue)
	return datas