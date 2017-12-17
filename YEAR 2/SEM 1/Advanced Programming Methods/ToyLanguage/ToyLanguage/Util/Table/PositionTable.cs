using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToyLanguage.Util.Table
{
    class PositionTable
    {
        private int[] nextList;
        private int currentCapacity = 3;
        private int currentFree;

        private void resize()
        {
            currentCapacity = this.currentCapacity * 2;

            int[] newNextList = new int[currentCapacity];

            // copy old values
            nextList.CopyTo(newNextList, 0);


            int oldSize = nextList.Length;
            nextList = newNextList;

            // update new positions
            for (int i = oldSize - 1; i < newNextList.Length; i++)
            {
                nextList[i] = i + 1;
            }

            // there is no next after the last value
            nextList[this.nextList.Length - 1] = -1;

            // update current free position
            currentFree = nextList[oldSize - 1];
        }

        public PositionTable()
        {
            // we start at 1 because address 0 is considered NULL
            currentFree = 1;

            nextList = new int[currentCapacity];

            for(int i = 0; i < nextList.Length - 1;i++)
            {
                nextList[i] = i + 1;
            }

            nextList[nextList.Length - 1] = - 1;
        }

        public void UpdateCurrentFree()
        {
            currentFree = nextList[currentFree];

            if (currentFree == -1) resize();
        }

        public void FreePosition(int position)
        {
            int freePos = currentFree;
            currentFree = position;
            nextList[position] = freePos;
        }

        public int CurrentFree
        {
            get
            {
                return currentFree;
            }
        }
    }
}
