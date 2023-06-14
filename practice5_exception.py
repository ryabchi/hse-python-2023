{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2106f12d",
   "metadata": {},
   "outputs": [],
   "source": [
    "class EmployeeError(Exception):\n",
    "    \"\"\"\n",
    "    Исключение связанное с должностью\n",
    "    \"\"\"\n",
    "    position: str\n",
    "\n",
    "    def __init__(self, position: str):\n",
    "        self.position = position\n",
    "\n",
    "\n",
    "class NoSuchPositionError(EmployeeError):\n",
    "    \"\"\" \n",
    "    Исключение поднимается, когда нет позиции в бд\n",
    "    \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "class TeamError(Exception):\n",
    "    \"\"\"\n",
    "    Исключение связанное с командой\n",
    "    \"\"\"\n",
    "    team_name: str\n",
    "\n",
    "    def __init__(self, team_name: str):\n",
    "        self.team_name = team_name\n",
    "\n",
    "\n",
    "class NoSuchMemberError(TeamError):\n",
    "    \"\"\"\n",
    "    Исключение поднимается, когда нет сотрудника в команде\n",
    "    \"\"\"\n",
    "    member: 'Employee'\n",
    "\n",
    "    def __init__(self, team_name: str, member: 'Employee'):\n",
    "        self.member = member\n",
    "\n",
    "        super().__init__(team_name)"
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
