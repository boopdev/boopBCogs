from bcogs.booper import cogfile

def setup(client):
    client.add_cog(cogfile.BooperCommands(client))
