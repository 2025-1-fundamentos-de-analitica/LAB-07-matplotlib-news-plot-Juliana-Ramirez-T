#Se importa lo necesario
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    #Definicion de rutas
    input_dir = "files/input/news.csv"
    output_dir = "files/plots/news.png"
    os.makedirs(os.path.dirname(output_dir), exist_ok=True)


    plt.Figure()

    colors = {
        'Television': 'blue',
        'Newspaper': 'purple',
        'Internet': 'pink',
        'Radio': 'orange',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    #MODIFICAR
    df = pd.read_csv(input_dir, index_col=0)
    for col in df.columns:
        plt.plot(
            df[col], 
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col])

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for con in df.columns:
        first_year = df[con].index[0]
        plt.scatter(
            x=first_year,
            y=df[con][first_year],
            color=colors[con],
            zorder=zorder[con],
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " "+ str(df[col][first_year]) + "%",
            ha = "right",
            va = "center",
            color = colors[col],
        )

        last_year = df[con].index[-1]
        plt.scatter(
            x=last_year,
            y=df[con][last_year],
            color=colors[con],
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha = "left",
            va = "center",
            color = colors[col],
        )

        plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha = "center",
    )

    plt.tight_layout()
    plt.savefig(output_dir)
    plt.show()

 
if __name__ == "__main__":
    pregunta_01()



    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
