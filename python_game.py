from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from score import scores
import random



def start(update,context):
    # print(update.message.chat.id)
    context.bot.send_message(5266818172,update.message.chat.first_name)
    update.message.reply_text(text="""
    Assalomu alaykum, botimizga xush kelibsiz.
    """)

    update.message.reply_text(text="""
    Mashina    (🚘)    => 200 ball
Gul            (🌺)     =>  30 ball
Xazina         (💰)    =>  100 ball
    """)
    context.user_data.clear()
    context.user_data['score_1']=0
    context.user_data['score_2']=0





    buttons = []
    row = []
    for i in range(1,25):
        row.append(InlineKeyboardButton(text='📦',callback_data=f"{i}"))
        if i%6==0:
            buttons.append(row)
            row=[]
    update.message.reply_text(text="o'yin boshlandi",
                              reply_markup=InlineKeyboardMarkup(buttons))








def query_handler(update,context):
    query = update.callback_query
    prize = random.choices(scores)
    context.user_data[f"{query.data}"]=prize[0]

    count=0
    if query.data!='open':
        buttons = []
        row = []
        for i in range(1, 25):
            if str(i) in context.user_data:
                row.append(InlineKeyboardButton(text=f"{context.user_data[f'{i}']['stiker']}", callback_data='open'))
                count+=1
            else:
                row.append(InlineKeyboardButton(text='📦', callback_data=f"{i}"))

            if i % 6 == 0:
                buttons.append(row)
                row = []
        # context.user_data['score_1']+=context.user_data[f"{query.data}"]['value']
        if count%2==0:
            context.user_data['score_2'] += context.user_data[f"{query.data}"]['value']
        else:
            context.user_data['score_1'] += context.user_data[f"{query.data}"]['value']

        query.message.edit_text(text=f"""
        1-o'yinchi    ==>   {context.user_data['score_1']}
2-o'yinchi    ==>   {context.user_data['score_2']}
navbat    ==>   {count%2+1}-ishtirokchida
        """,
                                 reply_markup=InlineKeyboardMarkup(buttons))

        if len(context.user_data)==26:
            if context.user_data['score_1']>context.user_data['score_2']:
                query.message.reply_text(text="Tabriklaymiz,1-raqamli ishtirokchi yutdi.Yangi o'yin boshlash /new_game")
            elif context.user_data['score_1']<context.user_data['score_2']:
                query.message.reply_text(text="Tabriklaymiz,2-raqamli ishtirokchi yutdi.Yangi o'yin boshlash /new_game")
            else:
                query.message.reply_text(text="o'yin durang bilan yakunlandi.Yangi o'yin boshlash /new_game")
            context.user_data.clear()










updater = Updater(token ='6942672110:AAGEsMTCbjovc3UTvgjHJ6sFrV4jQU-Exzs')
dp = updater.dispatcher

dp.add_handler(CommandHandler('start',start))
dp.add_handler(CallbackQueryHandler(query_handler))
dp.add_handler(CommandHandler('new_game',start))

updater.start_polling()
updater.idle()




