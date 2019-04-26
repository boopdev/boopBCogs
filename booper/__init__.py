from bcogs.booper import booper

def setup(client):
    client.add_cog(booper.BooperCommands(client))
