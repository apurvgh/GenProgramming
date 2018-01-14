using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace GeneralProgramming.Exchange
{
    /// <summary>
    /// This class will demonostrate how you can Process base64 binary images and 
    /// embedd them into your Outlook or any other E-mail clients
    /// </summary>
    public class ProcessBinaryImages
    {
        /// <summary>
        /// This function takes a string input which may has image HTML tags compares them to a regular expression.
        /// Depending the match it will then process every base64 value into Memory stream. 
        /// </summary>
        /// <param name="body"></param>
        /// <param name="attachmentDictionary"></param>
        /// <returns></returns>
        private string GetBody(string body, out Dictionary<string, MemoryStream> attachmentDictionary)
        {
            attachmentDictionary = new Dictionary<string, MemoryStream>();
            //This regular expression matches any base64 value.
            string regularExpImg = @"image/png;base64,(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?";
            bool isMatch = Regex.IsMatch(body, regularExpImg, RegexOptions.IgnoreCase);
            if (isMatch)
            {
                var matches = Regex.Matches(body, regularExpImg, RegexOptions.IgnoreCase);
                foreach (Match match in matches)
                {
                    var image = match.Value.Replace("image/png;base64,", "");
                    MemoryStream fileAttachment = GetImage(image);
                    //Remove the dashes and repalce as Underscores
                    var filePart = Guid.NewGuid().ToString().Replace("-", "_");
                    var fileName = $"Img{filePart}.jpg";
                    attachmentDictionary.Add(fileName, fileAttachment);
                    body = body.Replace(image, fileName);
                    //It's important to mention Cid to the actual image in the stream
                    body = body.Replace("data:image/png;base64,", "cid:");
                }

            }
            return body;
        }

        /// <summary>
        /// Return dynamic Image Number. 
        /// </summary>
        /// <param name="date"></param>
        /// <returns></returns>
        public long GetImageNumber(DateTime date)
        {
            long num = 1;
            string dateStr = date.ToString("yyMMddmmss");
            long alwaysIncrementeduniqueNum = num + 1;
            return Convert.ToInt64(dateStr + alwaysIncrementeduniqueNum);
        }

        /// <summary>
        /// Return image as Memory Stream
        /// </summary>
        /// <param name="base64String"></param>
        /// <returns></returns>
        private MemoryStream GetImage(string base64String)
        {
            Byte[] bitmapData = Convert.FromBase64String(base64String);
            MemoryStream streamBitmap = new MemoryStream(bitmapData);
            return streamBitmap;
        }



    }
}
