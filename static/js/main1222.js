

class PdfViewer {
    url = 'C:\Users\araso\Downloads\Telegram Desktop\OIPDC-master\OIPDC-master\static\Doc1.pdf';
    static pdfDoc = null;
    static pageNum = 1;
    static numPages = 0;

    constructor() {
        this.getData(PdfViewer.pageNum);
    }

    getData(pageNum){
        // Get Document
        pdfjsLib
            .getDocument(this.url)
            .promise.then(res => {
            PdfViewer.pdfDoc = res;
            PdfViewer.numPages = PdfViewer.pdfDoc.numPages;

            PdfViewer.renderPage(pageNum);
        });
    }

    // Render the page
    static renderPage(num) {
        let canvas = document.querySelector('#pdfArea');
        let ctx = canvas.getContext('2d');

        let scale = 1.5;
        // Get page
        PdfViewer.pdfDoc.getPage(num).then(page => {
            // Set scale
            const viewport = page.getViewport({ scale });
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            const renderCtx = {
                canvasContext: ctx,
                viewport
            };

            page.render(renderCtx);
        });
    }

    static reRenderCanvas(){
        setTimeout(()=>{
            PdfViewer.renderPage(PdfViewer.pageNum);
        },1000);
    }



    // Show Prev Page
    static showPrevPage() {
        if (PdfViewer.pageNum <= 1) {
            return;
        }
        PdfViewer.pageNum--;
        this.reRenderCanvas();
    }

    // Show Next Page
    static showNextPage() {

        if (PdfViewer.pageNum >= PdfViewer.numPages) {
            return;
        }
        PdfViewer.pageNum++;
        this.reRenderCanvas();
    }

}