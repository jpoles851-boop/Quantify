from flask import Flask, render_template, request
from Analysis2 import Analysis   # adjust if filename differs

app = Flask(__name__)

analysis = Analysis()

@app.route('/')
def home():
    return render_template('Maininterface.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form['symbol']


    d_to_e = analysis.get_debt_to_equity(symbol)


    volatility, v_comment = analysis.score_volatility(symbol)
    beta = analysis.calculate_beta(symbol)
    liquidity, l_comment = analysis.score_liquidity(symbol)

    result = {
        "symbol": symbol,
        "debt_to_equity": d_to_e,
        "volatility": volatility,
        "v_comment": v_comment,
        "beta": beta,
        "liquidity": liquidity,
        "l_comment": l_comment
    }

    return render_template('anotherone.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)