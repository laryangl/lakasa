# تم التعديل من قبل فريق مطوري يولاند

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "الالعاب":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **↯ اهلاً بك عزيزي اختر الاوامر الاتيه :** \n ⪼ سهم (1-6) \n ⪼ نرد (1-6) \n ⪼ سله (1-5) \n ⪼ طوبه (1-5) \n ⪼تخمين (1-64) \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩[𝘿𝙀𝙑](t.me/EEEEE1K) 𓆪"
            )
        else:
            await event.edit(
                "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **↯ اهلاً بك عزيزي اختر الاوامر الاتيه :** \n ⪼ سهم (1-6) \n ⪼ نرد (1-6) \n ⪼ سله (1-5) \n ⪼ طوبه (1-5) \n ⪼تخمين (1-64) \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩[𝘿𝙀𝙑](t.me/EEEEE1K) 𓆪"
            )
