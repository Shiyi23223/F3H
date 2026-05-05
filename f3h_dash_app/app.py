{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ab38f11-ba32-4f09-90fb-18195bb35b10",
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash\n",
    "from dash import html\n",
    "import dash_bio as dashbio\n",
    "\n",
    "\n",
    "# 读取 FASTA\n",
    "with open(\"F3H.fasta\", \"r\") as f:\n",
    "data = f.read()\n",
    "\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "# Dash server（部署必须）\n",
    "server = app.server\n",
    "    \n",
    "app.layout = html.Div([\n",
    "    html.H2(\"F3H Sequence Alignment Viewer\"),\n",
    "    \n",
    "    dashbio.AlignmentChart(\n",
    "        id=\"alignment-viewer\",\n",
    "        data=data,\n",
    "        height=600\n",
    "    )\n",
    "    )\n",
    "if __name__ == \"__main__\":\n",
    "    app.run_server(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
