U = "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑬𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائـمه اوامر الالعاب :** \n⪼ `.اكس او` \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"


@bot.on(admin_cmd(pattern="م22"))
async def wspr(yoland):
    await eor(yoland, U)


@bot.on(admin_cmd(pattern="اكس او$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
