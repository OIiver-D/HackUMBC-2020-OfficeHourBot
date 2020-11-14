# This cog will populate a fresh server with different channels 
# along with setting up roles / permissions
  
import discord
from discord.ext import commands 

# - Text Channels:
        # - instructor-general
        # - instructor-commands
        # - faq
# - Voice Channels:
        # - hangout
        # - staff-hangout (hidden)
        # - office-hours (hidden)

serverRoles = ["Professor", "TA", "Student"]

class serverSetup(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("TEMPLATE cog online.")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong!")

    @commands.command(pass_context=True)
    async def hello(self, ctx):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await ctx.message.channel.send(embed=embedVar)

    # !setup
    #is_owner() at end
    @commands.command(pass_context=True)
    async def setup(self,ctx):
    #"Put a string under the function to add to !help"
        await ctx.send("Setting Up!")
        studentTxtChannels = [ ("hangout", "general discussion"),
                            ("request", "Request help from an instructor, use !help for more info"), 
                            ("faq", "Ask general questions for peers or instructors to answer."),
                            ("assignments", "Instructors will update this when new assignments are posted.")]
        
        studentVcChannels = [("hangout", "Talk about whatever your heart desires"),
                            ("waitroom","Hangout until an instructor is able to help")]
        
        instructorTxtChannels = [("instructor-hangout", "No students, no problems"),
                                ("instructor-commands", "Please be patient with them")]
        
        instructorVcChannels = [("studen-free-hangout", "Student free is stress free")]
        
        #Creates a clean slate for the server
        # myText = ctx.guild.text_channels
        # for text in myText:
        #     await text.delete()
        # myCategories = ctx.guild.categories
        # for cat in myCategories:
        #     await cat.delete()
        


        #Creates roles
        for role in serverRoles:
            newRole = await ctx.guild.create_role(name = role)
            if role == "Professor":
                newRole.permissions.update(administrator = True)
            if role == "student":
                newRole.permissions.update(read_messages = False)

        myRoles = ctx.guild.roles
        #instructor cate
        await ctx.guild.create_category("instructors")
        #student cate
        await ctx.guild.create_category("students")
        myCategories = ctx.guild.categories
        


        #creates instructor text and voice channels
        for i in instructorTxtChannels:
            channel = await myCategories[0].create_text_channel(i[0])
            await channel.edit(topic = i[1])
        for i in instructorVcChannels:
            channel = await myCategories[0].create_voice_channel(i[0])
            await channel.edit(topic = i[1])
        
        #creates student text and voice channels
        for i in studentTxtChannels:
            channel = await myCategories[1].create_text_channel(i[0])
            await channel.edit(topic = i[1])

        for i in studentVcChannels:
            channel = await myCategories[1].create_voice_channel(i[0])
            await channel.edit(topic = i[1])
       
        #for i in myRoles:
        #  await ctx.send(i.name)
        



    @commands.command(pass_context=True)
    async def delete(self,ctx):
        myText = ctx.guild.text_channels
        myVoice = ctx.guild.voice_channels
        for text in myText:
            if text.name != "general":
                await text.delete()
        for voice in myVoice:
            if voice.name != "General":
                await voice.delete()

        myCategories = ctx.guild.categories
        for cat in myCategories:
            await cat.delete()

        myRoles = ctx.guild.roles
        for role in myRoles:
            if role.name in str(serverRoles):
                await role.delete()



def setup(client):
    client.add_cog(serverSetup(client))