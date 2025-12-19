from dados import obter_dados_exemplo


def main():
    df = obter_dados_exemplo()
    print("DataFrame:\n", df)
    print("\nColuna 'idade' como Series:\n", df['idade'])
    print("\nDescrição estatística:\n", df.describe())


if __name__ == '__main__':
    main()
