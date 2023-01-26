# Shadowrun Optimal Edge Bot

This is a bot to help you decide whether Breaking the Limit or Second Chance is the better option given your current dice pool (without edge), your edge attribute, and the limit of your throw. For details behind the math, please refer to this [blog post](https://timjadler.de/blog-posts/shadowrun-optimal-edge).

## Installation

You should be able to install this package from this repository via pip:

```
# pip install git+https://github.com/Emrys-Merlin/sr_optimal_edge_bot
```

This will install the `optimal_edge_bot` command. This command expects that the token of your discord app is exported in a environment variable with the name `DISCORD_TOKEN`. Alternatively, you can copy the `dotenv.example` to `.env` and enter your token therein.
