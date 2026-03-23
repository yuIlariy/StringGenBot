from pyrogram import filters, types

from anony import app, buttons, db


@app.on_message(filters.command(["start"]) & filters.private)
async def f_start(_, m: types.Message):
    await m.reply_photo(
        photo="https://telegra.ph/file/d84e1a26bf8596bbad10a.jpg",
        caption=f"Hey {m.from_user.first_name} 👋,\n\nThis is {app.mention} 🤖,\nAn open source session generator bot ⚡.\n\n🛸 powered by [NAm](https://t.me/xspes)",
        reply_markup=buttons.start_key(),
    )
    await db.add_user(m.from_user.id)
