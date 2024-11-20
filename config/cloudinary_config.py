import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="dr6smcraq",
    api_key="135637553352846",
    api_secret="wgBA6eBqPvSMkVLeVUfmnyoys4s"
)


def upload_pdf(file):
    try:
        result = cloudinary.uploader.upload(file.file, resource_type="auto")
        return result.get("secure_url")
    except Exception as e:
        raise Exception(f"Error al subir el archivo a Cloudinary: {str(e)}")


def delete_pdf(document):
    try:
        # Asegúrate de extraer correctamente el `public_id`
        public_id = document.url.split("/")[-1].split(".")[0]
        cloudinary.uploader.destroy(public_id)
    except Exception as e:
        raise Exception(f"Error al eliminar el archivo a Cloudinary: {str(e)}")
