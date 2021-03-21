import os
from tqdm import tqdm

from config import Config
from process_pipelines.chatterbot import chatterbot_process_pipeline
from process_pipelines.douban import douban_process_pipeline
from process_pipelines.ptt import ptt_process_pipeline
from process_pipelines.qingyun import qingyun_process_pipeline
from process_pipelines.subtitle import subtitle_process_pipeline
from process_pipelines.tieba import tieba_process_pipeline
from process_pipelines.weibo import weibo_process_pipeline
from process_pipelines.xiaohuangji import xiaohuangji_process_pipeline

from integrate_pipelines import *


def process_all_corpus():
    if not os.path.exists(Config.clean_chat_corpus_root):
        os.mkdir(Config.clean_chat_corpus_root)

    douban_process_pipeline()
    chatterbot_process_pipeline()
    ptt_process_pipeline()
    qingyun_process_pipeline()
    subtitle_process_pipeline()
    tieba_process_pipeline()
    weibo_process_pipeline()
    xiaohuangji_process_pipeline()

def integrate_all_corpus():
    '''
    将process_all_corpus函数输出的所有清洗过的数据按照规定格式整合到一起。
    格式参考 end2end-conversational-ai-cn-master/data/train.txt
    '''

    extra_corpus = []
    extra_corpus.extend(chatterbot_integrate())
    extra_corpus.extend(douban_single_turn_integrate())
    extra_corpus.extend(ptt_integrate())
    extra_corpus.extend(qingyun_integrate())
    extra_corpus.extend(subtitle_integrate())
    extra_corpus.extend(tieba_integrate())
    extra_corpus.extend(weibo_integrate())
    extra_corpus.extend(xiaohuangji_integrate())

    with open('extra_train.txt', 'w', encoding='utf8') as f:
        for dialougue in tqdm(extra_corpus, ncols=80):
            for utterance in dialougue:
                f.writelines(utterance + "\n")
            f.writelines("\n")

if __name__ == '__main__':
    # process_all_corpus()
    integrate_all_corpus()
