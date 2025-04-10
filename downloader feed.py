import instaloader

L = instaloader.Instaloader()

profile_name = input("Digite o nome exato do perfil desejado: ")

try:
    profile = instaloader.Profile.from_username(L.context, profile_name)
except instaloader.exceptions.ProfileNotExistsException:
    print("Escreva o nome do perfil correto")
    exit()
    
for post in profile.get_posts():
    L.download_post(post, target=profile.username)
    