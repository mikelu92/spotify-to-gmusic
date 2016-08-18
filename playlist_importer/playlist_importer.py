import spotipy

if __name__ == '__main__':
  if len(sys.argv) > 1:
    username = sys.argv[1]
  else:
    print "username required"
    print "usage: python name.py [username]"
  
  token = util.prompt_for_user_token(username)
  sp = spotipy.Spotify()

playlist = sp.user_playlists(
