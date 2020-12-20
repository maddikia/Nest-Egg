# Nest-Egg
**Nest Egg** is a **gamified banking application for kids.** It uses real money in a kid’s custodial bank/investment account. It pairs real financial decisions made by the kid, approved by the parent. It leverages the fact that having “skin in the game” increases engagement. When the kid reaches a legal age, **a real Nest Egg is delivered.** 

Created for Finastra's **Hack to the Future 2020** Hackathon. Check out our [Devpost](https://devpost.com/software/nest-egg-e3o0ap).

## Usage & Testing
Download the entirety of the `kid` directory and run `index.html` to start. 
For the most accurate experience, open the page in Chrome and use DevTool's Mobile Device Viewport Mode, selecting iPad and rotating the viewport to landscape orientation. If you're not sure how to do this, check out [Chrome's DevTools Documentation](https://developers.google.com/web/tools/chrome-devtools/device-mode).

Finastra FusionFabric.cloud **API Integration:** This is a preliminary integration which can create an external transfer and retrieve said transfer's details upon completion. For testing purposes, generate an authorization token through Postman and replace `token` in `external-transfer.py` before running.
